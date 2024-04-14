import json
from datetime import datetime

def load_birthdays(filename):
    with open(filename, 'r') as file:
        birthdays = json.load(file)
    return birthdays

def count_birthdays_by_month(birthdays):
    month_count = {
        "January": 0, "February": 0, "March": 0, "April": 0,
        "May": 0, "June": 0, "July": 0, "August": 0,
        "September": 0, "October": 0, "November": 0, "December": 0
    }

    for date_str in birthdays.values():
        month = datetime.strptime(date_str, '%Y-%m-%d').strftime('%B')
        match month:
            case "January":
                month_count["January"] += 1
            case "February":
                month_count["February"] += 1
            case "March":
                month_count["March"] += 1
            case "April":
                month_count["April"] += 1
            case "May":
                month_count["May"] += 1
            case "June":
                month_count["June"] += 1
            case "July":
                month_count["July"] += 1
            case "August":
                month_count["August"] += 1
            case "September":
                month_count["September"] += 1
            case "October":
                month_count["October"] += 1
            case "November":
                month_count["November"] += 1
            case "December":
                month_count["December"] += 1
            case _:
                print(f"Unknown month: {month}")

    return month_count

def main():
    birthdays = load_birthdays("birthdays.json")
    if birthdays:
        month_count = count_birthdays_by_month(birthdays)
        for month, count in month_count.items():
            print(f"{month}: {count}")
    else:
        print("No data to show.")


main()