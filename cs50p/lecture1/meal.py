# Robert Lowder 5/20/2024
# Lecture 1 Assignment 5 - Meal Time
# https://cs50.harvard.edu/python/2022/psets/1/meal/


# time.split()
# hour = int(time[0])
# minute = int(time[1])






def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

    # print(time)



def convert(time):
    time = time.split(":")
    # print(time[0])
    # print(time[1])
    hour = float(time[0])
    # print(hour)
    minute = float(time[1])/60
    # print(minute)
    # print(hour + minute)
    return hour + minute


if __name__ == "__main__":
    main()