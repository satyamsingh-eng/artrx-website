import asyncio
import json
from playwright.async_api import async_playwright

async def google_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
        page = await context.new_page()
        
        queries = [
            'Thanvi Suvva',
            'Thanvi Suvva LinkedIn',
            'site:linkedin.com "Thanvi Suvva"',
            'site:linkedin.com/in/ "Thanvi Suvva"'
        ]
        
        for q in queries:
            print(f"=== Playwright Google Search: {q} ===")
            try:
                await page.goto(f'https://www.google.com/search?q={q}', wait_until='domcontentloaded')
                await page.wait_for_timeout(2000)
                
                results = await page.eval_on_selector_all('div.g, div.MjjYud', '''
                    nodes => nodes.map(n => {
                        const titleEl = n.querySelector('h3');
                        const linkEl = n.querySelector('a');
                        const snippetEl = n.querySelector('div.VwiC3b, div.IsZvec');
                        return {
                            title: titleEl ? titleEl.innerText : '',
                            url: linkEl ? linkEl.href : '',
                            snippet: snippetEl ? snippetEl.innerText : ''
                        };
                    }).filter(r => r.title && r.url)
                ''')
                
                print(f"Found {len(results)} Google results:")
                for r in results[:5]:
                    print(f"  Title: {r['title']}\n  URL: {r['url']}\n  Snippet: {r['snippet']}\n  ---")
            except Exception as e:
                print("Error:", e)
            print()
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(google_playwright())
