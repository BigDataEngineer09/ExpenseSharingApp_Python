class ExpenseSharingApp:

    def __init__(self):
        '''
        Constructor to initiate variables
        '''
        self.friends = []
        self.new_friends = []
        self.numberOfPeople = 0
        self.total_expense = 0
        self.balances = {}
        self.individual_dicts = {}
        self.new_friend = False
        self.existing_friend = False
        self.paidby = ''
        self.splitted_Equally = False
        self.splitted_Unequally = False

    def get_friends(self):
        '''
        To get users in involved int the transaction limited to 5 users
        :return: PeopleInvolvedInTransaction
                 new_user - Newly added users
        '''
        while True:
            try:
                self.numberOfPeople = int(input("\nEnter Number of users : "))
                if self.numberOfPeople > 1:
                    if self.numberOfPeople < 6:
                        break
                    else:
                        print("Error:Only Maximum of 5 users can be added")
                else:
                    print("Error: Transaction should involve more than 1 user")
            except ValueError:
                print("Error: Please enter a valid digit.")

        existing_friends = []
        new_user = []
        PeopleInvolvedInTransaction = []
        names = []

        for i in range(0, self.numberOfPeople):
            while True:
                try:
                    name = input("Enter the user name : ").lower()
                    if name.isalpha():
                        if name not in names:
                            names.append(name)
                            break
                        else:
                            print("Error: Name already exists. Please enter a unique name.")
                    else:
                        print("Error: Only alphabetical letters are permitted.")
                except ValueError:
                    print("Error: Only alphabetical letters are permitted.")
            PeopleInvolvedInTransaction.append(name)
            self.new_friend = True

        if len(self.friends) == 0:
            self.friends = PeopleInvolvedInTransaction
            # print("New Users: ",PeopleInvolvedInTransaction)
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

        # print("Newly added people ", new_user)
        # print("Existing users being a  part of this transaction ", existing_friends)

        return PeopleInvolvedInTransaction, new_user

    def get_TotalExpense(self, PeopleInvolvedInTransaction):
        while True:
            try:
                self.total_expense = float(input("Enter the Total Amount in Euros: "))
                if self.total_expense > 0:
                    break
                else:
                    print("Error: Enter postive values")
            except ValueError:
                print("Error: Please enter a valid amount.")
        while True:
            try:
                self.paidby = input("Paidby : ").lower()
                if self.paidby in PeopleInvolvedInTransaction:
                    break
                else:
                    print("Error: This User does not exist in transaction.")
            except ValueError:
                print("Error: Please enter a valid user.")

    def split_equally(self, PeopleInvolvedInTransaction):
        '''
        to split the expense in equal shares
        :param PeopleInvolvedInTransaction:
        :return: none
        '''
        self.splitted_Equally = True
        self.split_equal_amount = self.total_expense / self.numberOfPeople
        if len(self.balances) == 0:
            currentTransactionBalance = {user: self.split_equal_amount for user in PeopleInvolvedInTransaction}
            self.balances = currentTransactionBalance
        elif self.existing_friend != True:
            currentTransactionBalance = {user: self.split_equal_amount for user in PeopleInvolvedInTransaction}
            self.balances.update(currentTransactionBalance)
        else:
            currentTransactionBalance = {user: self.split_equal_amount for user in PeopleInvolvedInTransaction}
            for key, value in currentTransactionBalance.items():
                if key in self.balances:
                    self.balances[key] += value
                else:
                    self.balances[key] = value
        print("Splitted Equally : ", self.split_equal_amount)
        self.splitted_Unequally = False

    def split_unequally(self, PeopleInvolvedInTransaction, new_user):
        '''
        to split the expense unequally based on user input
        :param PeopleInvolvedInTransaction:
        :return: none
        '''
        self.splitted_Unequally = True
        if len(self.balances) == 0:
            currentTransactionBalance = self.check_total_expense(PeopleInvolvedInTransaction)
            self.balances = currentTransactionBalance
            self.currentTransactionSplittedUnequally = currentTransactionBalance

        elif self.existing_friend != True:
            currentTransactionBalance = self.check_total_expense(new_user)
            self.balances.update(currentTransactionBalance)
            self.currentTransactionSplittedUnequally = currentTransactionBalance

        else:
            currentTransactionBalance = self.check_total_expense(PeopleInvolvedInTransaction)
            self.currentTransactionSplittedUnequally = currentTransactionBalance

        for key, value in currentTransactionBalance.items():
            if key in self.balances:
                self.balances[key] += value
            else:
                self.balances[key] = value

        self.splitted_Equally = False

    def check_total_expense(self, list):
        '''
        Method to Check if the total amount entered matches the total expense
        :param list:
        :return: currentTransactionBalance
        '''
        while True:
            total_custom_amount = 0
            currentTransactionBalance = {}
            try:
                for user in list:
                    if self.paidby== user:
                        message = f"Enter the amount paid by {user}:"
                    else:
                        message = f"Enter the amount to be paid by  {user} to {self.paidby} : "
                    custom_amount = float(input(message))
                    if custom_amount > 0:
                        currentTransactionBalance[user] = custom_amount
                        total_custom_amount += custom_amount
                    else:
                        print("Error: Enter a non-negative or more than 0 value.")

                if total_custom_amount == self.total_expense:
                    print("Transaction balances set based on user input.")
                    break
                else:
                    print(
                        f"Error: Total custom amount ({total_custom_amount:.2f}) does not match the total expense ({self.total_expense:.2f}). Carefully enter the amounts again.")
            except ValueError:
                print("Error: Please enter a valid amount.")
        return currentTransactionBalance

    def create_individualdict(self, PeopleInvolvedInTransaction, new_user):
        '''
        To set up personalized dictionaries in order to enter and settle each user's balance and display who owns whom
        :param PeopleInvolvedInTransaction:
        :param new_user:
        :return: none
        '''
        my_list = list(self.friends)
        my_dict = self.balances
        if len(self.individual_dicts) == 0:
            for user in my_list:
                self.individual_user_dict = {other_user: 0 for other_user in my_list if other_user != user}
                self.individual_dicts[user] = self.individual_user_dict
        if self.new_friend:
            for user in new_user:
                new_profile = {other_user: 0 for other_user in PeopleInvolvedInTransaction if other_user != user}
                self.individual_dicts[user] = new_profile
        if self.existing_friend and self.new_friend:
            for user in PeopleInvolvedInTransaction:
                for i in range(0, len(new_user)):
                    newUser = new_user[i]
                    if user != newUser:
                        if newUser not in self.individual_dicts[user]:
                            self.individual_dicts[user][newUser] = 0
        if self.existing_friend:
            otherUser = []
            for user in PeopleInvolvedInTransaction:
                if user != self.paidby:
                    otherUser.append(user)
                for i in range(0, len(otherUser)):
                    if otherUser[i] not in self.individual_dicts[self.paidby]:
                        self.individual_dicts[self.paidby][otherUser[i]] = 0
                    if self.paidby not in self.individual_dicts[otherUser[i]]:
                        self.individual_dicts[otherUser[i]][self.paidby] = 0

        # Split Unequally:
        if self.splitted_Unequally:
            for key, value in self.individual_dicts.items():
                PersonWhoPaidAmount = f"{key}"
                if PersonWhoPaidAmount == self.paidby:
                    for name in PeopleInvolvedInTransaction:
                        if name != self.paidby:
                            balance_PersonWhoPaid = self.individual_dicts[PersonWhoPaidAmount][name]
                            balance_otherUser = self.individual_dicts[name][PersonWhoPaidAmount]
                            if balance_otherUser == 0 and balance_PersonWhoPaid == 0:
                                self.individual_dicts[PersonWhoPaidAmount][name] += \
                                    self.currentTransactionSplittedUnequally[name]
                            elif balance_otherUser <= self.individual_dicts[PersonWhoPaidAmount][name]:
                                self.individual_dicts[name][PersonWhoPaidAmount] = 0
                                self.individual_dicts[PersonWhoPaidAmount][
                                    name] = balance_PersonWhoPaid + self.currentTransactionSplittedUnequally[name]
                            else:
                                if self.currentTransactionSplittedUnequally[name] < balance_otherUser:
                                    self.individual_dicts[name][PersonWhoPaidAmount] -= \
                                        self.currentTransactionSplittedUnequally[name]
                                else:
                                    self.individual_dicts[name][PersonWhoPaidAmount] = 0
                                    self.individual_dicts[PersonWhoPaidAmount][
                                        name] = self.currentTransactionSplittedUnequally[name] - balance_otherUser

        # Split Equally:
        else:
            # Update the transaction amounts
            for key, value in self.individual_dicts.items():
                PersonWhoPaidAmount = f"{key}"
                if PersonWhoPaidAmount == self.paidby:
                    for name in PeopleInvolvedInTransaction:
                        if name != self.paidby:
                            balance_PersonWhoPaid = self.individual_dicts[PersonWhoPaidAmount][name]
                            balance_otherUser = self.individual_dicts[name][PersonWhoPaidAmount]
                            if balance_otherUser == 0 and balance_PersonWhoPaid == 0:
                                self.individual_dicts[PersonWhoPaidAmount][name] += self.split_equal_amount
                            elif balance_otherUser <= self.split_equal_amount:
                                self.individual_dicts[name][PersonWhoPaidAmount] = 0
                                self.individual_dicts[PersonWhoPaidAmount][
                                    name] = self.split_equal_amount - balance_otherUser
                            else:
                                self.individual_dicts[name][PersonWhoPaidAmount] -= self.split_equal_amount

    def display_amount(self):
        '''
        To display the balances
        :return:
        '''
        print("\n§§§§§§§§§§§§§§§§  DASHBOARD  §§§§§§§§§§§§§§§§§ \n")
        for person, value in self.individual_dicts.items():
            print("---------------", "\033[1m", "To ", str(person).upper(), "\033[0m", " ----------------")
            # print(str(person).upper(), ":")
            d = self.individual_dicts[person]
            for name, amount in d.items():
                user = str(name)
                print("                   ", user.title(), f" owes  {amount:.2f}")
        # print("--------------------------------------------")


def main():
    Transaction = ExpenseSharingApp()
    while True:
        print("\n================ EXPENSE TRACKER ===================")
        print("\n 1. Add Expense")
        print(" 2. Close the App")
        while True:
            try:
                choice = int(input("    Please choose an option:  "))
                if 1 <= choice <= 2:
                    break
                else:
                    print("Error: Please enter a digit from 1 and 2.")
            except ValueError:
                print("Error: Please enter a valid digit.")

        if choice == 1:
            PeopleInvolved, new_user = Transaction.get_friends()
            Transaction.get_TotalExpense(PeopleInvolved)

            while True:
                try:
                    print("Do you want to split it \033[1m 'EQUALLY' \033[0m?", end="")
                    print(" Type \033[1m 'n' \033[0m to split \033[1m 'UNEQUALLY' \033[0m ")
                    response = input("y/n? : ").lower()
                    if response == "y" or response == "n":
                        break
                    else:
                        print("Error: Please enter 'y' or 'n'.")
                except ValueError:
                    print("Error: Please enter a valid response.")
            if response == "y":
                Transaction.split_equally(PeopleInvolved)
                Transaction.create_individualdict(PeopleInvolved, new_user)
                Transaction.display_amount()
            else:
                Transaction.split_unequally(PeopleInvolved, new_user)
                Transaction.create_individualdict(PeopleInvolved, new_user)
                Transaction.display_amount()
        elif choice == 2:
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
