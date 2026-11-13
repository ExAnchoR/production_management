class DisplayStaff:
    def __init__(self):
        try:
            with open("staff.csv", "r") as file:
                lines = file.readlines()[1:]

                if not lines:
                    print("\nNo staff records found.")
                    return

                print("\n==================== STAFF MEMBERS ====================")
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) >= 3:
                        print(f"ID: {parts[0]} | Name: {parts[1]} | Role: {parts[2]}")
                print("=======================================================\n")

        except FileNotFoundError:
            print("\nError: staff.csv not found.")