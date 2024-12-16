from app.extensions import db

class FinancialDetails(db.Model):
    __tablename__ = "financialdetails"

    id = db.Column("FinancialID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    bid_amount = db.Column("BidAmount", db.Numeric(10, 2))
    invoice_amount = db.Column("InvoiceAmount", db.Numeric(10, 2))
    invoice = db.Column("Invoice", db.String(100))
    storage_fee = db.Column("StorageFee", db.Numeric(10, 2))
    title_fee = db.Column("TitleFee", db.Numeric(10, 2))
    shipping = db.Column("Shipping", db.Numeric(10, 2))

    # Relationship back to Vehicle
    vehicle = db.relationship("Vehicle", back_populates="financial_details")
