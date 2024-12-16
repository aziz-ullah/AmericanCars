from app.extensions import db

class DepositDetails(db.Model):
    __tablename__ = "depositdetails"

    id = db.Column("DepositID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    amount_received = db.Column("AmountReceived", db.Numeric(10, 2))
    currency = db.Column("Currency", db.String(50))
    deposit_status = db.Column("DepositStatus", db.String(50))
    expire_date = db.Column("ExpireDate", db.Date)

    # Back reference
    vehicle = db.relationship("Vehicle", back_populates="deposits")
