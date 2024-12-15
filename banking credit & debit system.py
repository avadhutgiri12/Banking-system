from random import randint

class account:
    print('This is a ABC Bank\nTo open Your Account In Our Bank.') 
    name=input('Enter Your First Name : ')
    mobileNo=int(input('Enter Your Mobile Number : '))
    numberacc=randint(11111,999999999)
    print(f'Your account is successfully created!\nThis is your account number  {numberacc}') 
    balance=10000

    def __init__(self):
        with open ('accountnumber.txt','a') as f:
            f.write(f'{self.numberacc}\n')

    def accountno(self ):

        self.accountNo = input("Please enter your account number : ")
        with open ('accountnumber.txt','r') as f:
            self.number=f.read()
            
            if self.accountNo in self.number:
                self.procedure()

            else:
                print('Enter a valid account number')
                print(self.number)

    def credit(self):
        amount=int(input("Enter amount to credit : "))
        self.balance += amount
        print(f" The Rs.{amount} was creadited succesfully in your bank account\nYour remaining balance is Rs.{self.getbalance()}")
    
    
    def debit(self):
        amount=int(input("Enter amount for debit : "))
        self.balance -= amount
        print(f" The Rs.{amount} was debited succesfully from your bank account\nYour remaining balance is Rs.{self.getbalance()}")

    def getbalance(self):
        # print(f"Your balance is Rs.{self.balance}")
        return self.balance

    # def checkdata(self):
    #     with open('data.txt') as f:
    #         data=f.read()
    #     if self.name.lower() in data :
    #         print(f'Hi {self.name.title()}')
    #         self.accountno()
 
    def mobileno(self): 

        if len(str(self.mobileNo)) == 10 :
            print('')
        
        else:
            print('Enter a Valid Number!!')
            exit()

    def procedure(self):
        print("Do You want debit or credit balance?")
        ans=input("")
        if ans.lower() == "yes":
            print("1.debit\n2.credit\nchoose 1 for debit and 2 for credit.")
            choice=int(input(""))
            if choice == 1:
                self.debit()

            elif choice == 2:
                self.credit()

        else:
            print("Thank you!")
            exit()
        



holder1=account()
holder1.mobileno()
holder1.accountno()
        

# class account:
#     name = input('Enter Your name :')
#     mobileno = int(input('Enter Your mobile number :'))
    
#     accbalance=10000

#     def lenofmobileno(self):
#         if len(str(self.mobileno)) == 10:
#             print("Your number is correct")
#         else:
#             print('Enter a valid number')
#             exit

#     def generateaccno(self):
#         if len (str(self.mobileno)) == 10:
#             Accountno = randint(11111,99999)
#             print(f'Your Account number is {Accountno}')

#     def writeinfileaccno(self):
#         with open('accountnumber.txt','a') as f:
#             f.write
        





# user=account()
# user.lenofmobileno()