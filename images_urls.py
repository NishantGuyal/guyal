import pandas as pd

df = pd.read_csv("products_images.csv")

base_url = "https://nishantguyal.github.io/guyal"

df["Image URL"] = df["SKU"].apply(
    lambda sku: f"{base_url}/{sku}/{sku}.jpg" if pd.notna(sku) else ""
)

df[["SKU", "Image URL"]].to_csv("image_urls.csv", index=False)

print("✅ SKU to Image URL mapping saved to 'image_urls.csv'")
