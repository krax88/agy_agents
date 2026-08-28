import os
import re
import urllib.request
import urllib.parse
import json
import time
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15'
]

def clean_html(raw_html):
    clean_re = re.compile('<.*?>')
    return re.sub(clean_re, '', raw_html)

def execute_duckduckgo_search(query):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    
    retries = 3
    backoff = 10
    
    for attempt in range(retries):
        user_agent = random.choice(USER_AGENTS)
        req = urllib.request.Request(
            url,
            headers={'User-Agent': user_agent}
        )
        
        try:
            with urllib.request.urlopen(req, timeout=12) as response:
                html = response.read().decode('utf-8', errors='ignore')
                return html
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"  [Attempt {attempt+1}/{retries}] HTTP 403 Forbidden. Backing off for {backoff}s...")
                time.sleep(backoff)
                backoff *= 2  # Exponential backoff
            else:
                print(f"  HTTP Error {e.code} searching for '{query}': {e.reason}")
                return None
        except Exception as e:
            print(f"  Error searching for '{query}': {e}")
            return None
            
    print(f"  Failed all search attempts for '{query}' due to rate limits.")
    return None

def parse_ddg_results(html):
    if not html:
        return []
    
    results = []
    
    # Locate results links and descriptions
    # DDG HTML Search links format: <a class="result__link" href="...">Title</a>
    # DDG HTML Search snippets format: <a class="result__snippet" href="...">Snippet</a>
    
    link_pattern = re.compile(r'<a\s+class="result__link"\s+href="([^"]+)">([^<]+)</a>', re.DOTALL)
    snippet_pattern = re.compile(r'<a\s+class="result__snippet"\s+href="[^"]+">([^<]+)</a>', re.DOTALL)
    
    links = link_pattern.findall(html)
    snippets = snippet_pattern.findall(html)
    
    for i in range(min(len(links), 5)):
        link, title = links[i]
        snippet = snippets[i] if i < len(snippets) else ""
        
        if "uddg=" in link:
            parsed_link = urllib.parse.unquote(link.split("uddg=")[1].split("&")[0])
        else:
            parsed_link = link
            
        results.append({
            "title": title.strip(),
            "url": parsed_link.strip(),
            "snippet": snippet.strip()
        })
        
    return results

def main():
    print("Initializing Robust 100+ Search Financial & Strategic Harvester...")
    
    # 102 queries list
    queries = [
        # Sandvik Annual Reports (2016-2025)
        'site:home.sandvik "annual report" 2016 filetype:pdf',
        'site:home.sandvik "annual report" 2017 filetype:pdf',
        'site:home.sandvik "annual report" 2018 filetype:pdf',
        'site:home.sandvik "annual report" 2019 filetype:pdf',
        'site:home.sandvik "annual report" 2020 filetype:pdf',
        'site:home.sandvik "annual report" 2021 filetype:pdf',
        'site:home.sandvik "annual report" 2022 filetype:pdf',
        'site:home.sandvik "annual report" 2023 filetype:pdf',
        'site:home.sandvik "annual report" 2024 filetype:pdf',
        'site:home.sandvik "annual report" 2025 filetype:pdf',
        # Sandvik Interim Reports (2016-2026)
        'site:home.sandvik "interim report" "Q1" 2016 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2016 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2016 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2017 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2017 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2017 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2018 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2018 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2018 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2019 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2019 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2019 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2020 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2020 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2020 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2021 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2021 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2021 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2022 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2022 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2022 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2023 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2023 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2023 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2024 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2024 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2024 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2025 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2025 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2025 filetype:pdf',
        'site:home.sandvik "interim report" "Q1" 2026 filetype:pdf',
        'site:home.sandvik "interim report" "Q2" 2026 filetype:pdf',
        'site:home.sandvik "interim report" "Q3" 2026 filetype:pdf',
        # Alleima Annual Reports (2022-2025)
        'site:alleima.com "annual report" 2022 filetype:pdf',
        'site:alleima.com "annual report" 2023 filetype:pdf',
        'site:alleima.com "annual report" 2024 filetype:pdf',
        'site:alleima.com "annual report" 2025 filetype:pdf',
        # Alleima Interim Reports (2022-2026)
        'site:alleima.com "interim report" "Q1" 2022 filetype:pdf',
        'site:alleima.com "interim report" "Q2" 2022 filetype:pdf',
        'site:alleima.com "interim report" "Q3" 2022 filetype:pdf',
        'site:alleima.com "interim report" "Q1" 2023 filetype:pdf',
        'site:alleima.com "interim report" "Q2" 2023 filetype:pdf',
        'site:alleima.com "interim report" "Q3" 2023 filetype:pdf',
        'site:alleima.com "interim report" "Q1" 2024 filetype:pdf',
        'site:alleima.com "interim report" "Q2" 2024 filetype:pdf',
        'site:alleima.com "interim report" "Q3" 2024 filetype:pdf',
        'site:alleima.com "interim report" "Q1" 2025 filetype:pdf',
        'site:alleima.com "interim report" "Q2" 2025 filetype:pdf',
        'site:alleima.com "interim report" "Q3" 2025 filetype:pdf',
        'site:alleima.com "interim report" "Q1" 2026 filetype:pdf',
        'site:alleima.com "interim report" "Q2" 2026 filetype:pdf',
        'site:alleima.com "interim report" "Q3" 2026 filetype:pdf',
        # Sandvik Strategic Press Releases
        'site:home.sandvik "capital markets day" 2018 filetype:pdf',
        'site:home.sandvik "capital markets day" 2020 filetype:pdf',
        'site:home.sandvik "capital markets day" 2022 filetype:pdf',
        'site:home.sandvik "capital markets day" 2024 filetype:pdf',
        'site:home.sandvik "acquisition" "digital" OR "software" 2020',
        'site:home.sandvik "acquisition" "digital" OR "software" 2021',
        'site:home.sandvik "acquisition" "digital" OR "software" 2022',
        'site:home.sandvik "acquisition" "digital" OR "software" 2023',
        'site:home.sandvik "acquisition" "digital" OR "software" 2024',
        'site:home.sandvik "acquisition" "digital" OR "software" 2025',
        'site:home.sandvik "AutoMine" OR "OptiMine" press release',
        'site:home.sandvik "STATCOM" "Sandviken" electricity grid',
        'site:home.sandvik "automation" "machining" press release 2025',
        'site:home.sandvik "restructuring" OR "efficiency measures" 2025',
        # Alleima Strategic Press Releases
        'site:alleima.com "capital markets day" 2022 filetype:pdf',
        'site:alleima.com "capital markets day" 2024 filetype:pdf',
        'site:alleima.com "spin-off" "Sandvik Materials Technology" 2022',
        'site:alleima.com "Tube Mill 2026" OR "SMR" press release',
        'site:alleima.com "Kanthal" "Hallstahammar" investment',
        'site:alleima.com "Kanthal" "electrification" semiconductors',
        'site:alleima.com "medical" "Penang" OR "Malaysia" investment',
        'site:alleima.com "medical" "Palm Coast" wire production',
        'site:alleima.com "restructuring" OR "efficiency measures" 2025',
        'site:alleima.com "AlleMind" OR "Guru" artificial intelligence',
        'site:alleima.com "STATCOM" "Sandviken" EAF grid',
        'site:alleima.com "Life Cycle Assessment" OR "Sanmac" emissions',
        'site:alleima.com "bipolar plates" "hydrogen" strip steel',
        'site:alleima.com "decarbonization" OR "Scope 1 and 2" target',
        # Competitors
        'site:nipponsteel.com "digital strategy" OR "AI" annual report',
        'site:nipponsteel.com "EAF" "carbon neutrality" target',
        'site:tubacex.com "annual report" 2025 filetype:pdf',
        'site:tubacex.com "strategic plan" OR "digitalization" 2025',
        'site:salzgitter-ag.com "SALCOS" hydrogen steelmaking',
        'site:salzgitter-ag.com "annual report" 2025 filetype:pdf',
        'site:jiuli.com "annual report" 2025 OR "digitalization"',
        'site:haynesintl.com "annual report" 2025 filetype:pdf',
        'site:haynesintl.com "acquisition" OR "merger" 2024',
        'site:aperam.com "annual report" 2025 filetype:pdf',
        'site:aperam.com "recycling" "EAF" emissions footprint',
        'site:aperam.com "ELG" acquisition alloy scrap'
    ]
    
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "financial_search_results.json")
    
    # Load existing results if any to support resuming
    all_results = {}
    if os.path.exists(output_file):
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                all_results = json.load(f)
            print(f"Loaded {len(all_results)} existing queries from index.")
        except Exception:
            pass
            
    success_count = sum(1 for q, r in all_results.items() if r)
    
    for idx, query in enumerate(queries):
        if query in all_results and all_results[query]:
            print(f"[{idx+1}/{len(queries)}] Skipping already completed query: {query}")
            continue
            
        print(f"[{idx+1}/{len(queries)}] Executing: {query}")
        html = execute_duckduckgo_search(query)
        results = parse_ddg_results(html)
        
        all_results[query] = results
        if results:
            success_count += 1
            print(f"  - Found {len(results)} results")
        else:
            print("  - No results returned")
            
        # Write partial progress after every query
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_results, f, indent=2, ensure_ascii=False)
            
        # Throttling
        time.sleep(random.uniform(2.0, 4.0))
        
    print(f"\nAll operations completed. Results written to '{output_file}'. Successful: {success_count}/{len(queries)}")

if __name__ == '__main__':
    main()
