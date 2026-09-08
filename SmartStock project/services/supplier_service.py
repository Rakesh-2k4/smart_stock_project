from models.supplier import Supplier
from utils.file_handler import FileHandler
from utils.validators import Validator
from utils.exceptions import (
    SupplierNotFoundError,
    DuplicateSupplierError
)


class SupplierService:

    def __init__(self, filename="data/suppliers.json"):
        self.filename = filename

    # -----------------------------
    # GET ALL SUPPLIERS
    # -----------------------------
    def get_suppliers(self):
        data = FileHandler.read_json(self.filename)

        return [
            Supplier.from_dict(item)
            for item in data
        ]

    # -----------------------------
    # SAVE SUPPLIERS
    # -----------------------------
    def save_suppliers(self, suppliers):
        data = [
            supplier.to_dict()
            for supplier in suppliers
        ]

        FileHandler.write_json(
            self.filename,
            data
        )

    # -----------------------------
    # ADD SUPPLIER
    # -----------------------------
    def add_supplier(
        self,
        supplier_id,
        name,
        company,
        email,
        phone,
        address
    ):

        suppliers = self.get_suppliers()

        # Check duplicate supplier ID
        for supplier in suppliers:

            if supplier.supplier_id == supplier_id:

                raise DuplicateSupplierError(
                    f"Supplier ID '{supplier_id}' already exists."
                )

        # Validation
        Validator.validate_id(
            supplier_id,
            "Supplier ID"
        )

        Validator.validate_name(name)

        Validator.validate_email(email)

        Validator.validate_phone(phone)

        # Create Supplier object
        supplier = Supplier(
            supplier_id,
            name,
            company,
            email,
            phone,
            address
        )

        # Add to list
        suppliers.append(supplier)

        # Save to JSON
        self.save_suppliers(suppliers)

        return supplier

    # -----------------------------
    # GET ALL SUPPLIERS
    # -----------------------------
    def get_all_suppliers(self):
        return self.get_suppliers()

    # -----------------------------
    # FIND SUPPLIER
    # -----------------------------
    def find_supplier(self, supplier_id):

        suppliers = self.get_suppliers()

        for supplier in suppliers:

            if supplier.supplier_id == supplier_id:
                return supplier

        raise SupplierNotFoundError(
            f"Supplier '{supplier_id}' was not found."
        )

    # -----------------------------
    # SEARCH SUPPLIERS
    # -----------------------------
    def search_suppliers(self, keyword):

        suppliers = self.get_suppliers()

        keyword = keyword.lower()

        results = []

        for supplier in suppliers:

            if (
                keyword in supplier.supplier_id.lower()
                or keyword in supplier.name.lower()
                or keyword in supplier.company.lower()
                or keyword in supplier.email.lower()
            ):

                results.append(supplier)

        return results

    # -----------------------------
    # UPDATE SUPPLIER
    # -----------------------------
    def update_supplier(
        self,
        supplier_id,
        name=None,
        company=None,
        email=None,
        phone=None,
        address=None
    ):

        suppliers = self.get_suppliers()

        supplier = None

        # Find supplier
        for item in suppliers:

            if item.supplier_id == supplier_id:
                supplier = item
                break

        # If not found
        if supplier is None:

            raise SupplierNotFoundError(
                f"Supplier '{supplier_id}' was not found."
            )

        # Update only provided values
        if name:
            Validator.validate_name(name)
            supplier.name = name

        if company:
            supplier.company = company

        if email:
            Validator.validate_email(email)
            supplier.email = email

        if phone:
            Validator.validate_phone(phone)
            supplier.phone = phone

        if address:
            supplier.address = address

        # Save updated data
        self.save_suppliers(suppliers)

        return supplier

    # -----------------------------
    # DELETE SUPPLIER
    # -----------------------------
    def delete_supplier(self, supplier_id):

        suppliers = self.get_suppliers()

        supplier = self.find_supplier(supplier_id)

        suppliers.remove(supplier)

        self.save_suppliers(suppliers)

        return supplier


# from models.supplier import Supplier

# from utils.file_handler import FileHandler

# from utils.validators import Validator

# from utils.exceptions import (
#     SupplierNotFoundError,
#     DuplicateSupplierError
# )


# class SupplierService:
#     """
#     Handles all supplier-related operations.
#     """

#     def __init__(
#         self,
#         filename="data/suppliers.json"
#     ):
#         self.filename = filename

#     # ==========================================
#     # LOAD SUPPLIERS
#     # ==========================================

#     def get_suppliers(self):

#         data = FileHandler.read_json(
#             self.filename
#         )

#         return [
#             Supplier.from_dict(item)
#             for item in data
#         ]

#     # ==========================================
#     # SAVE SUPPLIERS
#     # ==========================================

#     def save_suppliers(self, suppliers):

#         data = [
#             supplier.to_dict()
#             for supplier in suppliers
#         ]

#         FileHandler.write_json(
#             self.filename,
#             data
#         )

#     # ==========================================
#     # ADD SUPPLIER
#     # ==========================================

#     def add_supplier(
#         self,
#         supplier_id,
#         name,
#         company,
#         email,
#         phone,
#         address
#     ):

#         suppliers = self.get_suppliers()

#         # Check duplicate ID
#         for supplier in suppliers:

#             if supplier.supplier_id == supplier_id:

#                 raise DuplicateSupplierError(
#                     f"Supplier ID "
#                     f"'{supplier_id}' already exists."
#                 )

#         # Validate
#         Validator.validate_id(
#             supplier_id,
#             "Supplier ID"
#         )

#         Validator.validate_name(name)

#         Validator.validate_email(email)

#         Validator.validate_phone(phone)

#         # Create object
#         supplier = Supplier(
#             supplier_id,
#             name,
#             company,
#             email,
#             phone,
#             address
#         )

#         suppliers.append(supplier)

#         self.save_suppliers(
#             suppliers
#         )

#         return supplier

#     # ==========================================
#     # VIEW ALL SUPPLIERS
#     # ==========================================

#     def get_all_suppliers(self):

#         return self.get_suppliers()

#     # ==========================================
#     # FIND SUPPLIER
#     # ==========================================

#     def find_supplier(
#         self,
#         supplier_id
#     ):

#         suppliers = self.get_suppliers()

#         for supplier in suppliers:

#             if supplier.supplier_id == supplier_id:

#                 return supplier

#         raise SupplierNotFoundError(
#             f"Supplier "
#             f"'{supplier_id}' was not found."
#         )

#     # ==========================================
#     # SEARCH SUPPLIER
#     # ==========================================

#     def search_suppliers(
#         self,
#         keyword
#     ):

#         suppliers = self.get_suppliers()

#         keyword = keyword.lower()

#         results = []

#         for supplier in suppliers:

#             if (
#                 keyword in supplier.supplier_id.lower()
#                 or keyword in supplier.name.lower()
#                 or keyword in supplier.company.lower()
#                 or keyword in supplier.email.lower()
#             ):

#                 results.append(supplier)

#         return results

#     # ==========================================
#     # DELETE SUPPLIER
#     # ==========================================

#     def delete_supplier(
#         self,
#         supplier_id
#     ):

#         suppliers = self.get_suppliers()

#         supplier = self.find_supplier(
#             supplier_id
#         )

#         suppliers.remove(supplier)

#         self.save_suppliers(
#             suppliers
#         )

#         return supplier