# Controller to add new raw material into materials.csv
class AddMaterial:
    def __init__(self, material=None):
        if material is None:
            return

        # icehck niya ang kung naa ba sya, ang material
        try:
            with open("materials.csv", "r") as f:
                next(f, None)  # iskip niya ang header
                for line in f:
                    parts = line.strip().split(",")
                    if parts and parts[0] == str(material.id):
                        print("\n========================================")
                        print("Warning: ID already exists! Please use a different ID. New material not added.")
                        print("========================================\n")
                        return
        except FileNotFoundError:
            # If materials.csv does not exist yet, magreate eh
            with open("materials.csv", "w") as f:
                f.write("id,name,unit,stock_qty,unit_cost\n")

        # Append new material to file
        with open("materials.csv", "a") as f:
            f.write(material.to_csv())
        print("\n========================================")
        print("Material added successfully!")
        print("========================================\n")
