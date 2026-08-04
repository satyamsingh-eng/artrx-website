import asyncio
import json
from playwright.async_api import async_playwright

urls = [
    'https://artrx.co/',
    'https://artrx.co/about-the-founder',
    'https://artrx.co/gallery',
    'https://artrx.co/our-partners',
    'https://artrx.co/contact-us'
]

async def run_qa():
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for url in urls:
            context = await browser.new_context(viewport={'width': 1280, 'height': 800})
            page = await context.new_page()
            
            console_errors = []
            page.on('console', lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ['error', 'warning'] else None)
            
            page_errors = []
            page.on('pageerror', lambda err: page_errors.append(str(err)))
            
            print(f"Auditing {url}...")
            try:
                response = await page.goto(url, wait_until='domcontentloaded', timeout=20000)
                await page.wait_for_timeout(2000)
                
                status = response.status if response else 0
                title = await page.title()
                
                # Check meta elements
                meta_tags = await page.evaluate('''() => {
                    const tags = {};
                    document.querySelectorAll('meta').forEach(m => {
                        const name = m.getAttribute('name') || m.getAttribute('property');
                        if (name) tags[name] = m.getAttribute('content');
                    });
                    return tags;
                }''')
                
                # Check heading hierarchy
                headings = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6')).map(h => ({
                        level: h.tagName,
                        text: h.innerText.trim()
                    }));
                }''')
                
                # Check images
                image_checks = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('img')).map(img => ({
                        src: img.src,
                        alt: img.alt,
                        complete: img.complete,
                        naturalWidth: img.naturalWidth,
                        naturalHeight: img.naturalHeight,
                        isBroken: img.complete && img.naturalWidth === 0
                    }));
                }''')
                
                # Check form inputs
                forms = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('form')).map(f => ({
                        action: f.action,
                        method: f.method,
                        inputs: Array.from(f.querySelectorAll('input, textarea, select')).map(i => ({
                            type: i.type,
                            name: i.name,
                            id: i.id,
                            required: i.required,
                            placeholder: i.placeholder
                        }))
                    }));
                }''')
                
                # Mobile view audit
                mobile_page = await context.new_page()
                await mobile_page.set_viewport_size({'width': 375, 'height': 667})
                await mobile_page.goto(url, wait_until='domcontentloaded')
                await mobile_page.wait_for_timeout(1000)
                has_overflow = await mobile_page.evaluate('document.documentElement.scrollWidth > window.innerWidth')
                await mobile_page.close()
                
                results[url] = {
                    'status': status,
                    'title': title,
                    'meta_tags': meta_tags,
                    'headings': headings,
                    'image_checks': image_checks,
                    'forms': forms,
                    'console_errors': console_errors,
                    'page_errors': page_errors,
                    'mobile_overflow': has_overflow
                }
                print(f"Completed audit for {url}")
            except Exception as e:
                print(f"Error auditing {url}: {e}")
            finally:
                await page.close()
                await context.close()
                
        await browser.close()
        
    with open('/tmp/artrx_qa_raw.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("QA audit complete. Results saved to /tmp/artrx_qa_raw.json")

if __name__ == '__main__':
    asyncio.run(run_qa())
