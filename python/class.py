class my_bank :
    name="SBI"
    num_of_user=0
    def __init__(self,name,amount):
        self.ac_name = name
        self.ac_balance = amount
        my_bank.num_of_user +=1
        print "WELOCOME TO THE SBI%s"%(self.ac_name)
        return
    def show_balance(self):
        print "your remaining balance is :%f"%(self.ac_balance)
        
        
    def withdraw(self,amount):
        if self.ac_balance > amount :
            self.ac_balance -= amount
            print "the with draw amount %f remaining balance in your account %f"%(amount,self.ac_balance)
        else :
            print "insufficient balance"
    def deposit(self,amount):
        self.ac_balance +=amount
        print "the deposit amount %f remaining balance in your account %f"%(amount,self.ac_balance)

        
class new_bank(my_bank):
    def __init__(self,name,amount,addr):
        my_bank.__init__(self,name,amount)
        self.addr=addr

    def withdraw(self,amount):
        if self.ac_balance > amount :
            self.ac_balance -= amount
            print " remaining balance in your account %f"%(self.ac_balance)
        else :
            print "insufficient balance"

    def __add__(self,other):
        self.balance +=other.balance
        other.ac_balance=()
        
