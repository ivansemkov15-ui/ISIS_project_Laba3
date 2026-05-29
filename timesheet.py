entries = []

def add_entry(date, task, hours):
    entries.append({"date": date, "task": task, "hours": hours})

def total_hours():
    return sum(entry["hours"] for entry in entries)

def list_entries():
    for entry in entries:
        print(f"{entry['date']} – {entry['task']}: {entry['hours']} ч")
