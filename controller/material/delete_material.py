# Controller to remove a raw material from materials.csv by ID
class DeleteMaterial:
    def __init__(self, target_id=None):
        try:
            with open("materials.csv", "r") as file:
                lines = file.readlines()

            if not lines:
                print("Inventory file is empty.")
                return

            header = lines[0]
            rows = lines[1:]
            found = False
            remaining_rows = []

            # Keep all rows except the one matching the target ID
            for line in rows:
                parts = line.strip().split(",")
                if parts and parts[0] == str(target_id):
                    found = True
                else:
                    remaining_rows.append(line)

            # Rewrite the file with the remaining materials
            if found:
                with open("materials.csv", "w") as file:
                    file.write(header)
                    file.writelines(remaining_rows)
                print(f"Material {target_id} deleted successfully!")
            else:
                print(f"Material ID '{target_id}' not found.")

        except FileNotFoundError:
            print("Error: materials.csv not found.")
