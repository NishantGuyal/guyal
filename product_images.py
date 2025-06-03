import pandas as pd
import os
import requests
from urllib.parse import urlparse
from pathlib import Path

# Load your Excel file
df = pd.read_csv("products_images.csv")  # Replace with your actual file path

# Iterate over rows
for index, row in df.iterrows():
    sku = str(row.get("SKU"))
    image_url = row.get("Image Url")

    if not sku or pd.isna(image_url):
        print(f"Error in SKU {sku}")
        continue

    image_url = str(image_url).strip()  # Ensure it's a string

    folder_path = Path(f"images/{sku}")
    folder_path.mkdir(parents=True, exist_ok=True)

    parsed_url = urlparse(image_url)
    ext = os.path.splitext(parsed_url.path)[1]

    if not ext:
        ext = ".jpg"

    image_path = folder_path / f"{sku}{ext}"

    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Saved: {image_path}")
    except Exception as e:
        print(f"Error downloading image for SKU {sku}: {e}")
