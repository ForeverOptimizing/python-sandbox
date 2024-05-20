# Robert Lowder 5/20/2024
# Lecture 1 Assignment 4 - Math Interpreter
# https://cs50.harvard.edu/python/2022/psets/1/interpreter/





spam = input("Expression: ")
spam = spam.split()

match spam[1]:
    case "+":
        print(float(spam[0])+float(spam[2]))
    case "-":
        print(float(spam[0])-float(spam[2]))
    case "*":
        print(float(spam[0])*float(spam[2]))
    case "/":
        print(float(spam[0])/float(spam[2]))
    case _:
        print("Invalid")





# Easy Method

# spam = input("Expression: ")
# eggs = float(eval(spam))
# print(eggs)