import shopify
import os
import time
import requests

STORE = os.getenv("STORE_NAME") + ".myshopify.com"
TOKEN = "your_admin_api_token"  # 자동 생성 후 입력

shopify.ShopifyResource.set_site(f"https://{STORE}/admin/api/2023-10")
shopify.ShopifyResource.headers.update({"X-Shopify-Access-Token": TOKEN})

def auto_upload():
    p = shopify.Product()
    p.title = "Wireless Earbuds"
    p.body_html = "Hot sale item from AliExpress"
    p.vendor = "AutoBot"
    p.images = [{"src": "https://ae01.alicdn.com/kf/Sb1.jpg"}]
    p.variants = [{"price": "29.99", "inventory_quantity": 100}]
    p.save()
    print("✅ 상품 등록 완료")

def auto_check_orders():
    orders = shopify.Order.find(limit=5, financial_status="paid")
    for o in orders:
        profit = float(o.total_price) - 12.99
        print(f"💰 수익: ${profit:.2f}")

if __name__ == "__main__":
    auto_upload()
    while True:
        auto_check_orders()
        time.sleep(3600)
