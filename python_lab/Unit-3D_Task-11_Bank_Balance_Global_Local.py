balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("After deposit:", balance)

def show_balance():
    balance = 500
    print("Local balance:", balance)

deposit(500)
show_balance()
print("Account balance:", balance)