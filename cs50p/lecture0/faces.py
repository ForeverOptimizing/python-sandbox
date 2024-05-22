# Robert Lowder 5/20/2024
# Lecture 0 Assignment 3 - Making Faces
# https://cs50.harvard.edu/python/2022/psets/0/faces/


# define main function
def main():
# call convert function passing a string
    eggs = convert(input())
    print(eggs)
    # print("Success 02")

# # Define convert that accepts a str as input
def convert(spam):
# # return with any :) and :( conveted to an emoticon
    temp = spam.replace(":)", "🙂")
    temp = temp.replace(":(", "🙁")
    # temp = temp.replace("u", "WOWOWOW")
    # print("Success 01")
    return temp






main()