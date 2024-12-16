from app.extensions import db

class Attachment(db.Model):
    __tablename__ = "attachments"

    id = db.Column("AttachmentID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    description = db.Column("Description", db.Text)
    file_type = db.Column("FileType", db.String(50))
    attachment_path = db.Column("AttachmentPath", db.String(255))
    relationship = db.Column("Relationship", db.String(100))

    # Back reference
    vehicle = db.relationship("Vehicle", back_populates="attachments")
