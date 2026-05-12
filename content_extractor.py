import requests
from bs4 import BeautifulSoup

def fetch_url_content(provider, url):

    if provider == 'azure':
        return load_from_local_file_system(url)
    
    return load_from_web(url)


def load_from_local_file_system(url):
    try:
        with open(url, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found for URL: {url}")
    except Exception as e:
        print(f"[FAILED] An exception occured when handling URL {url}: {e}")

    return ""


def load_from_web(url):
    with requests.Session() as session:
        try:
            # 10-second timeout prevents the script from hanging on unresponsive servers
            response = session.get(url, timeout=10)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                return response.text
            else:
                print(f"[ERROR] HTTP {response.status_code} for URL: {url}")

        except requests.exceptions.RequestException as e:
            print(f"[FAILED] Could not fetch {url}. Reason: {e}")
    
    return ""



def extract_report_content(provider, content):

    if provider == "aws":
        return extract_aws_report_content(content)
    if provider == "azure":
        return extract_azure_report_content(content)
    if provider == "cloudflare":
        return extract_cloudflare_report_content(content)
    if provider == "google":
        return extract_google_report_content(content)



def extract_aws_report_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    incident_report = soup.find('div', class_='main-container')

    return incident_report.get_text(separator=' ', strip=True).lower()


def extract_azure_report_content(content):
    return content


def extract_cloudflare_report_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    incident_report = soup.find('article', class_='post-full')

    return incident_report.get_text(separator=' ', strip=True).lower()


def extract_google_report_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    updates_table = soup.find('table', class_='status-updates')
    incident_report = updates_table.find('tr')

    return incident_report.get_text(separator=' ', strip=True).lower()
