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

async def scrape_all():
    site_data = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        
        for url in urls:
            page = await context.new_page()
            print(f"Navigating to {url}...")
            try:
                response = await page.goto(url, wait_until='domcontentloaded', timeout=15000)
                await page.wait_for_timeout(3000)
                
                title = await page.title()
                body_text = await page.inner_text('body')
                
                meta_desc = ''
                desc_elem = await page.query_selector('meta[name="description"], meta[property="og:description"]')
                if desc_elem:
                    meta_desc = await desc_elem.get_attribute('content') or ''
                
                images = await page.eval_on_selector_all('img', '''
                    imgs => imgs.map(img => ({
                        src: img.src,
                        alt: img.alt,
                        width: img.offsetWidth,
                        height: img.offsetHeight
                    }))
                ''')
                
                links = await page.eval_on_selector_all('a', '''
                    anchors => anchors.map(a => ({
                        text: a.innerText.trim(),
                        href: a.href
                    }))
                ''')
                
                design_info = await page.evaluate('''() => {
                    const body = document.body;
                    const style = window.getComputedStyle(body);
                    const h1 = document.querySelector('h1');
                    const h1Style = h1 ? window.getComputedStyle(h1) : null;
                    return {
                        fontFamily: style.fontFamily,
                        backgroundColor: style.backgroundColor,
                        textColor: style.color,
                        h1Font: h1Style ? h1Style.fontFamily : null,
                        h1Color: h1Style ? h1Style.color : null
                    };
                }''')
                
                page_slug = url.replace('https://artrx.co/', '').replace('/', '') or 'home'
                screenshot_path = f'/tmp/artrx_{page_slug}.png'
                await page.screenshot(path=screenshot_path, full_page=True)
                
                site_data[url] = {
                    'title': title,
                    'meta_description': meta_desc,
                    'status': response.status if response else 0,
                    'body_text': body_text,
                    'images': images,
                    'links': links,
                    'design_info': design_info,
                    'screenshot': screenshot_path
                }
                print(f"Successfully scraped {url} ({len(body_text)} chars)")
            except Exception as e:
                print(f"Error scraping {url}: {e}")
            finally:
                await page.close()
                
        await browser.close()
        
    with open('/tmp/artrx_full_scrape.json', 'w') as f:
        json.dump(site_data, f, indent=2)
    print("Full Playwright scrape completed and saved.")

if __name__ == '__main__':
    asyncio.run(scrape_all())
