# Controller to read and display all raw materials from materials.csv
class DisplayMaterial:
    def __init__(self):
        try:
            with open("materials.csv", "r") as file:
                lines = file.readlines()[1:]

                if not lines:
                    print("\nNo materials found in inventory.")
                    return

                # Print formatted table of raw materials
                print("\n==================== RAW MATERIALS ====================")
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) >= 5:
                        print(f"ID: {parts[0]} | Name: {parts[1]} | Qty: {parts[3]} {parts[2]} | Cost: PHP {parts[4]}")
                print("=======================================================\n")

        except FileNotFoundError:
            print("\nError: materials.csv not found.")
