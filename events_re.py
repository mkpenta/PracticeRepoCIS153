import re

def menu():
    print("""
        Enter a number
        1. search for date
        2. enter new event
        3. exit""")
    choice = int(input())
    return choice

def make_new_event(calendar, name, y, m, d):
    if (y,m,d) in calendar:
        return False
    else:
        calendar[(y,m,d)] = name
        return True
    
def save_calendar(calendar):
     with open('events.txt', 'w') as file:
         for year,month,day in calendar:
             file.write(f"{calendar[(year, month, day)]} :: {year}-{month}-{day}\n")


def build_calendar():
    # a calendar of dates to return
    calendar = {}
    #pattern to search with RE (format Event Name :: YYYY-MM-DD)
    pattern = r"(.+) :: ([0-9]{4})-([0-9]{2})-([0-9]{2})"

    date_pattern = re.compile(pattern)

    
    with open('events.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            
            # Find all matches in the line
            matches = date_pattern.findall(line)
        
            #extrct variables for each match
            #enter them in a dictionary
            for match in matches:
                #get data
                event,year, month,day  = match
                
                #make a date tuple for dictionary key
                date = (year, month, day)
                
                #only allow one event per date for now
                if date not in calendar:
                    calendar[date] = event
                    print(f"new event - {event}")
                else:
                    print(f"event exists - {event}")
    return calendar

def search_calendar(calendar, date):
    if date not in calendar:
        return None
    else:
        return calendar[date]

def main():
    cal = build_calendar()
    choice = 0
    while not choice == 3:
        choice = menu()
        if choice == 1:
            y = input("enter a year\n")
            m = input("enter a month\n")
            d = input("enter a day\n")
            e = search_calendar(cal,(y,m,d))
            if e == None:
                print("Date not found")
            else:
                print(e)
        elif choice == 2:
            y = input("enter a year\n")
            m = input("enter a month\n")
            d = input("enter a day\n")
            e = input("enter an event name\n")
            result = make_new_event(cal, e, y,m,d)
            if result:
                print("date added")
                save_calendar(cal)
            else:
                print("date exists")
        elif choice == 3:
            print("good bye")
        else:
            print("not a choice")
            
main()
            
            
            