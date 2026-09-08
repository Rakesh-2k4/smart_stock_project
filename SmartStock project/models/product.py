from datetime import datetime


class Product:
    """
    Represents a product in the SmartStock system.
    """

    # Class variable
    total_products = 0

    def __init__(
        self,
        product_id,
        name,
        category,
        purchase_price,
        selling_price,
        quantity,
        reorder_level,
        supplier_id
    ):
        """
        Constructor for Product.
        """

        self.product_id = product_id
        self.name = name
        self.category = category
        self.purchase_price = float(purchase_price)
        self.selling_price = float(selling_price)
        self.quantity = int(quantity)
        self.reorder_level = int(reorder_level)
        self.supplier_id = supplier_id

        self.created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        Product.total_products += 1

    # -------------------------------
    # INSTANCE METHODS
    # -------------------------------

    def add_stock(self, quantity):
        """
        Increase the available stock.
        """

        if quantity <= 0:
            raise ValueError(
                "Stock quantity must be greater than zero."
            )

        self.quantity += quantity

    def remove_stock(self, quantity):
        """
        Decrease the available stock.
        """

        if quantity <= 0:
            raise ValueError(
                "Stock quantity must be greater than zero."
            )

        if quantity > self.quantity:
            raise ValueError(
                "Insufficient stock available."
            )

        self.quantity -= quantity

    def is_low_stock(self):
        """
        Check whether the product has reached
        its reorder level.
        """

        return (
            0 < self.quantity <= self.reorder_level
        )

    def is_out_of_stock(self):
        """
        Check whether the product is out of stock.
        """

        return self.quantity == 0

    def calculate_stock_value(self):
        """
        Calculate total value of current stock.
        """

        return self.quantity * self.purchase_price

    def calculate_profit_per_unit(self):
        """
        Calculate profit earned on one unit.
        """

        return self.selling_price - self.purchase_price

    def calculate_potential_profit(self):
        """
        Calculate profit if all current stock is sold.
        """

        return (
            self.calculate_profit_per_unit()
            * self.quantity
        )

    def get_stock_status(self):
        """
        Return the current stock status.
        """

        if self.quantity == 0:
            return "OUT OF STOCK"

        elif self.quantity <= self.reorder_level:
            return "LOW STOCK"

        else:
            return "AVAILABLE"

    # -------------------------------
    # PROPERTY
    # -------------------------------

    @property
    def profit_margin(self):
        """
        Calculate profit margin percentage.
        """

        if self.selling_price == 0:
            return 0

        return (
            (
                self.selling_price
                - self.purchase_price
            )
            / self.selling_price
        ) * 100

    # -------------------------------
    # CLASS METHOD
    # -------------------------------

    @classmethod
    def get_total_products(cls):
        """
        Return total number of Product objects created.
        """

        return cls.total_products

    # -------------------------------
    # STATIC METHOD
    # -------------------------------

    @staticmethod
    def stock_status(quantity, reorder_level):
        """
        Determine stock status without
        creating a Product object.
        """

        if quantity == 0:
            return "OUT OF STOCK"

        elif quantity <= reorder_level:
            return "LOW STOCK"

        return "AVAILABLE"

    # -------------------------------
    # CONVERT OBJECT TO DICTIONARY
    # -------------------------------

    def to_dict(self):
        """
        Convert Product object into a dictionary
        so that it can be stored as JSON.
        """

        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "purchase_price": self.purchase_price,
            "selling_price": self.selling_price,
            "quantity": self.quantity,
            "reorder_level": self.reorder_level,
            "supplier_id": self.supplier_id,
            "created_at": self.created_at
        }

    # -------------------------------
    # CREATE OBJECT FROM DICTIONARY
    # -------------------------------

    @classmethod
    def from_dict(cls, data):
        """
        Create a Product object from dictionary data.
        """

        product = cls(
            data["product_id"],
            data["name"],
            data["category"],
            data["purchase_price"],
            data["selling_price"],
            data["quantity"],
            data["reorder_level"],
            data["supplier_id"]
        )

        product.created_at = data.get(
            "created_at",
            product.created_at
        )

        return product

    # -------------------------------
    # MAGIC METHODS
    # -------------------------------

    def __str__(self):
        """
        Human-readable representation.
        """

        return (
            f"{self.product_id} - "
            f"{self.name} - "
            f"{self.category} - "
            f"Stock: {self.quantity}"
        )

    def __repr__(self):
        """
        Developer-friendly representation.
        """

        return (
            f"Product("
            f"product_id='{self.product_id}', "
            f"name='{self.name}', "
            f"quantity={self.quantity})"
        )

    def __eq__(self, other):
        """
        Compare two products using Product ID.
        """

        if not isinstance(other, Product):
            return False

        return self.product_id == other.product_id