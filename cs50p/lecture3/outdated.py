# Robert Lowder 01/17/2025
# Lecture 3 Assignment 4 - Outdated
# https://cs50.harvard.edu/python/2022/psets/3/outdated/


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = gatherDate()
    print(date)


def gatherDate():
    while True:
        try:
            spam = input("Date: ")
            # if spam contains a comma
            if spam.count(",") == 1:
                # separate by comma
                left, year = spam.rsplit(",")
                # separate left half by white space
                # check if left half is two elements (month days)
                month, day = left.split()
                # check if month shows up in the list
                # if months.count(month.capitalize()) != 1: continue
                if month.capitalize() not in months: continue
                # check if day is between 1 and 31
                if int(day) < 1 or int(day) > 31: continue
                # check if year is an integer
                year = int(year)
                # change month into number
                month = months.index(month.capitalize()) + 1
                # reformat date into correct structure 2025-01-17
                date = (f"{year}-{month:02}-{int(day):02}")
                return date
            # elif spam contains slash
            elif spam.count("/") == 2:
                # separate by slash
                # ensure there are 3 variables
                month, day, year = spam.rsplit("/")
                # check if all variables are integers
                month = int(month)
                day = int(day)
                year = int(year)
                # check if day is between 1 and 31
                if day < 1 or day > 31: continue
                # check if month is between 1 and 12
                if month < 1 or month > 12: continue
                # reformat date into correct structure 2025-01-17
                # date = (f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}")
                date = (f"{year}-{month:02}-{day:02}")
                return date
        except ValueError:
            pass
    


main()