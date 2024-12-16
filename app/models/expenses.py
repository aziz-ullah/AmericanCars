from app.extensions import db


class Expenses(db.Model):
    __tablename__ = "expenses"
    id = db.Column("ExpensesID", db.Integer, primary_key=True)
    vehicle_id = db.Column("VehicleID", db.Integer, db.ForeignKey("vehicle.VehicleID"))
    repairing_exp = db.Column("RepairingEXP", db.Numeric(10, 2))
    other_expenses = db.Column("OtherExpenses", db.Numeric(10, 2))
    showroom_fee = db.Column("ShowroomFee", db.Numeric(10, 2))
    expense_date = db.Column("ExpenseDate", db.Date)
    vehicle = db.relationship("Vehicle", back_populates="expenses")
