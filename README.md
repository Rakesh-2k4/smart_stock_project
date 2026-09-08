# SmartStock - Inventory Management System

## 📌 About the Project

SmartStock is a Python-based Inventory Management System designed to help small businesses manage their products, suppliers, inventory, stock transactions, sales, and business reports efficiently.

The project is developed using **pure Python** with JSON files for data storage. It demonstrates important Python programming concepts such as **Object-Oriented Programming, functions, file handling, JSON, validation, exception handling, custom exceptions, and logging**.

The application is completely command-line based and does not require an SQL database or graphical user interface.

---

## 🎯 Problem Statement

Managing inventory manually can make it difficult to keep track of available stock, suppliers, sales, and transactions. It can also lead to incorrect stock calculations and difficulty identifying products that need restocking.

SmartStock provides a simple solution by bringing these inventory operations together in one Python application.

---

## 💡 Objectives

- Manage product information efficiently
- Maintain supplier details
- Track available inventory
- Perform stock-in and stock-out operations
- Maintain transaction history
- Record product sales
- Calculate revenue and profit
- Identify low-stock and out-of-stock products
- Generate business reports
- Store data using JSON files
- Demonstrate practical Python programming concepts

---

## 🚀 Features

### Product Management
- Add Product
- View All Products
- Search Product
- Update Product
- Delete Product
- Sort Products

### Supplier Management
- Add Supplier
- View All Suppliers
- Search Supplier
- Update Supplier
- Delete Supplier
- View Products by Supplier

### Inventory Management
- Stock In
- Stock Out
- Stock availability checking
- Low Stock Report
- Out of Stock Report

### Transaction Management
- Record stock transactions
- View transaction history
- Track previous and new stock quantities
- Store transaction date and time

### Sales Management
- Record sales
- View sales history
- Calculate total sales amount
- Calculate profit
- Automatically update product stock

### Business Reporting
- Total number of products
- Total stock quantity
- Total stock value
- Low-stock product count
- Out-of-stock product count
- Total items sold
- Total sales records
- Total revenue
- Total profit

### Validation and Error Handling
- Input validation
- Duplicate product checking
- Duplicate supplier checking
- Product not found handling
- Supplier not found handling
- Insufficient stock handling
- Invalid quantity handling
- Custom exceptions

### Logging
The application uses Python's built-in `logging` module to record important events such as application startup and sales transactions.

Logs are stored in:

```text
data/smartstock.log
