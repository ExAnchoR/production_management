import time

# 1. Checks all raw materials are in stock
# 2. Deducts required raw materials from materials.csv
# 3. Adds/updates the finished product in products.csv
# 4. Logs the batch run into production_history.csv


class RunProduction:
    def __init__(self, staff, product_id, product_name, qty_to_produce, requirements, unit_price):
        # requirements format: {material_id: qty_needed_per_single_product_unit}
        if not requirements or qty_to_produce <= 0:
            print("\nError: Production canceled. Invalid quantity or no ingredients provided.")
            return

        # 1 Read current raw materials from file
        try:
            with open("materials.csv", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("\nError: materials.csv not found.")
            return

        if not lines:
            print("\nError: materials.csv is empty.")
            return

        header = lines[0]
        rows = lines[1:]

        # Load inventory into a Python dictionary: {mat_id: [name, unit, stock_qty, unit_cost]}
        inventory = {}
        for line in rows:
            parts = line.strip().split(",")
            if len(parts) >= 5:
                inventory[parts[0]] = [parts[1], parts[2], float(parts[3]), float(parts[4])]

        # making sure Tanan material exists and has enough stock
        deduction_summary = []
        for mat_id, req_qty in requirements.items():
            if mat_id not in inventory:
                print(f"\n[Error] Material ID '{mat_id}' does not exist in inventory. Production aborted.")
                return

            mat_name, unit, stock, _ = inventory[mat_id]
            total_needed = req_qty * qty_to_produce

            # If one material is short, this stops immediately before deducting any stock
            if stock < total_needed:
                print(f"\n[Insufficient Stock] Needs {total_needed} {unit} of '{mat_name}', but only {stock} available.")
                print("Production aborted. No stock was deducted.")
                return

            deduction_summary.append((mat_id, mat_name, total_needed, unit))

        # 3 Deduct the required quantities from inventory
        for mat_id, req_qty in requirements.items():
            total_needed = req_qty * qty_to_produce
            inventory[mat_id][2] -= total_needed

        # 4 Save updated raw materials back to materials.csv
        with open("materials.csv", "w") as f:
            f.write(header)
            for mat_id, data in inventory.items():
                f.write(f"{mat_id},{data[0]},{data[1]},{data[2]},{data[3]}\n")

        # 5 Add or increase finished goods in products.csv
        prod_lines = []
        try:
            with open("products.csv", "r") as f:
                prod_lines = f.readlines()
        except FileNotFoundError:
            pass

        prod_header = "id,name,stock_qty,unit_price\n"
        prod_updated = False
        new_prod_rows = []

        # If product already exists, add to its current stock, if none add as a new
        if prod_lines:
            for line in prod_lines[1:]:
                parts = line.strip().split(",")
                if parts and parts[0] == str(product_id):
                    new_qty = int(parts[2]) + qty_to_produce
                    new_prod_rows.append(f"{parts[0]},{parts[1]},{new_qty},{parts[3]}\n")
                    prod_updated = True
                else:
                    new_prod_rows.append(line)

        if not prod_updated:
            new_prod_rows.append(f"{product_id},{product_name},{qty_to_produce},{unit_price}\n")

        with open("products.csv", "w") as f:
            f.write(prod_header)
            f.writelines(new_prod_rows)

        # 6 Save an record to production_history.csv
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("production_history.csv", "r") as f:
                pass
        except FileNotFoundError:
            with open("production_history.csv", "w") as f:
                f.write("timestamp,staff_id,staff_name,product,qty_produced,materials_used\n")

        # Combine material usage into a clean text string (e.g. "10 pcs of Wood; 40 pcs of Screws")
        usage_str = "; ".join([f"{amt} {u} of {name}" for _, name, amt, u in deduction_summary])

        with open("production_history.csv", "a") as f:
            f.write(f"{timestamp},{staff.id},{staff.name},{product_name},{qty_to_produce},{usage_str}\n")

        # Display success summary to the user
        print("\n========================================")
        print("Production Successful!")
        print(f"Produced: {qty_to_produce} unit(s) of '{product_name}'")
        print("Deductions applied:")
        for _, name, amt, u in deduction_summary:
            print(f"  - {amt} {u} of {name}")
        print(f"Operator: {staff.name} [{staff.role}]")
        print("========================================\n")
