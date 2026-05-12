from content_extractor import extract_report_content, fetch_url_content

# Usage
# 1. Update the provider name: aws, azure, cloudflare, google
# 2. Update the search terms
# 3. Update the list of urls (for Azure incidents, report content must be stored in a plain .txt file, and url should be the file path)
# 4. Run the script ($ python key_selector)

provider = 'google'

search_terms = [
    "bug",
    "latent issue",
    "unhandled exception",
    "exception",
    "race condition",
    "unexpected behavior",
    "function error",
    "logic error",
    "syntax error",
    "unhandled error",
    "throttling logic",
    "function logic",
    "code",
    "software",
    "memory leak",
    "glitch",
    "deadlock",
    "null pointer",
    "concurrency"
]

urls_to_scan = [
    "https://status.cloud.google.com/incidents/1yphfNLPHEnwJcWqwxbu"
]


def filter_relevant_reports(provider, url_list, keywords):
    """
    Fetches URLs and checks if the extracted content contains any of the keywords.
    """
    relevant_urls = []
    keywords_lower = [kw.lower() for kw in keywords]

    for url in url_list:
        content = fetch_url_content(provider, url)
        content_text = extract_report_content(provider, content)
        
        # Check if any keyword exists in the extracted text
        if any(keyword in content_text for keyword in keywords_lower):
            relevant_urls.append(url)
            print(f"[MATCH] Found keywords in: {url}")
        else:
            print(f"[SKIP] No keywords in: {url}")
            
    return relevant_urls


if __name__ == "__main__":

    print("Starting scan...")
    matched_reports = filter_relevant_reports(provider, urls_to_scan, search_terms)
    
    print("\n--- Final Results ---")
    print(f"Total reports found: {len(matched_reports)}")
    for matched_url in matched_reports:
        print(matched_url)
