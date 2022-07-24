from the_bank import Account, Bank

if __name__ == "__main__":

    print("Subject tests:\n-------------")

    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))

    print("")

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('\033[91mFailed\033[0m')
        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

    print("")


    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("\nMore tests:\n-----------")

    if bank.transfer('William John', 'Smith Jane', 7000.0) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer('William John', 'Smith Jane', -1000.0) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer('William John', 'Smith Jane', "lol") is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer('William John', 'Smith Jane', 1) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.add(Account('William John')) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.add('William John') is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer('William John', 1, 1) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer(3, 1, 1) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer(1, 1, 1) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    bank.fix_account(1)

    print("")

    bank.fix_account('Existpa')

    print("")

    if bank.add(Account('Account Corrupted')) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')

    print("")

    if bank.transfer('Account Corrupted', 'Smith Jane', 0.0) is False:
        print('\033[91mFailed\033[0m')
    else:
        print('\033[92mSuccess\033[0m')
    bank.fix_account('Account Corrupted')
