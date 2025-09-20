# Import the calendar module
import calendar

# Get all month names
months = list(calendar.month_name)  

# month_name[0] is empty, months 1-12 have actual names

# Print the months
for i, month in enumerate(months):
    if i != 0:  # skip the empty string at index 0
        print(month)
