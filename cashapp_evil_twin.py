 class CashAppEvilTwin:
    def __init__(self):
        self.balance = 0.00  # Start with a balance of 0

    def set_balance(self, amount):
        self.balance = amount  
        print(f"Fake cash balance set to: ${self.balance:.2f}")

    def send_money(self, username, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return False  
        self.balance -= amount  
        print(f"Sent ${amount:.2f} to {username}. New balance: ${self.balance:.2f}")
        return True

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

def main():
    app = CashAppEvilTwin()
    print("Welcome to the CashApp Evil Twin Simulator!")
    
    while True:
        action = input("Enter 'set' to set balance, 'send' to send money, 'balance' to check balance, or 'exit' to quit: ")
        
        if action == 'set':
            amount = float(input("Enter fake cash balance: "))
            app.set_balance(amount)
        elif action == 'send':
            user = input("Enter username: ")
            amount = float(input("Enter amount to send: "))
            app.send_money(user, amount)
        elif action == 'balance':
            app.check_balance()
        elif action == 'exit':
            print("Exiting CashApp Evil Twin Simulator.")
            break  
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
