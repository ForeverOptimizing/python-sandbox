# Part of L4notes.py

def main():
    hello("world")
    goodbye("world")



def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")


# If this file is run by itself then run the main function, if it is used to call a method then ignore main
if __name__ == "__main__":
    main()