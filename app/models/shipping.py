from app.extensions import db

class Shipping(db.Model):
    __tablename__ = "shipping"
    id = db.Column("ShippingID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    shipping_company = db.Column("ShippingCompany", db.String(100))
    shipping_type = db.Column("ShippingType", db.String(50))
    container_no = db.Column("ContainerNo", db.String(50))
    export_date = db.Column("ExportDate", db.Date)
    state = db.Column("State", db.String(50))
    remarks = db.Column("Remarks", db.Text)
    vehicle = db.relationship("Vehicle", back_populates="shipping_details")
