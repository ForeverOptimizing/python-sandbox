# Robert Lowder 01/17/2025
# Lecture 3 Assignment 3 - Grocery List
# https://cs50.harvard.edu/python/2022/psets/3/grocery/




def main():
    items = getItems()
    items = sortItems(items)
    print(items)



def getItems():
    items = {}
    while True:
        try:
            # get item
            item = input()
            # add item to items
            items.append(item)
            # items += item     # This just adds each character to the list rather than the word
        # wait for EOF
        except EOFError:
            return items


def sortItems(items):
    return items

main()

















# def main():
#     sortItems(gatherItems())


# def gatherItems():
#     items = []
#     gathering = True
#     while gathering:
#         try:
#             items.append(input().capitalize())
#         except EOFError:
#             return items

# def sortItems(items):
#     for x in items:
#         print(f"{items[x].count} {items[x]}")




# main()