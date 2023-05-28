
#initialize variables



# Define Bank Account Class

class Account:
    def __init__(self):
        self.pin = 0
        self.name = 'Default'
        self.balance = 0.0




# Get user defined PIN number

# CHeck Balance

    def balance(self):
        return self.balance



# Define Deopositing Function
    def deposit(self,cash):
        self.balance += cash



# Define Withraw Function
# CHeck if funds are available
    def withdraw(self):
        keepGoing = True
        while(keepGoing):
            try:
                amount = float(input('How much would you like to withdrawl: \n$'))
            except:
                print('ERROR!!!')
                break

            if(amount > self.balance):
                print(f'That exceeds your balance in this account.\nYour current balance is: ${self.balance}')
            else:
                self.balance -= amount
                keepGoing = False
        





# Define __str__
    def __str__(self):
        return f'{self.name}s Account'



#