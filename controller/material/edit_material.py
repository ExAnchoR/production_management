# Controller to find a raw material by ID and update its details
class EditMaterial:
    def __init__(self, target_id=None, updated_material=None):
        try:
            with open("materials.csv", "r") as file:
                lines = file.readlines()

            if not lines:
                print("Inventory file is empty.")
                return

            header = lines[0]
            rows = lines[1:]
            found = False
            new_rows = []

            # iSearch line by line, then iilis ang matching ID with updated details
            for line in rows:
                parts = line.strip().split(",")
                if parts and parts[0] == str(target_id):
                    new_rows.append(updated_material.to_csv())
                    found = True
                else:
                    new_rows.append(line)

            # Write the updated inventory back to materials.csv
            if found:
                with open("materials.csv", "w") as file:
                    file.write(header)
                    file.writelines(new_rows)
                print(f"Material {target_id} updated successfully!")
            else:
                print(f"Material ID '{target_id}' not found.")

        except FileNotFoundError:
            print("Error: materials.csv not found.")
