# Robert Lowder 5/20/2024
# Lecture 1 Assignment 3 - File Extensions
# https://cs50.harvard.edu/python/2022/psets/1/extensions/

# Take input of file extension
spam = input("File name: ")
# check if input ends with any filetype name
# match spam:
#     case spam.endswith(".gif"):
#         print("image/gif")
#     case spam.endswith(".jpg") | spam.endswith(".jpeg"):
#         print("image/jpeg")
#     case spam.endswith(".png"):
#         print("image/png")
#     case spam.endswith(".pdf"):
#         print("application/pdf")
#     case spam.endswith(".txt"):
#         print("text/plain")
#     case spam.endswith(".zip"):
#         print("application/zip")
    

if spam.endswith(".gif"):
    print("image/gif")
elif spam.endswith(".jpg") | spam.endswith(".jpeg"):
    print("image/jpeg")
elif spam.endswith(".png"):
    print("image/png")
elif spam.endswith(".pdf"):
    print("application/pdf")
elif spam.endswith(".txt"):
    print("text/plain")
elif spam.endswith(".zip"):
    print("application/zip")
else:
    print("invalid")
      

# output mediatype

