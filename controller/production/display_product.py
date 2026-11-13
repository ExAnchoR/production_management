# Controller to read and display finished goods catalog from products.csv
class DisplayProduct:
    def __init__(self):
        try:
            with open("products.csv", "r") as file:
                lines = file.readlines()[1:]

                if not lines:
                    print("\nNo finished goods in inventory yet.")
                    return

                # Print formatted list of finished products
                print("\n==================== FINISHED GOODS ====================")
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) >= 4:
                        print(f"ID: {parts[0]} | Product: {parts[1]} | Qty Produced: {parts[2]} | Price: PHP {parts[3]}")
                print("========================================================\n")

        except FileNotFoundError:
            print("\nNo production runs recorded yet (products.csv not found).")
