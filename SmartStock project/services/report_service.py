from services.product_service import ProductService
from services.sale_service import SaleService


class ReportService:

    def __init__(self):
        self.product_service = ProductService()
        self.sale_service = SaleService()

    # -----------------------------
    # INVENTORY SUMMARY
    # -----------------------------
    def inventory_summary(self):

        products = self.product_service.get_products()

        total_products = len(products)

        total_quantity = sum(
            product.quantity
            for product in products
        )

        total_stock_value = sum(
            product.quantity * product.purchase_price
            for product in products
        )

        low_stock_count = sum(
            1
            for product in products
            if product.quantity <= product.reorder_level
            and product.quantity > 0
        )

        out_of_stock_count = sum(
            1
            for product in products
            if product.quantity == 0
        )

        return {
            "total_products": total_products,
            "total_quantity": total_quantity,
            "total_stock_value": total_stock_value,
            "low_stock_count": low_stock_count,
            "out_of_stock_count": out_of_stock_count
        }

    # -----------------------------
    # SALES SUMMARY
    # -----------------------------
    def sales_summary(self):

        sales = self.sale_service.get_all_sales()

        total_sales = sum(
            sale.total_amount
            for sale in sales
        )

        total_profit = sum(
            sale.profit
            for sale in sales
        )

        total_items_sold = sum(
            sale.quantity
            for sale in sales
        )

        return {
            "total_sales": total_sales,
            "total_profit": total_profit,
            "total_items_sold": total_items_sold,
            "total_sale_records": len(sales)
        }

    # -----------------------------
    # COMPLETE REPORT
    # -----------------------------
    def complete_report(self):

        inventory = self.inventory_summary()
        sales = self.sales_summary()

        print("\n============================================")
        print("          SMARTSTOCK BUSINESS REPORT")
        print("============================================")

        print("\n----------- INVENTORY SUMMARY -----------")

        print(
            f"Total Products       : "
            f"{inventory['total_products']}"
        )

        print(
            f"Total Stock Quantity : "
            f"{inventory['total_quantity']}"
        )

        print(
            f"Stock Value          : ₹"
            f"{inventory['total_stock_value']:.2f}"
        )

        print(
            f"Low Stock Products   : "
            f"{inventory['low_stock_count']}"
        )

        print(
            f"Out of Stock         : "
            f"{inventory['out_of_stock_count']}"
        )

        print("\n----------- SALES SUMMARY -----------")

        print(
            f"Total Items Sold     : "
            f"{sales['total_items_sold']}"
        )

        print(
            f"Total Sale Records   : "
            f"{sales['total_sale_records']}"
        )

        print(
            f"Total Revenue        : ₹"
            f"{sales['total_sales']:.2f}"
        )

        print(
            f"Total Profit         : ₹"
            f"{sales['total_profit']:.2f}"
        )

        print("\n============================================")