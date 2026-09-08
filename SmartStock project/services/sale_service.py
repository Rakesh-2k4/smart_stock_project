from models.sale import Sale
from utils.file_handler import FileHandler


class SaleService:

    def __init__(self, filename="data/sales.json"):
        self.filename = filename

    # -----------------------------
    # GET SALES
    # -----------------------------
    def get_sales(self):

        data = FileHandler.read_json(self.filename)

        return [
            Sale.from_dict(item)
            for item in data
        ]

    # -----------------------------
    # SAVE SALES
    # -----------------------------
    def save_sales(self, sales):

        data = [
            sale.to_dict()
            for sale in sales
        ]

        FileHandler.write_json(
            self.filename,
            data
        )

    # -----------------------------
    # GENERATE SALE ID
    # -----------------------------
    def generate_sale_id(self):

        sales = self.get_sales()

        if not sales:
            return "S001"

        numbers = []

        for sale in sales:

            number = int(
                sale.sale_id[1:]
            )

            numbers.append(number)

        next_number = max(numbers) + 1

        return f"S{next_number:03d}"

    # -----------------------------
    # RECORD SALE
    # -----------------------------
    def add_sale(
        self,
        product,
        quantity
    ):

        sales = self.get_sales()

        sale_id = self.generate_sale_id()

        selling_price = product.selling_price
        purchase_price = product.purchase_price

        total_amount = selling_price * quantity

        profit = (
            selling_price - purchase_price
        ) * quantity

        sale = Sale(
            sale_id,
            product.product_id,
            product.name,
            quantity,
            selling_price,
            total_amount,
            profit
        )

        sales.append(sale)

        self.save_sales(sales)

        return sale

    # -----------------------------
    # GET ALL SALES
    # -----------------------------
    def get_all_sales(self):

        return self.get_sales()

    # -----------------------------
    # TOTAL SALES
    # -----------------------------
    def get_total_sales(self):

        sales = self.get_sales()

        return sum(
            sale.total_amount
            for sale in sales
        )

    # -----------------------------
    # TOTAL PROFIT
    # -----------------------------
    def get_total_profit(self):

        sales = self.get_sales()

        return sum(
            sale.profit
            for sale in sales
        )