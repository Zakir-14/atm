class Atm:
    def __init__(self,CardHolderName,BankName,pinNumber,UPIpin):
        self.BankName = BankName
        self.pinNumber = pinNumber
        self.UPIpin = UPIpin
        self.CardHolderName = CardHolderName

    def showBalance(self):
        balance = self.UPIpin/2
        print(balance)
    
name = input("ENTER YOUR NAME :")
bankname = input("ENTER YOUR BANK NAME :")
pin = input("PLEASE ENTER YOUR PIN NUMBER :")
upi = input("PLEASE ENTER YOUR UPI NUMBER :")

Account = Atm(name,bankname,pin,upi)

print(name)
print(bankname)
print("You have sucessfully saved your account !")
print("1) CASH WITHDRAWAL")
print("2) VIEW BALANCE")
choose=input("HOW MAY I HELP YOU :")
#while (choose != '1') | (choose != '2'):
   # if usr_input == '1':
    #    search()
    #elif usr_input == '2':
     #   sys.exit()

if choose=="1" :
    pin1=input("PLEASE ENTER YOUR PIN :")
    if pin1==pin:
        money=input("ENTER THE REQUIRED MONEY :")
        print("Money withdrawal is sucessfully completed")
    else :
        print("INCORRECT PIN !!!")

elif choose=="2":
    upi1=input("PLEASE ENTER YOUR UPI NUMBER :")
    if upi1==upi:
        Account.showBalance()
    else :
        print("INCORRECT UPI !!!")



print("1) CASH WITHDRAWAL")
print("2) VIEW BALANCE")
choose=input("HOW MAY I HELP YOU :")       



    
