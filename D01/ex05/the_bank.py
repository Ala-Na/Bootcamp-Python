class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount
        print("{} now have a balance of {} $.".format(self.name, self.value))


class Bank(object):
    '''The bank'''

    def __init__(self):
        self.account = []

    def __dir__(self):
        return self.account

    def add(self, account):
        '''Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        '''
        print("Tentative of registering new account into bank.")
        if not isinstance(account, Account):
            print("Account to add not of Account type.")
            return False
        for present_account in self.account:
            if (account.name == present_account.name):
                print("Account name {} already registered in bank.".format(account.name))
                return False
        self.account.append(account)
        print("Registered {} account succesfully.".format(account.name))
        return True

    def transfer(self, origin, dest, amount):
        '''Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        '''
        print("Transfer tentative of {} $ from {} to {}.".format(amount, origin, dest))
        acc_ori = self._obtain_id(origin)
        acc_dest = self._obtain_id(dest)
        if acc_ori is False or acc_dest is False:
            print("At least one of the account can't be found.")
            return False
        if not (isinstance(amount, float) or isinstance(amount, int)):
            print("Amount to transfer {} must be a float or an int.".format(amount))
            return False
        if amount < 0:
           print("Amount to transfer {} can't be negative.".format(amount))
           return False
        if not self._security_for_origin(acc_ori, amount) or not self._security_for_dest(acc_dest):
            print("One of the account is corrupted or doesn't have enough funds. Can't process transfer.")
            return False
        if not acc_dest.id == acc_ori.id:
            acc_dest.transfer(amount)
            acc_ori.transfer(-amount)
        else:
            print("Same account {}: balance stay the same.".format(acc_dest.name))
        return True

    def _obtain_id(self, account_name):
        if isinstance(account_name, str):
            i = 0
            while i < len(self.account):
                if self.account[i].name == account_name:
                    return self.account[i]
                i += 1
        print("Account {} not found.".format(account_name))
        return False

    def fix_account(self, name):
        '''fix account associated to name if corrupted
            @name: str(name) of the account
            @return True if success, False if an error occured
        '''
        print("Fixing tentative of {} account.".format(name))
        if not isinstance(name, str):
            print("{} is not a valid account name.".format(name))
            return False
        acc = self._obtain_id(name)
        if acc is False:
            return False
        if any(key.startswith("b") for key in acc.__dict__):
            for key in acc.__dict__:
                if key.startswith("b"):
                    acc.__dict__.pop(key)
        if (len(acc.__dict__) % 2 == 0):
            if any(k == "info" for k in acc.__dict__):
                acc.__dict__.pop('info')
            else:
                acc._dict__['info'] = ""
        if not self._check_corruption(acc):
            print("Can't fix account.")
            return False
        return True

    def _check_corruption(self, account):
        if (len(account.__dict__) % 2 == 0):
            return False
        if any(key.startswith("b") for key in account.__dict__):
            return False
        if not any(key.startswith("zip") for key in account.__dict__) and not any(key.startswith("addr") for key in account.__dict__):
            return False
        if not "name" in account.__dict__:
            return False
        if not "value" in account.__dict__:
            return False
        if not "id" in account.__dict__:
            return False
        if not isinstance(account.name, str):
            return False
        if not isinstance(account.id, int):
            return False
        if not (isinstance(account.value, int) or isinstance(account.value, float)):
            return False
        return True

    def _security_for_origin(self, account, amount):
        if not isinstance(account, Account):
            print("Must receive object of class Account.")
            return False
        if not self._check_corruption(account):
            print("Account {} is corrupted !".format(account.name))
            return False
        if account.value < amount:
            print("Not enough funds on account {} to process transfer.".format(account.name))
            return False
        return True

    def _security_for_dest(self, account):
        if not isinstance(account, Account):
            print("Must receive object of class Account.")
            return False
        if not self._check_corruption(account):
            print("Account {} is corrupted !".format(account.name))
            return False
        return True
