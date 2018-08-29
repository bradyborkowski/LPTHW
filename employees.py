class emp(object):

    def __init__(self, first, last, rate):
        self.first = first
        self.last = last
        self.rate = rate
        self.email = first + '.' + last + '@pgfmsolutions.com'

    def give_raise(self):
        print(f"{self.first} {self.last} currently makes ${self.rate} per year")
        print(f"Would you like to give {self.first} {self.last} a raise?")
        confirm = input("Yes or No? > ")

        if confirm == 'yes':

            print("Give the raise by percentage, or total increase?")
            choice = input("Type 'percentage' or 'total' > ")

            if choice == 'percentage':

                print(f"What percentage will you increase {self.first}'s pay by?")

                amount = float(input("Enter a percentage: > "))
                percent = round((amount / 100), 2)

                print(f"Increasing {self.first}'s pay by {percent * 100}%")

                oldrate = self.rate
                newrate = (self.rate * percent) + self.rate
                change = newrate - oldrate

                print(f"{self.first} {self.last} has recieved a raise of ${change}")
                print(f"Added to their previous rate of ${oldrate} makes their current rate ${newrate}")

                self.rate = newrate

                print(f"Be sure to tell {self.first} that their raise has been processed!")

                return self.rate

            elif choice == 'total':
                print(f"How much would you like to raise {self.first}'s pay by?'")
                amount = int(input("Enter an amount: > "))
                print(f"Increasing {self.first}'s pay by ${amount}")
                oldrate = self.rate
                newrate = (self.rate + amount)
                percent = round(float(amount / oldrate), 2)
                print(f"{self.first} {self.last} has recieved a raise of ${amount}")
                print(f"Added to their previous rate of ${oldrate} makes their current rate ${newrate}")
                self.rate = newrate
                print(f"Be sure to tell {self.first} that their raise has been processed!")
                return self.rate

            else:
                print("Sorry, that's not an option.")

        else:
            print("No problem, goodbye!")

    def show_pay(self):
        return self.rate
