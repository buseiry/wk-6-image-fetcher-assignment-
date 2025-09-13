# Ubuntu Image Fetcher 

This Python tool downloads images from the internet and saves them locally with safety checks.

## Features
- Accepts multiple image URLs at once
- Checks headers to ensure files are images
- Prevents downloading duplicate images
- Saves all images into `Fetched_Images` folder
- Handles errors gracefully

## How to Run
1. Install Python 3 and the `requests` library:
   pip install requests

2. Run the script:
   python ubuntu_image_fetcher.py

3. Enter one or more image URLs separated by commas.

## Output
- Images saved to `Fetched_Images` directory
- Graceful error handling for bad URLs or network issues

## Ubuntu Principles
Community, Respect, Sharing, and Practicality are reflected in this script by:
- Connecting to the wider web community
- Handling errors gracefully
- Organizing fetched images for later sharing
- Serving a real need
