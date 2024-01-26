
class ExpenseSharingApp:

    def __init__(self):
        '''
        Constructor to initiate variables
        '''
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
        '''
        To get users in involved int the transaction
        :return: PeopleInvolvedInTransaction
                 new_user - Newly added users
        '''
        while True:
            try:
                self.numberOfPeople = int(input("Enter Number of People: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Error: Please enter a valid digit.")

        existing_friends=[]
        new_user=[]
        PeopleInvolvedInTransaction=[]
        names=[]

        for i in range(0, self.numberOfPeople):
            while True:
                try:
                    name = input("Enter the user name: ").lower()
                    if name.isalpha():
                        if name not in names:
                            names.append(name)
                            break  # Exit the loop if the input is valid
                        else:
                            print("Error: Name already exists. Please enter a unique name.")
                    else:
                        print("Error: Only alphabetical characters are allowed for the name")
                except ValueError:
                    print("Error: Only alphabetical characters are allowed for the name")
            PeopleInvolvedInTransaction.append(name)
            self.new_friend = True

        if len(self.friends)==0:
            self.friends=PeopleInvolvedInTransaction
            #print("New Users: ",PeopleInvolvedInTransaction)
        else:
            for user in PeopleInvolvedInTransaction:
                if user not in self.friends:
                    new_user.append(user)
                   # print("new users: ",user)
                    self.new_friend = True
                    self.friends.append(user)
                else:
                    existing_friends.append(user)
                    self.existing_friend = True

            print("Newly added people",new_user)
            print("Existing users involved in this transaction", existing_friends)

        return PeopleInvolvedInTransaction,new_user

    def get_TotalExpense(self,PeopleInvolvedInTransaction):
        while True:
            try:
                self.total_expense = int(input("Enter the Total Amount: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Error: Please enter a valid amount.")
        while True:
                try:
                    self.paidby = input("Paidby").lower()
                    if self.paidby in PeopleInvolvedInTransaction:
                        break  # Exit the loop if the input is valid
                    else:
                        print("Error: This User does not exist in transaction.")
                except ValueError:
                    print("Error: Please enter a valid user.")


    def split_equally(self,PeopleInvolvedInTransaction):
        '''
        to split the expense in equal shares
        :param PeopleInvolvedInTransaction:
        :return: none
        '''
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
        print("splitted equally",self.split_equal_amount)

    def create_individualdict(self,PeopleInvolvedInTransaction,new_user):
        '''
        To create individual dictionaries to add and settle the balances of each user and display who owns whom
        :param PeopleInvolvedInTransaction:
        :param new_user:
        :return: none
        '''
        my_list = list(self.friends)
        my_dict = self.balances
        if len(self.individual_dicts) == 0:
            for user in my_list:
                self.individual_user_dict = {other_user: 0 for other_user in my_list if other_user != user}
                self.individual_dicts[f'{user}'] = self.individual_user_dict
        if self.new_friend:
                for user in new_user:
                    new_profile = {other_user: 0 for other_user in PeopleInvolvedInTransaction if other_user != user }
                    self.individual_dicts[user]=new_profile
                #for person, value in self.individual_dicts.items():
                    #print(f"{person} = {value}")
        if self.existing_friend and self.new_friend:
            for user in PeopleInvolvedInTransaction:
                for i in range(0,len(new_user)):
                    newUser=new_user[i]
                    if user != newUser:
                        if newUser not in self.individual_dicts[user]:
                            self.individual_dicts[user][newUser] = 0
        if self.existing_friend:
            otherUser=[]
            for user in PeopleInvolvedInTransaction:
                if user!=self.paidby:
                    otherUser.append(user)
                for i in range(0,len(otherUser)):
                        if otherUser[i] not in self.individual_dicts[self.paidby] :
                            self.individual_dicts[self.paidby][otherUser[i]] = 0
                            print("#### Updated profile:", self.individual_dicts[user])
                        if self.paidby not in self.individual_dicts[otherUser[i]]:
                            self.individual_dicts[otherUser[i]][self.paidby] = 0
                            print("#### Updated profile:", self.individual_dicts[otherUser[i]])

        # Print individual dictionaries
        for key, value in self.individual_dicts.items():
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



    def display_amount(self):
        print("\n_______________ BALANCES ___________________")
        for person, value in self.individual_dicts.items():
            print(str(person).upper(), ":")
            d = self.individual_dicts[person]
            for name, amount in d.items():
                print("- ", name, " owes ", amount)


def main():
    Transaction = ExpenseSharingApp()
    while True:
        print("\n Please choose any action \n")
        print("1. Add Expense")
        print("2. Exit")
        while True:
            try:
                choice = int(input("Enter a value from 1 to 2: "))
                if 1 <= choice <= 5:
                    break  # Exit the loop if the input is valid
                else:
                    print("Error: Please enter a digit from 1 and 2.")
            except ValueError:
                print("Error: Please enter a valid digit.")

        if choice == 1:
            PeopleInvolved,new_user = Transaction.get_friends()
            Transaction.get_TotalExpense(PeopleInvolved)
            Transaction.split_equally(PeopleInvolved)
            Transaction.create_individualdict(PeopleInvolved,new_user)
            Transaction.display_amount()
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()








