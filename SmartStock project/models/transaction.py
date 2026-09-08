from datetime import datetime


class Transaction:

    def __init__(
        self,
        transaction_id,
        product_id,
        transaction_type,
        quantity,
        previous_stock,
        new_stock
    ):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.previous_stock = previous_stock
        self.new_stock = new_stock
        self.date_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "product_id": self.product_id,
            "transaction_type": self.transaction_type,
            "quantity": self.quantity,
            "previous_stock": self.previous_stock,
            "new_stock": self.new_stock,
            "date_time": self.date_time
        }

    @classmethod
    def from_dict(cls, data):

        transaction = cls(
            data["transaction_id"],
            data["product_id"],
            data["transaction_type"],
            data["quantity"],
            data["previous_stock"],
            data["new_stock"]
        )

        transaction.date_time = data["date_time"]

        return transaction

    def display(self):

        print("\n--------------------------------------------")
        print(f"Transaction ID : {self.transaction_id}")
        print(f"Product ID     : {self.product_id}")
        print(f"Type           : {self.transaction_type}")
        print(f"Quantity       : {self.quantity}")
        print(f"Previous Stock : {self.previous_stock}")
        print(f"New Stock      : {self.new_stock}")
        print(f"Date & Time    : {self.date_time}")