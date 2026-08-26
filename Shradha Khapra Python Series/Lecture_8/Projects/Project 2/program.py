class Banking:
    def __init__(self, acno, balance):
        self.acno = acno
        self.balance = balance

    def credit(self):
        crdbal = float(input("Amount to Credit:-"))
        self.balance += crdbal
        print("Balance credited", crdbal,"total amount is",self.balance)

    def debit(self):
        dbtbal = float(input("Amount to Debit:-"))
        self.balance -= dbtbal
        print("Baalance debited", dbtbal,"total balance is ", self.balance)

    def cekbal(self):
        print(self.balance)

B1 = Banking(123, 1000)
B1.credit()
B1.debit()
B1.cekbal()