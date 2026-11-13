# Controller to register a new staff member into staff.csv
class AddStaff:
    def __init__(self, staff=None):
        if staff is None:
            return

        # Check if staff.csv exists and if the ID is already taken
        try:
            with open("staff.csv", "r") as f:
                next(f, None)  # Skip the header line
                for line in f:
                    parts = line.strip().split(",")
                    if parts and parts[0] == str(staff.id):
                        print("\n========================================")
                        print("Warning: Staff ID already exists! New staff not added.")
                        print("========================================\n")
                        return
        except FileNotFoundError:
            # If staff.csv doesn't exist yet, then create new
            with open("staff.csv", "w") as f:
                f.write("id,name,role\n")

        # Append the new staff details to the file
        with open("staff.csv", "a") as f:
            f.write(staff.to_csv())
        print("\n========================================")
        print("Staff added successfully!")
        print("========================================\n")
