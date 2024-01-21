
class ExpenseSharingApp:

    def __init__(self):
        self.friends = []
        self.numberOfPeople = 0
        self.total_expense = 0
        self.balances ={}
        self.new_friend = False
        self.existing_friend = False
        self.PeopleInvolvedInTransaction = []
        self.paidby=''

    def get_friends(self):
        self.numberOfPeople = int(input("Enter Number of People: "))
        new_friends= []
        existing_friends=[]
        self.PeopleInvolvedInTransaction=[]

        for i in range(0,self.numberOfPeople):
            name = input("Enter Friend name: ").lower()
            self.PeopleInvolvedInTransaction.append(name)
            new_friends.append(name)
            self.new_friend = True
        for name in self.friends:
            if name not in new_friends:
                new_friends.append(name)
            else:
                existing_friends.append(name)
                self.existing_friend = True
        if self.new_friend:
            self.friends = new_friends
            print("Newly added people",new_friends)
            #return new_friends
        if self.existing_friend:
            self.friends = self.friends
            print("Existing  people", existing_friends)
            #return existing_friend
        return self.PeopleInvolvedInTransaction

    def set_balance(self):
        self.balances = {name: 0.0 for name in self.friends}
    def get_TotalExpense(self):
        self.total_expense = float(input("Enter the Total Amount: "))
        self.paidby = input("Paidby").lower()

    def split_equally(self):
        split_equal_amount= self.total_expense/self.numberOfPeople
        if len(self.balances) ==0:
            self.balances = {name: split_equal_amount for name in self.PeopleInvolvedInTransaction}
        elif self.existing_friend!=True:
            currentTransactionBalance = {name: split_equal_amount for name in self.PeopleInvolvedInTransaction}
            self.balances.update(currentTransactionBalance)
        else:
            currentTransactionBalance={name:split_equal_amount for name in self.PeopleInvolvedInTransaction }
            temp=currentTransactionBalance.keys()
            for key, value in currentTransactionBalance.items():
                if key in self.balances:
                    self.balances[key] += value
           # self.balances.update(currentTransactionBalance)

    def create_individualdict(self):
        my_list = list(self.friends)
        my_dict = self.balances

        individual_dicts = {}

        for item in my_list:
            individual_dict = {other_item: 0 for other_item in my_list if other_item != item}
            individual_dict['total'] = my_dict[item]
            individual_dicts[f'{item}'] = individual_dict

        # Print individual dictionaries
        for key, value in individual_dicts.items():
            print(f"{key} = {value}")
            PersonWhoPaidAmount=f"{key}"
            if PersonWhoPaidAmount == self.paidby:
                for i in self.PeopleInvolvedInTransaction:
                    if i==PersonWhoPaidAmount:
                        for name in self.PeopleInvolvedInTransaction:
                            if name!=PersonWhoPaidAmount:
                                individual_dicts[PersonWhoPaidAmount][name]=self.balances[name]
        print("after changes : ")
        for person, value in individual_dicts.items():
            print(f"{person} = {value}")

        for person,value in individual_dicts.items():
                print(str(person).upper(),":")
                d=individual_dicts[person]
                for name,amount in d.items():
                    print("- ",name, " owes " ,amount)


    def display_amount(self):
        for name in self.friends:
            print(f"{name}:")
            print(f" - Owes: {self.balances[name]:.2f} Euros")


def main():
    Transaction = ExpenseSharingApp()
    while True:
        print("Please choose any action \n")
        print("1. Add Friends")
        print("2. Add Expense")
        print("3. Split Equally")
        print("4. Display balances")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Transaction.get_friends()
        elif choice == 2:
            Transaction.get_TotalExpense()
        elif choice == 3:
            Transaction.split_equally()
        elif choice == 4:
            Transaction.display_amount()
            Transaction.create_individualdict()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()








