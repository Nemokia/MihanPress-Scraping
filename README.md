# MihanPress-Scraping
 This Python script scrapes a WordPress-based website for video and PDF resources. It organizes downloads into uniquely named folders, ensures sanitized folder names, and downloads files sequentially. The tool handles invalid characters and processes each resource efficiently.
# WordPress Scraper

## Overview
This Python script scrapes a WordPress-based website to extract and download video and PDF resources. Each resource is organized into uniquely named folders for better file management. The script handles invalid folder names and ensures sequential processing of resources.

## Features
- Automatically identifies and downloads video files (`.mp4`) and PDF documents from the specified website.
- Creates structured folders named sequentially with sanitized folder names based on the video file name.
- Handles errors gracefully, ensuring uninterrupted execution even if some resources are unavailable.

## Prerequisites
- Python 3.6+
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `re` (part of Python standard library)

To install the required libraries, run:
```bash
pip install requests beautifulsoup4
```

## How to Use
1. Clone or download this repository.
2. Open the script file and ensure the `base_url` variable is set to the URL of the WordPress page you want to scrape (default: `https://mihanwp.com/wordpress-learn/`).
3. Run the script:
```bash
python wordpress_scraper.py
```
4. The script will create numbered folders (`1-name`, `2-name`, etc.) in the current directory, each containing the relevant video and PDF files.

## Example Output Structure
```
.
|-- 1-how-to-build-a-website
|   |-- how-to-build-a-website.mp4
|   |-- guide.pdf
|-- 2-what-is-domain-name
|   |-- what-is-domain-name.mp4
|   |-- reference.pdf
```

## Notes
- The script assumes the presence of specific HTML structures on the target website (e.g., `<video>` tags for videos and `<a>` tags for PDFs).
- If the structure of the target site changes, modifications to the script may be necessary.
