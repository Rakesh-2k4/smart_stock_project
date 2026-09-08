from models.transaction import Transaction
from utils.file_handler import FileHandler


class TransactionService:

    def __init__(self, filename="data/transactions.json"):
        self.filename = filename

    # -----------------------------
    # GET TRANSACTIONS
    # -----------------------------
    def get_transactions(self):

        data = FileHandler.read_json(self.filename)

        return [
            Transaction.from_dict(item)
            for item in data
        ]

    # -----------------------------
    # SAVE TRANSACTIONS
    # -----------------------------
    def save_transactions(self, transactions):

        data = [
            transaction.to_dict()
            for transaction in transactions
        ]

        FileHandler.write_json(
            self.filename,
            data
        )

    # -----------------------------
    # GENERATE TRANSACTION ID
    # -----------------------------
    def generate_transaction_id(self):

        transactions = self.get_transactions()

        if not transactions:
            return "T001"

        numbers = []

        for transaction in transactions:

            number = int(
                transaction.transaction_id[1:]
            )

            numbers.append(number)

        next_number = max(numbers) + 1

        return f"T{next_number:03d}"

    # -----------------------------
    # ADD TRANSACTION
    # -----------------------------
    def add_transaction(
        self,
        product_id,
        transaction_type,
        quantity,
        previous_stock,
        new_stock
    ):

        transactions = self.get_transactions()

        transaction_id = self.generate_transaction_id()

        transaction = Transaction(
            transaction_id,
            product_id,
            transaction_type,
            quantity,
            previous_stock,
            new_stock
        )

        transactions.append(transaction)

        self.save_transactions(transactions)

        return transaction

    # -----------------------------
    # GET ALL TRANSACTIONS
    # -----------------------------
    def get_all_transactions(self):

        return self.get_transactions()

    # -----------------------------
    # SEARCH BY PRODUCT
    # -----------------------------
    def search_by_product(self, product_id):

        transactions = self.get_transactions()

        return [
            transaction
            for transaction in transactions
            if transaction.product_id == product_id
        ]