class DisplayLog:
    def __init__(self):
        try:
            with open("activity_logs.csv", "r") as file:
                lines = file.readlines()[1:]

                if not lines:
                    print("\nNo activity logs recorded yet.")
                    return

                print("\n============================== ACTIVITY LOGS ==============================")
                for line in lines:
                    parts = line.strip().split(",")
                    if len(parts) >= 5:
                        print(f"[{parts[0]}] Staff: {parts[2]} ({parts[1]}) | Action: {parts[3]} | Info: {parts[4]}")
                print("===========================================================================\n")

        except FileNotFoundError:
            print("\nError: activity_logs.csv not found.")