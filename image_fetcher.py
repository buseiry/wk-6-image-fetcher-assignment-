import requests
import os
from urllib.parse import urlparse
import mimetypes
import uuid

def get_filename_from_url(url):
    """Extract a safe filename from URL or generate one."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or "." not in filename:  # No proper filename
        filename = f"image_{uuid.uuid4().hex[:8]}.jpg"
    return filename

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for one or more URLs (comma separated)
    urls_input = input("Please enter one or more image URLs (separate with commas): ").strip()
    urls = [u.strip() for u in urls_input.split(",") if u.strip()]

    # Create directory if not exists
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        print(f"\nProcessing: {url}")

        try:
            # First do a HEAD request to check headers
            head = requests.head(url, timeout=10, allow_redirects=True)
            head.raise_for_status()

            content_type = head.headers.get("Content-Type", "")
            if not content_type.startswith("image"):
                print(f"✗ Skipped: Not an image (Content-Type={content_type})")
                continue

            # Now download the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            filename = get_filename_from_url(url)
            filepath = os.path.join("Fetched_Images", filename)

            # Skip if file already exists (duplicate prevention)
            if os.path.exists(filepath):
                print(f"✓ Skipped download: {filename} already exists.")
                continue

            # Save image in binary mode
            with open(filepath, 'wb') as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
