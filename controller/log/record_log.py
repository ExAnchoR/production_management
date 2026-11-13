import time

class RecordLog:
    def __init__(self, staff=None, action=None, details=None):
        if staff is None or action is None:
            return

        # Format a simple readable timestamp: YYYY-MM-DD HH:MM:SS
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        staff_id = staff.id if staff.id else "UNKNOWN"
        staff_name = staff.name if staff.name else "UNKNOWN"

        try:
            with open("activity_logs.csv", "r") as f:
                pass
        except FileNotFoundError:
            with open("activity_logs.csv", "w") as f:
                f.write("timestamp,staff_id,staff_name,action,details\n")

        with open("activity_logs.csv", "a") as f:
            f.write(f"{current_time},{staff_id},{staff_name},{action},{details}\n")