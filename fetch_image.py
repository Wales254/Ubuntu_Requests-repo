import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Ask user for image URL
    image_url = input("Please enter the image URL: ").strip()

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Send HTTP request to fetch the image
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes

        # Extract filename from URL
        parsed_url = urlparse(image_url)
        filename = os.path.basename(parsed_url.path)
        if not filename:  # If no filename in URL, give a default one
            filename = "downloaded_image.jpg"

        # Save the image
        save_path = os.path.join(save_dir, filename)
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print("⚠️ Failed to fetch the image. Error:", e)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
