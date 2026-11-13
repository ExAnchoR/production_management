from model.staff import Staff
from model.raw_material import RawMaterial
from model.product import Product

# Material Controllers
from controller.material.add_material import AddMaterial
from controller.material.display_material import DisplayMaterial
from controller.material.edit_material import EditMaterial
from controller.material.delete_material import DeleteMaterial

# Staff Controller
from controller.staff.add_staff import AddStaff

# Production Controllers
from controller.production.run_production import RunProduction
from controller.production.display_product import DisplayProduct
from controller.production.display_history import DisplayHistory


# Menu class
class Menu:
    def __init__(self):
        self.staff = Staff()
        self.material = RawMaterial()

    # AUTHENTICATIONNNN
    # Register a new staff member and save into staff.csv
    def register_staff(self):
        print("\n--- Register Staff ---")
        stf = Staff()
        stf.id = input("Input New Staff ID: ").strip()
        stf.name = input("Input Staff Name: ").strip()
        stf.role = input("Input Staff Role (e.g. Supervisor/Operator): ").strip()

        if not stf.id or not stf.name:
            print("Staff ID and Name cannot be empty.")
            return False

        AddStaff(stf)
        return True

    # Login existing staff by matching ID in staff.csv
    def login_staff(self):
        print("\n--- Staff Login ---")
        input_id = input("Enter Staff ID: ").strip()

        try:
            with open("staff.csv", "r") as f:
                next(f, None)  # Skip header row
                for line in f:
                    parts = line.strip().split(",")
                    # If ID matches, store current staff in session
                    if parts and parts[0] == input_id:
                        self.staff.id = parts[0]
                        self.staff.name = parts[1]
                        self.staff.role = parts[2] if len(parts) > 2 else "Staff"
                        print(f"\nLogin successful! Welcome, {self.staff.name} ({self.staff.role})")
                        return True
        except FileNotFoundError:
            print("No staff records found. Please register first.")
            return False

        print("Invalid Staff ID. Record not found.")
        return False

    # Screen to choose Register, Login, or Exit for authentikation
    def show_Staff_Auth(self):
        while True:
            print("\n===================================")
            print("       STAFF AUTHENTICATION")
            print("===================================")
            print("1. Register Staff")
            print("2. Login Staff")
            print("3. Exit")

            auth_choice = input("Select an option (1-3): ").strip()

            if auth_choice == "1":
                self.register_staff()
            elif auth_choice == "2":
                if self.login_staff():
                    return True
            elif auth_choice == "3":
                print("Exiting application.")
                return False
            else:
                print("Invalid choice, please select between 1 and 3.")

    # OPERATION FOR RAW MATERIAL
    # Asks user for new material details and call AddMaterial controller
    def add_Material(self):
        print("\n--- Add Raw Material ---")
        mat = RawMaterial()
        mat.id = input("Input Material ID: ").strip()
        mat.name = input("Input Material Name: ").strip()
        mat.unit = input("Input Unit (pcs/kg/meters/liters): ").strip()
        mat.stock_qty = float(input("Input Initial Stock Qty: ") or 0)
        mat.unit_cost = float(input("Input Unit Cost (PHP): ") or 0)
        AddMaterial(mat)

    # Call DisplayMaterial controller to show all raw materials
    def display_Material(self):
        DisplayMaterial()

    # Asks user for target ID and updated values, then call EditMaterial controller
    def edit_Material(self):
        print("\n--- Edit Raw Material ---")
        target_id = input("Enter Material ID to edit: ").strip()
        print("Provide updated details:")
        mat = RawMaterial()
        mat.id = target_id
        mat.name = input("Input New Material Name: ").strip()
        mat.unit = input("Input New Unit: ").strip()
        mat.stock_qty = float(input("Input New Stock Qty: ") or 0)
        mat.unit_cost = float(input("Input New Unit Cost (PHP): ") or 0)
        EditMaterial(target_id, mat)

    # Asks user for target ID, ask for confirmation, and call DeleteMaterial controller
    def delete_Material(self):
        print("\n--- Delete Raw Material ---")
        target_id = input("Enter Material ID to delete: ").strip()
        confirm = input(f"Are you sure you want to delete [{target_id}]? (y/n): ").strip().lower()
        if confirm == 'y':
            DeleteMaterial(target_id)
        else:
            print("Deletion cancelled.")

    # PRODUCTION OPERATIONS
    # Collect product info and recipe requirements, then run the production batch
    def run_production_order(self):
        print("\n--- Execute Production Batch ---")
        DisplayMaterial()  # Show available materials for reference

        prod_id = input("Enter Finished Product ID (e.g. P101): ").strip()
        prod_name = input("Enter Product Name (e.g. Dining Chair): ").strip()
        qty = int(input("Enter Units to Produce: ") or 1)
        unit_price = float(input("Target Selling Price per Finished Product (PHP): ") or 0)

        # Loop to collect which raw materials and how much are needed per product unit
        requirements = {}
        print("\n--- Define Required Raw Materials ---")
        print("(Enter materials one by one. Type 'done' when finished)")

        while True:
            mat_id = input("Input Material ID (or 'done' to build): ").strip()
            if mat_id.lower() == 'done':
                break

            if not mat_id:
                continue

            try:
                per_unit = float(input(f"Quantity needed per 1 unit of '{prod_name}': ").strip())
                if per_unit <= 0:
                    print("Quantity must be greater than 0.")
                    continue
                requirements[mat_id] = per_unit
                print(f"Added Material [{mat_id}] -> {per_unit} per product unit.\n")
            except ValueError:
                print("Invalid number. Please try again.")

        if not requirements:
            print("No materials specified. Production cancelled.")
            return

        # Executes the production run
        RunProduction(self.staff, prod_id, prod_name, qty, requirements, unit_price)

    # Call DisplayProduct controller to show finished goods stuffs
    def display_finished_goods(self):
        DisplayProduct()

    # Call DisplayHistory controller to show batch logs or hustiry
    def display_production_history(self):
        DisplayHistory()

    #  MAIN DASHBOARD
    # Main menu showed to the logged-in staff member
    def show_menu(self):
        while True:
            print("\n===================================")
            print("    PRODUCTION MANAGEMENT SYSTEM")
            print(f"    Operator: {self.staff.name} [{self.staff.role}]")
            print("===================================")
            print("--- Raw Materials Warehouse ---")
            print("1. Add Raw Material")
            print("2. Display Raw Materials")
            print("3. Edit Raw Material")
            print("4. Delete Raw Material")
            print("--- Manufacturing Line ---")
            print("5. Run Production Order (Deduct Materials & Build)")
            print("6. View Finished Goods Catalog")
            print("7. View Production History Log")
            print("-----------------------------------")
            print("8. Logout")

            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                self.add_Material()
            elif choice == "2":
                self.display_Material()
            elif choice == "3":
                self.edit_Material()
            elif choice == "4":
                self.delete_Material()
            elif choice == "5":
                self.run_production_order()
            elif choice == "6":
                self.display_finished_goods()
            elif choice == "7":
                self.display_production_history()
            elif choice == "8":
                print(f"Operator {self.staff.name} logged out.")
                break
            else:
                print("Invalid choice, please select between 1 and 8.")