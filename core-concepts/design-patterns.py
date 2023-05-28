
"""
TITLE: 8 Design Patterns EVERY Developer Should Know
SOURCE: https://youtu.be/tAuRQs_d9F8
AUTHOR: NeetCode
"""





# Factory
# Allows you to hide the secret ingredients

# class Burger:
#     def __init__(self,ingredients):
#         self.ingredients = ingredients

#     def print(self):
#         print(self.ingredients)

# class BurgerFactory:

#     def createCheeseBurger(self):
#         ingredients = ["bun", "cheese", "beef-patty"]
#         return Burger(ingredients)

#     def createDeluxeCheeseBurger(self):
#         ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
#         return Burger(ingredients)

#     def createVeganBurger(self):
#         ingredients = ["bun", "special-sauce", "veggie-patty"]
#         return Burger(ingredients)
    
# burgerFactory = BurgerFactory()
# burgerFactory.createCheeseBurger().print()
# burgerFactory.createDeluxeCheeseBurger().print()
# burgerFactory.createVeganBurger().print()





# Builder

# class Burger:
#     def __init__(self):
#         self.buns = None
#         self.patty = None
#         self.cheese = None

#     def setBuns(self, bunStyle):
#         self.buns = bunStyle

#     def setPatty(self, pattyStyle):
#         self.patty = pattyStyle

#     def setCheese(self, cheeseStyle):
#         self.cheese = cheeseStyle
    
# class BurgerBuilder:
#     def __init__(self):
#         self.burger = Burger()

#     def addBuns(self, bunStyle)
#         self.burger.setBuns(bunStyle):
#         return self

#     def addPatty(self, pattyStyle):
#         self.burger.setPatty(pattyStyle)
#         return self
    
#     def addCheese(self, cheeseStyle):
#         self.burger.setCheese(cheeseStyle)
#         return self

#     def build(self):
#         return self.burger

# burger = BurgerBuilder() \
#             .addBuns("sesame") \
#             .addPatty("fish-patty") \
#             .addCheese("swiss cheese") \
#             .build()

# Singleton
class ApplicationState:
    instance = None











