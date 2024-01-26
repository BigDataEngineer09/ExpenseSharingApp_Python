
class ExpenseSharingApp:

    def __init__(self):
        self.friends = []
        self.new_friends = []
        self.numberOfPeople= 0
        self.total_expense = 0
        self.balances={}
        self.individual_dicts={}
        self.new_friend = False
        self.existing_friend= False
        self.paidby=''

    def get_friends(self):
        while True:
            try:
                self.numberOfPeople = int(input("Enter Number of People: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Error: Please enter a valid digit.")

        existing_friends=[]
        new_user=[]
        PeopleInvolvedInTransaction=[]

        for i in range(0, self.numberOfPeople):
            while True:
                try:
                    name = input("Enter Friend name: ").lower()
                    if name.isalpha():
                        break  # Exit the loop if the input is valid
                    else:
                        print("Error: Only alphabetical characters are allowed for the name")
                except ValueError:
                    print("Error: Only alphabetical characters are allowed for the name")
            PeopleInvolvedInTransaction.append(name)
            self.new_friend = True

        if len(self.friends)==0:
            self.friends=PeopleInvolvedInTransaction
            print("New Users: ",PeopleInvolvedInTransaction)
        else:
            for user in PeopleInvolvedInTransaction:
                if user not in self.friends:
                    new_user.append(user)
                    print("new users: ",user)
                    self.new_friend = True
                    self.friends.append(user)
                else:
                    existing_friends.append(user)
                    self.existing_friend = True

            print("Newly added people",new_user)
            print("Existing  people involved in transaction", existing_friends)

        return PeopleInvolvedInTransaction,new_user

    def get_TotalExpense(self):
        self.total_expense = float(input("Enter the Total Amount: "))
        self.paidby = input("Paidby").lower()

    def split_equally(self,PeopleInvolvedInTransaction):
        self.split_equal_amount= self.total_expense/self.numberOfPeople
        if len(self.balances) ==0:
            currentTransactionBalance= {name: self.split_equal_amount for name in PeopleInvolvedInTransaction}
            self.balances = currentTransactionBalance
        elif self.existing_friend!=True:
            currentTransactionBalance = {name: self.split_equal_amount for name in  PeopleInvolvedInTransaction}
            self.balances.update(currentTransactionBalance)
        else:
            currentTransactionBalance={name:self.split_equal_amount for name in PeopleInvolvedInTransaction }
            for key, value in currentTransactionBalance.items():
                if key in self.balances:
                    self.balances[key] += value
                else:
                    self.balances[key] = value
        #print("splitted equally",self.balances)

    def create_individualdict(self,PeopleInvolvedInTransaction,new_user):
        my_list = list(self.friends)
        my_dict = self.balances
        if len(self.individual_dicts) == 0:
            for user in my_list:
                self.individual_user_dict = {other_user: 0.0 for other_user in my_list if other_user != user}
                self.individual_dicts[f'{user}'] = self.individual_user_dict
        if self.new_friend:
                for user in new_user:
                    new_profile = {other_user: 0.0 for other_user in PeopleInvolvedInTransaction if other_user != user }
                    self.individual_dicts[user]=new_profile
                   # print("/n ### new_profile: ", self.individual_dicts[user])
                for person, value in self.individual_dicts.items():
                    print(f"{person} = {value}")
        if self.existing_friend and self.new_friend:
            for user in PeopleInvolvedInTransaction:
                for i in range(0,len(new_user)):
                    newUser=new_user[i]
                    if user != newUser:
                        if newUser not in self.individual_dicts[user]:
                            self.individual_dicts[user][newUser] = 0.0
                            #print("#### Updated profile:", self.individual_dicts[user])
        if self.existing_friend:
            otherUser=[]
            for user in PeopleInvolvedInTransaction:
                if user!=self.paidby:
                    otherUser.append(user)
                for i in range(0,len(otherUser)):
                        if otherUser[i] not in self.individual_dicts[self.paidby] :
                            self.individual_dicts[self.paidby][otherUser[i]] = 0.0
                            #print("#### Updated profile:", self.individual_dicts[user])


        # Print individual dictionaries
        for key, value in self.individual_dicts.items():
            #print(f"{key} = {value}")
            PersonWhoPaidAmount=f"{key}"
            if PersonWhoPaidAmount == self.paidby:
                    for name in PeopleInvolvedInTransaction:
                        if name != self.paidby:
                            balance_PersonWhoPaid = self.individual_dicts[PersonWhoPaidAmount][name]
                            balance_otherUser=self.individual_dicts[name][PersonWhoPaidAmount]
                            if balance_otherUser ==0 and balance_PersonWhoPaid ==0:
                                self.individual_dicts[PersonWhoPaidAmount][name] += self.split_equal_amount
                            elif balance_otherUser<=self.split_equal_amount:
                                self.individual_dicts[name][PersonWhoPaidAmount] =0
                                self.individual_dicts[PersonWhoPaidAmount][name]=self.split_equal_amount - balance_otherUser
                            else:
                                self.individual_dicts[name][PersonWhoPaidAmount]-=self.split_equal_amount

                            #self.individual_dicts[PersonWhoPaidAmount][name] +=self.split_equal_amount
        '''
        print("after changes : ")
        for person, value in self.individual_dicts.items():
            print(f"{person} = {value}")
        '''
        for person,value in self.individual_dicts.items():
                print(str(person).upper(),":")
                d=self.individual_dicts[person]
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
        while True:
            try:
                choice = int(input("Enter a value from 1 to 5: "))
                if 1 <= choice <= 5:
                    break  # Exit the loop if the input is valid
                else:
                    print("Error: Please enter a digit from 1 to 5.")
            except ValueError:
                print("Error: Please enter a valid digit.")

        if choice == 1:
            PeopleInvolved,new_user = Transaction.get_friends()
        elif choice == 2:
            Transaction.get_TotalExpense()
        elif choice == 3:
            Transaction.split_equally(PeopleInvolved)
        elif choice == 4:
            Transaction.create_individualdict(PeopleInvolved,new_user)



        elif choice == 5:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()








