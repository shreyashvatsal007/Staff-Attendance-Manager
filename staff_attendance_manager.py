from datetime import date


def create():
    file = open("attendance.txt", "w")
    file.write("Name Date Status\n")
    file.close()
    print("Attendance file created successfully.\n")

def inputdata():
    name = input("Enter staff name: ")
    today = str(date.today())
    status = input("Enter status (P = Present / A = Absent): ")
    status = status.upper()
    return name, today, status

def write(name, today, status):
    line = name + " " + today + " " + status + "\n"
    file = open("attendance.txt", "a")
    file.write(line)
    file.close()
    print("Attendance recorded for", name)

def mark():
    name, today, status = inputdata()
    write(name, today, status)

def read():
    file = open("attendance.txt", "r")
    lines = file.readlines()
    file.close()
    return lines

def show(lines):
    print("\n--- Attendance Records ---")
    for line in lines:
        print(line.strip())

def count(lines):
    total = {}
    for i in range(1, len(lines)):
        record = lines[i].strip().split()
        if len(record) == 3:
            name, date_str, status = record
            status = status.upper()
            if name not in total:
                total[name] = {"P": 0, "A": 0}
            if status == "P":
                total[name]["P"] += 1
            elif status == "A":
                total[name]["A"] += 1
    return total

def summary(total):
    print("\n--- Summary per Person ---")
    for name, counts in total.items():
        print(f"{name}: Present = {counts['P']}, Absent = {counts['A']}")

def main():
    while True:
        print("--- Staff Attendance Manager ---")
        print("1. Create New Attendance File")
        print("2. Mark Attendance")
        print("3. View Attendance and Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create()
        elif choice == "2":
            mark()
        elif choice == "3":
            lines = read()
            show(lines)
            total_data = count(lines)
            summary(total_data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
