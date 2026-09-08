import re


class Validator:
    """
    Provides validation methods for SmartStock.
    """

    # ==========================================
    # VALIDATE NAME
    # ==========================================

    @staticmethod
    def validate_name(name):
        """
        Validate a person's or product's name.
        """

        if not name or not name.strip():
            raise ValueError(
                "Name cannot be empty."
            )

        if not re.match(
            r"^[A-Za-z ]+$",
            name
        ):
            raise ValueError(
                "Name should contain only "
                "letters and spaces."
            )

        return True

    # ==========================================
    # VALIDATE POSITIVE NUMBER
    # ==========================================

    @staticmethod
    def validate_positive_number(
        value,
        field_name
    ):
        """
        Validate that a value is a positive number.
        """

        try:

            value = float(value)

        except (ValueError, TypeError):

            raise ValueError(
                f"{field_name} must be a number."
            )

        if value <= 0:

            raise ValueError(
                f"{field_name} must be greater "
                f"than zero."
            )

        return value

    # ==========================================
    # VALIDATE QUANTITY
    # ==========================================

    @staticmethod
    def validate_quantity(value):
        """
        Validate that quantity is a positive integer.
        """

        try:

            value = int(value)

        except (ValueError, TypeError):

            raise ValueError(
                "Quantity must be an integer."
            )

        if value <= 0:

            raise ValueError(
                "Quantity must be greater than zero."
            )

        return value

    # ==========================================
    # VALIDATE EMAIL
    # ==========================================

    @staticmethod
    def validate_email(email):
        """
        Validate an email address.
        """

        pattern = (
            r"^[\w\.-]+@[\w\.-]+\.\w+$"
        )

        if not re.match(pattern, email):

            raise ValueError(
                "Invalid email address."
            )

        return True

    # ==========================================
    # VALIDATE PHONE
    # ==========================================

    @staticmethod
    def validate_phone(phone):
        """
        Validate a 10-digit phone number.
        """

        phone = str(phone)

        if (
            not phone.isdigit()
            or len(phone) != 10
        ):

            raise ValueError(
                "Phone number must contain "
                "exactly 10 digits."
            )

        return True

    # ==========================================
    # VALIDATE ID
    # ==========================================

    @staticmethod
    def validate_id(
        value,
        field_name
    ):
        """
        Validate that an ID is not empty.
        """

        if not value or not value.strip():

            raise ValueError(
                f"{field_name} cannot be empty."
            )

        return True