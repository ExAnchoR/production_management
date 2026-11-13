class DeleteStaff:
    def __init__(self, target_id=None):
        try:
            with open("staff.csv", "r") as file:
                lines = file.readlines()

            if not lines:
                print("Staff file is empty.")
                return

            header = lines[0]
            rows = lines[1:]
            found = False
            remaining_rows = []

            for line in rows:
                parts = line.strip().split(",")
                if parts and parts[0] == str(target_id):
                    found = True
                else:
                    remaining_rows.append(line)

            if found:
                with open("staff.csv", "w") as file:
                    file.write(header)
                    file.writelines(remaining_rows)
                print(f"Staff {target_id} deleted successfully!")
            else:
                print(f"Staff ID '{target_id}' not found.")

        except FileNotFoundError:
            print("Error: staff.csv not found.")