import os
import requests
from bs4 import BeautifulSoup
import re

def sanitize_folder_name(folder_name):
    """Sanitize the folder name to remove invalid characters."""
    return re.sub(r'[\\/:*?"<>|]', '_', folder_name)

def create_folder(folder_name):
    """Create a folder if it doesn't already exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_file(url, folder_name, file_name):
    """Download a file and save it to the specified folder."""
    print(f"Starting download from: {url}")
    file_path = os.path.join(folder_name, file_name)
    if os.path.exists(file_path):
        print(f"Already downloaded: {file_path}")
        return
    try:
        response = requests.get(url, stream=True)
        print(f"HTTP GET request sent. Status code: {response.status_code}")
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while downloading {url}: {e}")

def scrape_and_download(base_url):
    """Scrape the website for video and PDF links and download them."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article', class_='home-post borderbox')
    folder_count = 1

    for article in articles:
        # Extract the article link
        a_tag = article.find('a', href=True)
        if not a_tag:
            continue

        article_url = a_tag['href']
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.text, 'html.parser')

        # Extract video link
        video_tag = article_soup.find('figure', class_='wp-block-video aligncenter')
        if video_tag:
            video = video_tag.find('video', src=True)
            if video:
                video_src = video['src']
                folder_name = f"{folder_count}-{sanitize_folder_name(video_src.split('/')[-1].split('.')[0])}"
                create_folder(folder_name)
                download_file(video_src, folder_name, video_src.split('/')[-1])
                folder_count += 1

        # Extract PDF link
        pdf_button = article_soup.find('div', class_='wp-block-button')
        if pdf_button:
            pdf_tag = pdf_button.find('a', class_='wp-block-button__link wp-element-button', href=True)
            if pdf_tag:
                pdf_url = pdf_tag['href']
                download_file(pdf_url, folder_name, pdf_url.split('/')[-1])
        elif article_url.endswith('.pdf'):
            download_file(article_url, folder_name, article_url.split('/')[-1])
        else:
            print(f"Failed to download {pdf_url}")
            pass


if __name__ == "__main__":
    base_url = "https://mihanwp.com/wordpress-learn/"
    scrape_and_download(base_url)
