class Supplier:
    """
    Represents a supplier in the SmartStock system.
    """

    def __init__(
        self,
        supplier_id,
        name,
        company,
        email,
        phone,
        address
    ):
        self.supplier_id = supplier_id
        self.name = name
        self.company = company
        self.email = email
        self.phone = phone
        self.address = address

    def to_dict(self):
        """
        Convert Supplier object into dictionary.
        """

        return {
            "supplier_id": self.supplier_id,
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "phone": self.phone,
            "address": self.address
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create Supplier object from dictionary.
        """

        return cls(
            data["supplier_id"],
            data["name"],
            data["company"],
            data["email"],
            data["phone"],
            data["address"]
        )

    def display(self):
        """
        Display supplier information.
        """

        print(
            f"\nSupplier ID : {self.supplier_id}"
        )

        print(
            f"Name        : {self.name}"
        )

        print(
            f"Company     : {self.company}"
        )

        print(
            f"Email       : {self.email}"
        )

        print(
            f"Phone       : {self.phone}"
        )

        print(
            f"Address     : {self.address}"
        )

        print("-" * 45)

    def __str__(self):
        return (
            f"{self.supplier_id} - "
            f"{self.name} - "
            f"{self.company}"
        )