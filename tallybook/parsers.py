
import argparse
import calendar
import datetime as dt
from datetime import date
from tallybook.storage import load_data, save_data
import re
import json


def check_day(habit, day=None):
    '''
    
    '''
    if day != None:
        this = date.today()
        today = date(this.year, this.month, day)
    else:
        today = date.today()
    
    month_key = f"{today.year}-{today.month}" #why :02?
    data = load_data()

    if habit not in data:
        data[habit] = {}
    if month_key not in data[habit]:
        data[habit][month_key] = []

    if today.day not in data[habit][month_key]:
        data[habit][month_key].append(today.day)
        print(f"Number of times you have done this habit this month: {len(data[habit][month_key])}")
        save_data(data)
        
#################################################################################

def uncheck_day(habit, day=None):
    if day != None:
        this = date.today()
        today = date(this.year, this.month, day)
    else:
        today = date.today()
    
    month_key = f"{today.year}-{today.month}" #why :02?
    data = load_data()

    if habit not in data:
        print("There is no habit named {habit}")
    if month_key not in data[habit]:
        print("There is no month being tracked for this habit")
    
    if today.day not in data[habit][month_key]:
        print("{day} already unchecked!")

    data[habit][month_key].remove(today.day)
    save_data(data)

#################################################################################

def add(args):

    month_key = f"{date.today().year}-{date.today().month}" # again :02
    data = load_data()
    if args.habit not in data:
        month_color = {month_key : []}
        data[str(args.habit)] = month_color
        
        save_data(data)

    print(f"{str(args.habit)} added to list!")

#################################################################################

def unadd(args):

    month_key = f"{date.today().year}-{date.today().month}" # again :02
    data = load_data()
    if args.habit not in data:
        print(f"Habit {args.habit} not found!")
        return 
    
    del data[str(args.habit)]
    save_data(data)
    print(f"{str(args.habit)} unadded from list!")

#################################################################################

def check(args):
    print(f"{args.habit} checked off for today! Good job!")
    if args.day != None:
        check_day(args.habit, args.day)
    else:
        print("idk rn")

#################################################################################

def uncheck(args): # call it uncheck()
    uncheck_day(args.habit, args.day)

#################################################################################
        
def color(text, day, color):


    day = str(day)
    ansi = re.compile(r'\033\[[0-9;]*m')

    parts = ansi.split(text)
    seps = ansi.findall(text)

    RESET = '\033[0m'
    colored = f"{color}{day}{RESET}"

    for i in range(len(parts)):
        parts[i] = re.sub(rf'\b{day}\b', colored, parts[i], count=1)

    
    result = parts[0]
    for sep, part in zip(seps, parts[1:]):
        result += sep + part

    return result

#################################################################################

def show_calendar(args):
    
    #https://stackoverflow.com/a/75376935
    '''
    Story time: I was trying to figure out a way to use the built in 
    calendar system to display a date in the terminal that was a different
    color from the rest. I found out that calendar can be formatted purely
    as text. This works well as I decided I want my habit tracker to be a 
    CLI tool. I looked at this guy's implementation. Apparently there was 
    trouble if the string of todays date matched the string of the year. 
    Since that was a problem, he had a solution where he basically checked
    how many times the string of the day appeared in the year, then he colored
    in that many times + 1, and then removed the coloring from the string.
    I thought that was goofy, so this implementation uses string manipulation
    to split the string from its days and header, do the coloring, and then join
    them back together again. I think it looks nice.
    '''

    habit = args.habit
    data = load_data()
    month_key = f"{date.today().year}-{date.today().month}" # again :02
    checked_days = data.get(habit, {}).get(month_key, [])

    

    today = date.today()
    GREEN = '\033[92m'
    RED =  '\033[31m'
    RESET = '\033[0m'

    cal = (calendar.month(today.year, today.month))

    # splits entire calendar string into days and the rest of the 
    # calendar.
    lines = cal.splitlines()
    day_lines = lines[2:] 
    day_lines = "\n".join(day_lines)

    other_lines = lines[:2]
    other_lines = "\n".join(other_lines)

    for marked_day in checked_days:
        colored_day = RED + str(marked_day) + RESET
        day_lines = color(day_lines, str(marked_day), RED)

    cal = other_lines + "\n" + day_lines

    print(cal)

#################################################################################

def list_habits(args):
    data = load_data()

    print("Here is a list of all the habits you are tracking")
    print("=================================================")
    for k in data:
        print(k)

#################################################################################
