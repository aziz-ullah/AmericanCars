from app.extensions import db

class Vehicle(db.Model):
    __tablename__ = "vehicle"

    id = db.Column("VehicleID", db.Integer, primary_key=True)
    lot_no = db.Column("LotNo", db.String(50))
    make = db.Column("Make", db.String(100))
    model = db.Column("Model", db.String(100))
    year = db.Column("Year", db.Integer)
    color = db.Column("Color", db.String(50))
    vin = db.Column("VIN", db.String(50))
    current_status = db.Column("CurrentStatus", db.String(50))
    location = db.Column("Location", db.String(100))
    buying_date = db.Column("BuyingDate", db.Date)
    remarks = db.Column("Remarks", db.Text)

    # Relationships
    attachments = db.relationship("Attachment", back_populates="vehicle", lazy="dynamic")
    clearance_details = db.relationship("ClearanceDetails", back_populates="vehicle", uselist=False)
    deposits = db.relationship("DepositDetails", back_populates="vehicle", lazy="dynamic")
    expenses = db.relationship("Expenses", back_populates="vehicle", lazy="dynamic")
    financial_details = db.relationship("FinancialDetails", back_populates="vehicle", lazy="dynamic")
    images = db.relationship("Image", back_populates="vehicle", lazy="dynamic")
    owners = db.relationship("Owner", back_populates="vehicle", lazy="dynamic")
    shipping_details = db.relationship("Shipping", back_populates="vehicle", lazy="dynamic")
