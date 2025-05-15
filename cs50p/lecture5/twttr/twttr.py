# Robert Lowder 04/16/2025
# Lecture 5 Assignment 1 - Testing my twttr
# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/



def main():
    # Gets string
    spam = input("Input: ")
    # Shortens string
    newString = shorten(spam)
    # Prints shortened string
    print(newString)

# Returns string with all vowels omitted
def shorten(spam):
    eggs = ""
    for c in spam:
        match c:
            case "a" | "A":
                pass
            case "e" | "E":
                pass
            case "i" | "I":
                pass
            case "o" | "O":
                pass
            case "u" | "U":
                pass
            case _:
                eggs += c

    return eggs



if __name__ == "__main__":
    main()