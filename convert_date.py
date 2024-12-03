from datetime import datetime, timedelta


def convert_date(date_str):
    """set date to mm-dd-yyyy and return it"""
    now = datetime.now()
    if date_str == "today":
        # Format tomorrow's date in mm-dd-yyyy format
        reval_str = now.strftime('%Y-%m-%d')

    elif date_str == "tomorrow":
        # Add one day (to get tomorrow)
        tomorrow = now + timedelta(days=1)
        # Format tomorrow's date in mm-dd-yyyy format
        reval_str = tomorrow.strftime('%Y-%m-%d')

    else:
        # Remove the ordinal suffix (ND, ST, TH) and day of week
        date_str = date_str[4:-2]
        year = str(now.year)
        date_str = date_str + " " + year

        # Parse the date string to a datetime object
        date_obj = datetime.strptime(date_str, "%b %d %Y")

        reval_str = date_obj.strftime("%Y-%m-%d")

    return reval_str

def check_starting_time(starting_time, date_of_game):
    """check time of game; update date of game -1 if before 4am"""
    hour = int(starting_time.split(":")[0])
    
    if starting_time.endswith("AM") and hour <= 4:
        date_of_game = datetime.strptime(date_of_game, "%Y-%m-%d") 
        date_of_game -= timedelta(days=1)
        date_of_game = date_of_game.strftime("%Y-%m-%d")

    return date_of_game

#example 
# MON DEC 2nd
"""
datetime.strptime -->
datatime.strftime -->
"""
