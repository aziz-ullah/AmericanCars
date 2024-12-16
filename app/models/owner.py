from app.extensions import db


class Owner(db.Model):
    __tablename__ = "owner"
    id = db.Column("OwnerID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    related_to = db.Column("RelatedTo", db.String(100))
    account_type = db.Column("AccountType", db.String(50))
    account_no = db.Column("AccountNo", db.String(50))
    clearance_details = db.Column("ClearanceDetails", db.String(255))
    vehicle = db.relationship("Vehicle", back_populates="owners")
