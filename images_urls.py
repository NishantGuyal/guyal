import pandas as pd

# Load your CSV that contains SKUs
df = pd.read_csv("products_images.csv")  # Replace with your actual file

# Base URL for GitHub Pages
base_url = "https://nishantguyal.github.io/guyal"


# Construct the image URL for each SKU
df["Image URL"] = df["SKU"].apply(
    lambda sku: f"{base_url}/{sku}/{sku}.jpg" if pd.notna(sku) else ""
)

# Optional: Save to a new file with just SKU and URL
df[["SKU", "Image URL"]].to_csv("image_urls.csv", index=False)

print("✅ SKU to Image URL mapping saved to 'image_urls.csv'")
