from services.product_service import ProductService
from services.supplier_service import SupplierService
from services.transaction_service import TransactionService
from services.sale_service import SaleService
from services.report_service import ReportService
from utils.logger import SmartStockLogger

from utils.exceptions import (
    ProductNotFoundError,
    DuplicateProductError,
    SupplierNotFoundError,
    DuplicateSupplierError,
    InsufficientStockError,
    InvalidQuantityError
)


# ==================================================
# SERVICE OBJECTS
# ==================================================

product_service = ProductService()
supplier_service = SupplierService()
transaction_service = TransactionService()
sale_service = SaleService()
report_service = ReportService()
logger = SmartStockLogger.get_logger()
logger.info("SmartStock application started")

# ==================================================
# ADD PRODUCT
# ==================================================

def add_product():

    print("\n========== ADD PRODUCT ==========")

    try:

        product_id = input("Product ID: ").strip()

        # Check duplicate Product ID
        try:

            product_service.find_product(product_id)

            print(
                f"\nError: Product ID '{product_id}' "
                f"already exists."
            )

            return

        except ProductNotFoundError:

            pass

        name = input("Product Name: ").strip()

        category = input("Category: ").strip()

        purchase_price = input("Purchase Price: ").strip()

        selling_price = input("Selling Price: ").strip()

        quantity = input("Quantity: ").strip()

        reorder_level = input("Reorder Level: ").strip()

        supplier_id = input("Supplier ID: ").strip()

        product = product_service.add_product(
            product_id,
            name,
            category,
            purchase_price,
            selling_price,
            quantity,
            reorder_level,
            supplier_id
        )

        print(
            f"\nProduct '{product.name}' "
            f"added successfully!"
        )

    except (
        ValueError,
        DuplicateProductError
    ) as error:

        print(f"\nError: {error}")


# ==================================================
# VIEW PRODUCTS
# ==================================================

def view_products():

    print("\n========== ALL PRODUCTS ==========")

    products = product_service.get_products()

    if not products:

        print("No products found.")

        return

    for product in products:

        print(
            f"""
Product ID      : {product.product_id}
Name            : {product.name}
Category        : {product.category}
Purchase Price  : ₹{product.purchase_price:.2f}
Selling Price   : ₹{product.selling_price:.2f}
Quantity        : {product.quantity}
Reorder Level   : {product.reorder_level}
Supplier ID     : {product.supplier_id}
Stock Status    : {product.get_stock_status()}
Stock Value     : ₹{product.calculate_stock_value():.2f}
Profit / Unit   : ₹{product.calculate_profit_per_unit():.2f}
--------------------------------------------
"""
        )


# ==================================================
# SEARCH PRODUCT
# ==================================================

def search_product():

    keyword = input(
        "\nEnter Product ID, Name or Category: "
    ).strip()

    products = product_service.search_products(
        keyword
    )

    print("\n========== SEARCH RESULTS ==========")

    if not products:

        print("No matching products found.")

        return

    for product in products:

        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name} | "
            f"Category: {product.category} | "
            f"Stock: {product.quantity} | "
            f"Price: ₹{product.selling_price:.2f}"
        )


# ==================================================
# LOW STOCK REPORT
# ==================================================

def low_stock_report():

    products = product_service.get_low_stock_products()

    print(
        "\n========== LOW STOCK PRODUCTS =========="
    )

    if not products:

        print("No low-stock products.")

        return

    for product in products:

        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name} | "
            f"Stock: {product.quantity} | "
            f"Reorder Level: {product.reorder_level}"
        )


# ==================================================
# OUT OF STOCK REPORT
# ==================================================

def out_of_stock_report():

    products = (
        product_service.get_out_of_stock_products()
    )

    print(
        "\n========== OUT OF STOCK PRODUCTS =========="
    )

    if not products:

        print("No out-of-stock products.")

        return

    for product in products:

        print(
            f"ID: {product.product_id} | "
            f"Name: {product.name}"
        )


# ==================================================
# UPDATE PRODUCT
# ==================================================

def update_product():

    print("\n========== UPDATE PRODUCT ==========")

    product_id = input(
        "Enter Product ID: "
    ).strip()

    try:

        product = product_service.find_product(
            product_id
        )

        print(
            f"\nCurrent Product: {product}"
        )

        print(
            "\nPress Enter to keep the current value."
        )

        name = input(
            f"Name [{product.name}]: "
        ).strip()

        category = input(
            f"Category [{product.category}]: "
        ).strip()

        selling_price = input(
            f"Selling Price "
            f"[{product.selling_price}]: "
        ).strip()

        reorder_level = input(
            f"Reorder Level "
            f"[{product.reorder_level}]: "
        ).strip()

        updated_product = product_service.update_product(
            product_id,
            name=name if name else None,
            category=category if category else None,
            selling_price=selling_price
            if selling_price else None,
            reorder_level=reorder_level
            if reorder_level else None
        )

        print(
            "\nProduct updated successfully!"
        )

        print(updated_product)

    except (
        ValueError,
        ProductNotFoundError
    ) as error:

        print(f"\nError: {error}")


# ==================================================
# DELETE PRODUCT
# ==================================================

def delete_product():

    print("\n========== DELETE PRODUCT ==========")

    product_id = input(
        "Enter Product ID: "
    ).strip()

    try:

        product = product_service.delete_product(
            product_id
        )

        print(
            f"\nProduct '{product.name}' "
            f"deleted successfully."
        )

    except ProductNotFoundError as error:

        print(f"\nError: {error}")


# ==================================================
# SORT PRODUCTS
# ==================================================

def sort_products():

    print(
        """
========== SORT PRODUCTS ==========

1. Sort by Selling Price
2. Sort by Selling Price (High to Low)
3. Sort by Stock
4. Sort by Stock (High to Low)
"""
    )

    choice = input("Enter choice: ").strip()

    if choice == "1":

        products = product_service.sort_by_price()

    elif choice == "2":

        products = product_service.sort_by_price(
            descending=True
        )

    elif choice == "3":

        products = product_service.sort_by_stock()

    elif choice == "4":

        products = product_service.sort_by_stock(
            descending=True
        )

    else:

        print("Invalid choice.")

        return

    print("\n========== SORTED PRODUCTS ==========")

    for product in products:

        print(
            f"{product.product_id} | "
            f"{product.name} | "
            f"Stock: {product.quantity} | "
            f"Price: ₹{product.selling_price:.2f}"
        )


# ==================================================
# ADD SUPPLIER
# ==================================================

def add_supplier():

    print("\n========== ADD SUPPLIER ==========")

    try:

        supplier_id = input(
            "Supplier ID: "
        ).strip()

        # Check duplicate Supplier ID
        try:

            supplier_service.find_supplier(
                supplier_id
            )

            print(
                f"\nError: Supplier ID "
                f"'{supplier_id}' already exists."
            )

            return

        except SupplierNotFoundError:

            pass

        name = input(
            "Supplier Name: "
        ).strip()

        company = input(
            "Company Name: "
        ).strip()

        email = input(
            "Email: "
        ).strip()

        phone = input(
            "Phone: "
        ).strip()

        address = input(
            "Address: "
        ).strip()

        supplier = supplier_service.add_supplier(
            supplier_id,
            name,
            company,
            email,
            phone,
            address
        )

        print(
            f"\nSupplier '{supplier.name}' "
            f"added successfully!"
        )

    except (
        ValueError,
        DuplicateSupplierError
    ) as error:

        print(f"\nError: {error}")


# ==================================================
# VIEW SUPPLIERS
# ==================================================

def view_suppliers():

    print("\n========== ALL SUPPLIERS ==========")

    suppliers = supplier_service.get_all_suppliers()

    if not suppliers:

        print("No suppliers found.")

        return

    for supplier in suppliers:

        supplier.display()


# ==================================================
# SEARCH SUPPLIER
# ==================================================

def search_supplier():

    keyword = input(
        "\nEnter Supplier ID, Name or Company: "
    ).strip()

    results = supplier_service.search_suppliers(
        keyword
    )

    print("\n========== SEARCH RESULTS ==========")

    if not results:

        print("No suppliers found.")

        return

    for supplier in results:

        print(
            f"ID: {supplier.supplier_id} | "
            f"Name: {supplier.name} | "
            f"Company: {supplier.company} | "
            f"Email: {supplier.email}"
        )


def update_supplier():

    print("\n========== UPDATE SUPPLIER ==========")

    supplier_id = input("Enter Supplier ID to update: ").strip()

    try:

        # Check supplier exists
        supplier = supplier_service.find_supplier(supplier_id)

        print("\nCurrent Supplier Details:")
        supplier.display()

        print("\nEnter new details.")
        print("Press ENTER to keep the existing value.")

        name = input(
            f"Name [{supplier.name}]: "
        ).strip()

        company = input(
            f"Company [{supplier.company}]: "
        ).strip()

        email = input(
            f"Email [{supplier.email}]: "
        ).strip()

        phone = input(
            f"Phone [{supplier.phone}]: "
        ).strip()

        address = input(
            f"Address [{supplier.address}]: "
        ).strip()

        # Convert empty values to None
        name = name if name else None
        company = company if company else None
        email = email if email else None
        phone = phone if phone else None
        address = address if address else None

        updated_supplier = supplier_service.update_supplier(
            supplier_id,
            name,
            company,
            email,
            phone,
            address
        )

        print("\nSupplier updated successfully!")

        updated_supplier.display()

    except SupplierNotFoundError as e:

        print(f"\nError: {e}")

    except ValueError as e:

        print(f"\nError: {e}")

# ==================================================
# DELETE SUPPLIER
# ==================================================

def delete_supplier():

    print("\n========== DELETE SUPPLIER ==========")

    supplier_id = input(
        "Enter Supplier ID: "
    ).strip()

    try:

        supplier = supplier_service.delete_supplier(
            supplier_id
        )

        print(
            f"\nSupplier '{supplier.name}' "
            f"deleted successfully."
        )

    except SupplierNotFoundError as error:

        print(f"\nError: {error}")



def products_by_supplier():

    print("\n========== PRODUCTS BY SUPPLIER ==========")

    supplier_id = input("Enter Supplier ID: ").strip()

    try:

        # First check whether supplier exists
        supplier = supplier_service.find_supplier(supplier_id)

        # Find products belonging to supplier
        products = product_service.get_products_by_supplier(
            supplier_id
        )

        print("\nSupplier Details:")
        print(f"Supplier ID : {supplier.supplier_id}")
        print(f"Supplier    : {supplier.name}")
        print(f"Company     : {supplier.company}")

        print("\nProducts Supplied:")

        if not products:
            print("No products found for this supplier.")
            return

        total_quantity = 0

        for product in products:

            print("\n---------------------------------------------")
            print(f"Product ID : {product.product_id}")
            print(f"Name       : {product.name}")
            print(f"Category   : {product.category}")
            print(f"Quantity   : {product.quantity}")
            print(f"Selling Price : ₹{product.selling_price:.2f}")

            total_quantity += product.quantity

        print("\n---------------------------------------------")
        print(f"Total Products : {len(products)}")
        print(f"Total Quantity : {total_quantity}")

    except SupplierNotFoundError as e:

        print(f"\nError: {e}")



def stock_in():

    print("\n========== STOCK IN ==========")

    product_id = input("Enter Product ID: ").strip()

    try:

        product = product_service.find_product(product_id)

        print(f"\nProduct Name     : {product.name}")
        print(f"Current Quantity : {product.quantity}")

        quantity = int(
            input("Enter quantity received: ")
        )

        previous_quantity = product.quantity

        updated_product = product_service.stock_in(
            product_id,
            quantity
        )

        transaction_service.add_transaction(
            product_id,
            "STOCK IN",
            quantity,
            previous_quantity,
            updated_product.quantity
        )

        print("\nStock added successfully!")

        print(f"Product ID       : {updated_product.product_id}")
        print(f"Product Name     : {updated_product.name}")
        print(f"Previous Stock   : {previous_quantity}")
        print(f"Added Quantity   : {quantity}")
        print(f"New Stock        : {updated_product.quantity}")

    except ProductNotFoundError as e:

        print(f"\nError: {e}")

    except (ValueError, InvalidQuantityError) as e:

        print(f"\nError: {e}")


def stock_out():

    print("\n========== STOCK OUT ==========")

    product_id = input("Enter Product ID: ").strip()

    try:

        product = product_service.find_product(product_id)

        print(f"\nProduct Name     : {product.name}")
        print(f"Current Quantity : {product.quantity}")

        quantity = int(
            input("Enter quantity sold: ")
        )

        previous_quantity = product.quantity

        updated_product = product_service.stock_out(
            product_id,
            quantity
        )

        transaction_service.add_transaction(
            product_id,
            "STOCK OUT",
            quantity,
            previous_quantity,
            updated_product.quantity
        )

        print("\nStock removed successfully!")

        print(f"Product ID       : {updated_product.product_id}")
        print(f"Product Name     : {updated_product.name}")
        print(f"Previous Stock   : {previous_quantity}")
        print(f"Removed Quantity : {quantity}")
        print(f"New Stock        : {updated_product.quantity}")

    except ProductNotFoundError as e:

        print(f"\nError: {e}")

    except InsufficientStockError as e:

        print(f"\nError: {e}")

    except (ValueError, InvalidQuantityError) as e:

        print(f"\nError: {e}")


def transaction_history():

    print("\n========== TRANSACTION HISTORY ==========")

    transactions = transaction_service.get_all_transactions()

    if not transactions:

        print("\nNo transactions found.")

        return

    for transaction in transactions:

        transaction.display()

    print("\n--------------------------------------------")
    print(f"Total Transactions : {len(transactions)}")



def record_sale():

    print("\n========== RECORD SALE ==========")

    product_id = input("Enter Product ID: ").strip()

    try:

        # Find product
        product = product_service.find_product(product_id)

        print(f"\nProduct Name     : {product.name}")
        print(f"Selling Price    : ₹{product.selling_price:.2f}")
        print(f"Current Stock    : {product.quantity}")

        quantity = int(
            input("Enter quantity sold: ")
        )

        # Store previous stock
        previous_quantity = product.quantity

        # Remove stock
        updated_product = product_service.stock_out(
            product_id,
            quantity
        )

        # Create sale record
        sale = sale_service.add_sale(
            updated_product,
            quantity
        )


        logger.info(
            f"Sale recorded: {sale.sale_id} | "
            f"Product: {sale.product_id} | "
            f"Quantity: {quantity} | "
            f"Amount: ₹{sale.total_amount:.2f}"
        )

        # Create transaction record
        transaction_service.add_transaction(
            product_id,
            "STOCK OUT",
            quantity,
            previous_quantity,
            updated_product.quantity
        )

        print("\nSale recorded successfully!")

        print(f"Sale ID          : {sale.sale_id}")
        print(f"Product ID       : {sale.product_id}")
        print(f"Product Name     : {sale.product_name}")
        print(f"Quantity Sold    : {sale.quantity}")
        print(f"Selling Price    : ₹{sale.selling_price:.2f}")
        print(f"Total Amount     : ₹{sale.total_amount:.2f}")
        print(f"Profit           : ₹{sale.profit:.2f}")
        print(f"Previous Stock   : {previous_quantity}")
        print(f"Remaining Stock  : {updated_product.quantity}")
        print(f"Date & Time      : {sale.date_time}")

    except ProductNotFoundError as e:

        print(f"\nError: {e}")

    except InsufficientStockError as e:

        print(f"\nError: {e}")

    except (ValueError, InvalidQuantityError) as e:

        print(f"\nError: {e}")


def view_sales():

    print("\n========== ALL SALES ==========")

    sales = sale_service.get_all_sales()

    if not sales:

        print("\nNo sales found.")

        return

    for sale in sales:

        sale.display()

    print("\n--------------------------------------------")

    print(
        f"Total Sales Amount : ₹"
        f"{sale_service.get_total_sales():.2f}"
    )

    print(
        f"Total Profit       : ₹"
        f"{sale_service.get_total_profit():.2f}"
    )

    print(
        f"Total Transactions : {len(sales)}"
    )


def business_report():

    report_service.complete_report()


# ==================================================
# MAIN MENU
# ==================================================

def main():

    while True:

        print(
            """
============================================
              SMARTSTOCK SYSTEM
============================================

1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Low Stock Report
7. Out of Stock Report
8. Sort Products
9. Add Supplier
10. View All Suppliers
11. Search Supplier
12. Delete Supplier
13. Update supplier
14. View Products by Supplier
15. Stock In
16. Stock Out
17. Transaction History
18. Record Sale
19. View Sales
20. Business Report
21. Exit

============================================
"""
        )

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_product()

        elif choice == "2":

            view_products()

        elif choice == "3":

            search_product()

        elif choice == "4":

            update_product()

        elif choice == "5":

            delete_product()

        elif choice == "6":

            low_stock_report()

        elif choice == "7":

            out_of_stock_report()

        elif choice == "8":

            sort_products()

        elif choice == "9":

            add_supplier()

        elif choice == "10":

            view_suppliers()

        elif choice == "11":

            search_supplier()

        elif choice == "12":

            delete_supplier()

        elif choice == "13":
             
            update_supplier()

        elif choice == "14":

            products_by_supplier()

        elif choice == "15":

            stock_in()

        elif choice == "16":

            stock_out()

        elif choice == "17":

            transaction_history()

        elif choice == "18":

            record_sale()

        elif choice == "19":

            view_sales()

        elif choice == "20":

            business_report()

        elif choice == "21":

            print(
                "\nThank you for using SmartStock!"
            )

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


# ==================================================
# PROGRAM START
# ==================================================

if __name__ == "__main__":

    main()