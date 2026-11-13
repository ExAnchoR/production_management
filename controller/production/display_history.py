# Controller to view the log of all completed production batches
class DisplayHistory:
    def __init__(self):
        try:
            with open("production_history.csv", "r") as file:
                lines = file.readlines()[1:]  # Skip header row

                if not lines:
                    print("\nNo batch production runs recorded.")
                    return

                # Print formatted history of past production
                print("\n========================= PRODUCTION HISTORY =========================")
                for line in lines:
                    line_clean = line.strip()
                    if not line_clean:
                        continue
                    parts = line_clean.split(",")
                    if len(parts) >= 6:
                        materials_used = ",".join(parts[5:])
                        print(f"[{parts[0]}] Staff: {parts[2]} ({parts[1]})")
                        print(f"  -> Produced: {parts[4]}x '{parts[3]}'")
                        print(f"  -> Consumed: {materials_used}")
                        print("-----------------------------------------------------------------------------")
                print("============================================================================\n")

        except FileNotFoundError:
            print("\nError: production_history.csv not found.")
