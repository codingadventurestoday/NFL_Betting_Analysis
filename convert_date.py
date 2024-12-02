from datetime import datetime, timedelta


def convert_date(date_str):
    """set date to mm-dd-yyyy and return it"""
    now = datetime.now()
    if date_str == "today":
        # Format tomorrow's date in mm-dd-yyyy format
        reval_str = now.strftime('%m-%d-%Y')

    elif date_str == "tomorrow":
        # Add one day (to get tomorrow)
        tomorrow = now + timedelta(days=1)
        # Format tomorrow's date in mm-dd-yyyy format
        reval_str = tomorrow.strftime('%m-%d-%Y')

    else:
        # Remove the ordinal suffix (ND, ST, TH) and day of week
        date_str = date_str[4:-2]
        year = str(now.year)
        date_str = date_str + " " + year

        # Parse the date string to a datetime object
        date_obj = datetime.strptime(date_str, "%b %d %Y")

        reval_str = date_obj.strftime("%m-%d-%Y")

    return reval_str


#example 
# MON DEC 2nd
"""
datetime.strptime -->
datatime.strftime -->
"""
