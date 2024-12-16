from app.extensions import db

class Image(db.Model):
    __tablename__ = "image"
    id = db.Column("ImageID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    image_path = db.Column("ImagePath", db.String(255))
    vehicle = db.relationship("Vehicle", back_populates="images")
