import pandas as pd
from datetime import datetime, timedelta

def analyze_timesheet(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Sort the data by Employee Name and Time
    df = df.sort_values(by=['Employee Name', 'Time'])

    # Initialize variables to track shifts and employees
    current_employee = None
    current_shift_start = None
    consecutive_days = 0

    # Iterate through the rows in the DataFrame
    for index, row in df.iterrows():
        employee = row['Employee Name']
        shift_start = row['Time']

        # Check for consecutive days
        if current_employee == employee:
            if (shift_start - current_shift_start).days == 1:
                consecutive_days += 1
            else:
                consecutive_days = 0
        else:
            consecutive_days = 0

        # Check for 7 consecutive days
        if consecutive_days == 6:
            print(f"{employee} has worked for 7 consecutive days. Position: {row['Position ID']}")

        # Check for less than 10 hours between shifts
        if current_employee == employee and (shift_start - current_shift_start).seconds < 36000 and (shift_start - current_shift_start).seconds > 3600:
            print(f"{employee} has less than 10 hours between shifts. Position: {row['Position ID']}")

        # Check for more than 14 hours in a single shift
        shift_hours = row['Timecard Hours (as Time)'].seconds / 3600
        if shift_hours > 14:
            print(f"{employee} has worked for more than 14 hours in a single shift. Position: {row['Position ID']}")

        # Update current employee and shift information
        current_employee = employee
        current_shift_start = shift_start

# Assuming the file is named 'timesheet.xlsx', you can replace it with the actual file name.
file_path = 'https://docs.google.com/spreadsheets/d/1eRujNQYov-tZ8j9yvkah6lSzJOpNweMF/edit?usp=drive_link&ouid=118321497519425076839&rtpof=true&sd=true'

# Call the function to analyze the timesheet
analyze_timesheet(file_path)
