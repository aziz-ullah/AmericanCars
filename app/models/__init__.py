# Models imports
from .vehicle import Vehicle
from .attachment import Attachment
from .clearance_details import ClearanceDetails
from .deposit_details import DepositDetails
from .expenses import Expenses
from .financial_details import FinancialDetails
from .image import Image
from .owner import Owner
from .shipping import Shipping

# Optionally, export all models for easy access
__all__ = [
    "Vehicle",
    "Attachment",
    "ClearanceDetails",
    "DepositDetails",
    "Expenses",
    "FinancialDetails",
    "Image",
    "Owner",
    "Shipping",
]
