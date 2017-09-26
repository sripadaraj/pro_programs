new_acc=input("To create a new account press 1: ")
if new_acc ==1:
    acc_name=raw_input("Enter the name: ")
    acc_amount=raw_input("Enter the amount: ")
    acc_noo=raw_input("Enter the account number: ")


    a=open("old.txt","r+")
    a.seek(0,2)
    a.write("%s %s %s\n"%(acc_name,acc_amount,acc_noo))

############################################
######### To count the line number
################################################
f=open("old.txt","r")
f.seek(0,0)
line_no=0
acc_no=raw_input("Enter a Account number: ")
for line in f.readlines():
    line_no += 1
    if line.find(acc_no) >=0:
        a=line_no
#######################################################################
  #To the line data collected      
###########################################################
f=open("old.txt","r")
f.seek(0,0)
fd=f.readlines()
##print fd[(a-1)]
line=fd[a-1]     
##print line
##print type(line)
x=line.split()
##print x
#############################################
    #Input
###############################################################

acc_name=x[0]#raw_input('Enter account holder name: ')#### each index for name amount and acc_no
amount=int(x[1])#input('Enter amount:')
acc_no=int(x[2])#input('enter acc no:')
####################################################################3
       ## Bank 
#######################################################################
class my_bank:
    name='SBI'
    num_user=0
    def __init__(self,name,amount):
        self.ac_name = name
        self.ac_balance = amount
        my_bank.num_user += 1
        print 'well come to %s branch %s'%(my_bank.name,acc_name)
        return
    def show_balance(self):
        print '%s ur balance is %d'%(acc_name,self.ac_balance)

    def deposite(self,amount):
        if amount > 0 :
            self.ac_balance += amount
            print '%s remaning balance %d'%(acc_name,self.ac_balance)

    def withdraw(self,amount):
        if self.ac_balance > amount :
            self.ac_balance -= amount
            print '%s remaning balance %d'%(acc_name,self.ac_balance)
        else:
            print '%s insuff balance %d'%(acc_name,self.ac_balance)

    def __del__(self):
        my_bank.num_user -= 1

##a=my_bank('ggg',1000)
##a.show_balance()


_1=my_bank(('%s')%(acc_name),amount)
##_1.show_balance()

##
show_balance=input("To see balance 1: ")
withdraw=input("To withdraw press 2: ")
deposite=input("To deposite press 3: ")

if show_balance==1:
     _1.show_balance()

if withdraw==2:
    amount=input("Enter the withdraw amount: ")
    _1.withdraw(amount)

if deposite==3:
   amount=input("Enter the deposite amount: ")
   _1.deposite(amount)


vv = getattr(_1,'ac_balance')
##print vv
oo=str(vv)
##print oo
##print type(oo)
##print x
##print type(x)
x[1]=oo
##print x[1]
##print type(x[1])
##print x




st1=' '
cc=st1.join(x)
##print cc
fd[(a-1)]=cc
mm=fd[(a-1)]
##print "fd = ", fd




st2='\n'
gg=st2.join(fd)
##print "gg = ", gg

f=open('old.txt','w+')
f.write(gg)
f.seek(0,0)
f_data=f.read()
##print f_data

f=open('New.txt','w+')
f.write(gg)
f.seek(0,0)
fd=f.read()



