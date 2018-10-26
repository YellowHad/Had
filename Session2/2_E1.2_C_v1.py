if __name__ == '__main__':
    class BankAccount(object):
        def __init__(self, balance, account_owner):
            self.balance = balance
            self.account_owner = account_owner

        def __str__(self):
            return "Bank account('{}', '{}')".format(self.balance, self.account_owner)

    people = [BankAccount(1000, "abi"),
              BankAccount(23113, "didi"),
              BankAccount(148435, "bubi"),
              BankAccount(471920, "jani"),
              BankAccount(22135, "alexi")]

    rp = [ba.account_owner for ba in people if ba.balance > 30000]
    print(rp)

    for x in people:
        print(x.account_owner + " is rich!" if x.balance > 30000 else x.account_owner + " is not rich!")

    # Sorting people
    def get_balance(account):
        return account.balance

    sorted_accounts = sorted(people, key=get_balance, reverse=True)

    print(["{}".format(a) for a in sorted_accounts])