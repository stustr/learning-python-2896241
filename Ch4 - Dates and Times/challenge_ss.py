
import calendar
from weakref import WeakKeyDictionary


days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

c = calendar.Calendar


def which_day():
    print("Which day of the week do you want to count?")
    for day in calendar.day_name:
        print(day)
    global usr_day 
    usr_day = input()
    if usr_day.lower() not in days:
        print("Not a valid input")
        which_day()


def which_month():
    print("\nIn which month?")
    for month in calendar.month_name:
        print(month)
    global usr_month
    usr_month = input()
    if usr_month.lower() not in months:
        print("Not a valid input")
        which_month()
     
     
def which_year():
    global usr_year
    usr_year = input("\nAnd which year? ")
    
    
def how_many():
    global usr_day_index
    usr_day_index = days.index(usr_day)
    global usr_month_index
    usr_month_index = months.index(usr_month) + 1
    global usr_year_int
    usr_year_int = int(usr_year)
    days_count = 0
    week_list = calendar.monthcalendar(usr_year_int, usr_month_index)
    for i in week_list:
        if i[usr_day_index] != 0:
            days_count += 1
    print(days_count)
    
        
def main():
    which_day()
    which_month()
    which_year()
    how_many()

           
main()  