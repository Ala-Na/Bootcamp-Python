class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount


class Bank(object):

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        acc_ori = self._obtain_id(origin)
        acc_dest = self._obtain_id(dest)
        if amount < 0:
           print("Amount to transfer can't be negative.")
           return False
        if not isinstance(amount, float):
            print("Amount to transfer must be a float.")
            return False
        if not _security_for_origin(acc_ori, amount) or not _security_for_dest(acc_dest):
            print("One of the account is corrupted. Can't process transfet.")
            return False
        acc_dest.transfer(amount)
        acc_ori.value -= amount
        return True        

    def _obtain_id(self, account):
        if isinstance(account, int):
            i = 0
            while i < len(self.account):
                if self.account[i].id == account:
                    return self.account[i]
                i += 1
        elif isinstance(account, str):
            i = 0
            while i < len(self.account):
                if self.account[i].name == account:
                    return self.account[i]
                i += 1
        print("Account not found.")
        return False


    def fix_account(self, account):
        acc = _obtain_id(account)
        if any(key.startswith("b") for key in account.__dict__):
            for key in account.__dict__:
                if key.startswith("b"):
                    acc.__dict__.pop(key)
        if (len(acc.__dict__) % 2 == 0):
            if any(key == "info" for key in account.__dict__):
                acc.__dict__.pop(key)
            else:
                acc._dict__['info'] = ""
        if not _check_corruption(acc):
            print("Can't fi account.")
            return False
        return True

    def _check_corruption(self, account):
        if (len(account.__dict__) % 2 == 0):
            return False
        if any(key.startswith("b") for key in account.__dict__):
            return False
        if not any(key.startswith("zip") for key in account.__dict__) and not any(key.startswith("addr") for key in account.__dict__):
            return False
        if not account.__dict__.has_key("name"):
            return False
        if not account.__dict__.has_key("id"):
            return False
        if not account.__dict__.has_key("value"):
            return False
        return True

    def _security_for_origin(self, account, amount):
        if not isinstance(account, Account):
            print("Must receive object of class Account.")
            return False
        if not self._check_corruption(account):
            print("Accounted is corrupted !")
            return False
        if account.value < amount:
            print("Not enough funds on account to process transfert.")
            return False
        return True

    def _security_for_dest(self, account):
        if not isinstance(account, Account):
            print("Must receive object of class Account.")
            return False
        if not self._check_corruption(account):
            print("Accounted is corrupted !")
            return False
        return True