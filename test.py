from app import create_app, db
from app.models import Vehicle

app = create_app()

with app.app_context():
    # Create a new vehicle
    vehicle = Vehicle(
        lot_no="12345",
        make="Ford",
        model="Mustang",
        year=2023,
        color="Red",
        vin="1FA6P8TH1L5100000",
        current_status="Available",
        location="New York",
        buying_date="2023-12-01",
        remarks="Test vehicle"
    )
    db.session.add(vehicle)
    db.session.commit()
    print("Vehicle added:", vehicle)
