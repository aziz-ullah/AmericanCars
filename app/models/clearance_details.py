from app.extensions import db

class ClearanceDetails(db.Model):
    __tablename__ = "clearancedetails"

    id = db.Column("ClearanceID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    declaration_no = db.Column("DeclarationNo", db.String(100))
    declaration_date = db.Column("DeclarationDate", db.Date)
    invoice_no = db.Column("InvoiceNo", db.String(100))
    clearance_company = db.Column("ClearanceCompany", db.String(100))
    attestation_fee = db.Column("AttestationFee", db.Numeric(10, 2))
    inspection_fee = db.Column("InspectionFee", db.Numeric(10, 2))
    customs_fee = db.Column("CustomsFee", db.Numeric(10, 2))
    vat = db.Column("VAT", db.Numeric(10, 2))
    clearance_fee = db.Column("ClearanceFee", db.Numeric(10, 2))

    # Back reference
    vehicle = db.relationship("Vehicle", back_populates="clearance_details")
