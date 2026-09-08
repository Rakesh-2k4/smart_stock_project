class SmartStockException(Exception):
    """
    Base exception class for SmartStock.
    All custom SmartStock exceptions will inherit from this class.
    """
    pass


class ProductNotFoundError(SmartStockException):
    """
    Raised when a requested product does not exist.
    """
    pass


class DuplicateProductError(SmartStockException):
    """
    Raised when a product with the same ID already exists.
    """
    pass


class InsufficientStockError(SmartStockException):
    """
    Raised when there is not enough stock for a sale.
    """
    pass


class InvalidQuantityError(SmartStockException):
    """
    Raised when an invalid quantity is entered.
    """
    pass


class SupplierNotFoundError(SmartStockException):
    """
    Raised when a requested supplier does not exist.
    """
    pass


class DuplicateSupplierError(SmartStockException):
    """
    Raised when a supplier with the same ID already exists.
    """
    pass