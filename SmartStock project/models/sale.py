from datetime import datetime


class Sale:

    def __init__(
        self,
        sale_id,
        product_id,
        product_name,
        quantity,
        selling_price,
        total_amount,
        profit
    ):
        self.sale_id = sale_id
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.selling_price = selling_price
        self.total_amount = total_amount
        self.profit = profit
        self.date_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def to_dict(self):

        return {
            "sale_id": self.sale_id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "quantity": self.quantity,
            "selling_price": self.selling_price,
            "total_amount": self.total_amount,
            "profit": self.profit,
            "date_time": self.date_time
        }

    @classmethod
    def from_dict(cls, data):

        sale = cls(
            data["sale_id"],
            data["product_id"],
            data["product_name"],
            data["quantity"],
            data["selling_price"],
            data["total_amount"],
            data["profit"]
        )

        sale.date_time = data["date_time"]

        return sale

    def display(self):

        print("\n--------------------------------------------")
        print(f"Sale ID        : {self.sale_id}")
        print(f"Product ID     : {self.product_id}")
        print(f"Product Name   : {self.product_name}")
        print(f"Quantity       : {self.quantity}")
        print(f"Selling Price  : ₹{self.selling_price:.2f}")
        print(f"Total Amount   : ₹{self.total_amount:.2f}")
        print(f"Profit         : ₹{self.profit:.2f}")
        print(f"Date & Time    : {self.date_time}")