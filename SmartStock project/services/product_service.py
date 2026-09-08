import os

from models.product import Product

from utils.file_handler import FileHandler
from utils.validators import Validator

from utils.exceptions import (
    ProductNotFoundError,
    DuplicateProductError,
    InsufficientStockError,
    InvalidQuantityError
)


class ProductService:
    """
    Handles all product-related business operations.
    """

    def __init__(self):
        """
        Initialize ProductService.
        """

        self.filename = os.path.join(
            "data",
            "products.json"
        )

    # ==================================================
    # GET ALL PRODUCTS
    # ==================================================

    def get_products(self):
        """
        Read products from JSON and convert
        them into Product objects.
        """

        data = FileHandler.read_json(
            self.filename
        )

        products = [
            Product.from_dict(item)
            for item in data
        ]

        return products

    # ==================================================
    # SAVE PRODUCTS
    # ==================================================

    def save_products(self, products):
        """
        Convert Product objects to dictionaries
        and save them to JSON.
        """

        data = [
            product.to_dict()
            for product in products
        ]

        FileHandler.write_json(
            self.filename,
            data
        )

    # ==================================================
    # ADD PRODUCT
    # ==================================================

    def add_product(
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
        Add a new product to the inventory.
        """

        products = self.get_products()

        # Check duplicate Product ID
        for product in products:

            if product.product_id == product_id:

                raise DuplicateProductError(
                    f"Product ID '{product_id}' "
                    f"already exists."
                )

        # Validate product name
        Validator.validate_name(name)

        # Validate prices
        purchase_price = (
            Validator.validate_positive_number(
                purchase_price,
                "Purchase price"
            )
        )

        selling_price = (
            Validator.validate_positive_number(
                selling_price,
                "Selling price"
            )
        )

        # Validate quantities
        quantity = Validator.validate_quantity(
            quantity
        )

        reorder_level = Validator.validate_quantity(
            reorder_level
        )

        # Selling price should not be lower
        # than purchase price

        if selling_price < purchase_price:

            raise ValueError(
                "Selling price cannot be lower "
                "than purchase price."
            )

        # Create Product object

        product = Product(
            product_id,
            name,
            category,
            purchase_price,
            selling_price,
            quantity,
            reorder_level,
            supplier_id
        )

        # Add product to list

        products.append(product)

        # Save updated list

        self.save_products(products)

        return product

    # ==================================================
    # FIND PRODUCT
    # ==================================================

    def find_product(self, product_id):
        """
        Find a product using Product ID.
        """

        products = self.get_products()

        for product in products:

            if product.product_id == product_id:

                return product

        raise ProductNotFoundError(
            f"Product '{product_id}' "
            f"not found."
        )


    def update_product(
        self,
        product_id,
        name=None,
        category=None,
        selling_price=None,
        reorder_level=None
    ):
        
        """
        Update product information and save
        the changes permanently to JSON.
        """

        products = self.get_products()

        # Find product
        product = None

        for item in products:

            if item.product_id == product_id:
                product = item
                break

        # Product does not exist
        if product is None:

            raise ProductNotFoundError(
                f"Product '{product_id}' not found."
            )

        # -----------------------------
        # UPDATE NAME
        # -----------------------------

        if name is not None and name.strip() != "":

            Validator.validate_name(name)

            product.name = name

        # -----------------------------
        # UPDATE CATEGORY
        # -----------------------------

        if category is not None and category.strip() != "":

            product.category = category

        # -----------------------------
        # UPDATE SELLING PRICE
        # -----------------------------

        if selling_price is not None and str(
            selling_price
        ).strip() != "":

            selling_price = (
                Validator.validate_positive_number(
                    selling_price,
                    "Selling price"
                )
            )

            if selling_price < product.purchase_price:

                raise ValueError(
                    "Selling price cannot be lower "
                    "than purchase price."
                )

            product.selling_price = selling_price

        # -----------------------------
        # UPDATE REORDER LEVEL
        # -----------------------------

        if reorder_level is not None and str(
            reorder_level
        ).strip() != "":

            reorder_level = (
                Validator.validate_quantity(
                    reorder_level
                )
            )

            product.reorder_level = reorder_level

        # -----------------------------
        # SAVE CHANGES
        # -----------------------------

        self.save_products(products)

        return product

        

    # ==================================================
    # DELETE PRODUCT
    # ==================================================

    def delete_product(self, product_id):
        """
        Delete a product from inventory.
        """

        products = self.get_products()

        product = None

        for item in products:

            if item.product_id == product_id:

                product = item
                break

        if product is None:

            raise ProductNotFoundError(
                f"Product '{product_id}' "
                f"not found."
            )

        products.remove(product)

        self.save_products(products)

        return product

    # ==================================================
    # SEARCH PRODUCTS
    # ==================================================

    def search_products(self, keyword):
        """
        Search products by ID, name or category.
        """

        products = self.get_products()

        keyword = keyword.lower()

        results = [
            product
            for product in products
            if keyword in product.product_id.lower()
            or keyword in product.name.lower()
            or keyword in product.category.lower()
        ]

        return results


        # -----------------------------
    # GET PRODUCTS BY SUPPLIER
    # -----------------------------
    def get_products_by_supplier(self, supplier_id):

        products = self.get_products()

        results = []

        for product in products:

            if product.supplier_id == supplier_id:
                results.append(product)

        return results

    # ==================================================
    # LOW STOCK PRODUCTS
    # ==================================================

    def get_low_stock_products(self):
        """
        Return products that need reordering.
        """

        products = self.get_products()

        return [
            product
            for product in products
            if product.is_low_stock()
        ]

    # ==================================================
    # OUT OF STOCK PRODUCTS
    # ==================================================

    def get_out_of_stock_products(self):
        """
        Return products with zero stock.
        """

        products = self.get_products()

        return [
            product
            for product in products
            if product.is_out_of_stock()
        ]

    # ==================================================
    # SORT PRODUCTS BY PRICE
    # ==================================================

    def sort_by_price(self, descending=False):
        """
        Sort products according to selling price.
        """

        products = self.get_products()

        return sorted(
            products,
            key=lambda product: product.selling_price,
            reverse=descending
        )

    # ==================================================
    # SORT PRODUCTS BY STOCK
    # ==================================================

    def sort_by_stock(self, descending=False):
        """
        Sort products according to quantity.
        """

        products = self.get_products()

        return sorted(
            products,
            key=lambda product: product.quantity,
            reverse=descending
        )



        # -----------------------------
    # STOCK IN
    # -----------------------------
    def stock_in(self, product_id, quantity):

        products = self.get_products()

        # Find product
        product = None

        for item in products:
            if item.product_id == product_id:
                product = item
                break

        # Product not found
        if product is None:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )

        # Validate quantity
        Validator.validate_quantity(quantity)

        # Add stock
        product.quantity += quantity

        # Save updated product
        self.save_products(products)

        return product


        # -----------------------------
    # STOCK OUT
    # -----------------------------
    def stock_out(self, product_id, quantity):

        products = self.get_products()

        # Find product
        product = None

        for item in products:
            if item.product_id == product_id:
                product = item
                break

        # Product not found
        if product is None:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )

        # Validate quantity
        Validator.validate_quantity(quantity)

        # Check sufficient stock
        if quantity > product.quantity:
            raise InsufficientStockError(
                f"Insufficient stock. Available stock: {product.quantity}"
            )

        # Remove stock
        product.quantity -= quantity

        # Save updated product
        self.save_products(products)

        return product