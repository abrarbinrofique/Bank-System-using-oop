from abc import ABC

class User(ABC):
    account_list={}
    Loan_list={}
    
    
   
    
    
    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address
        self.Loan_activation=True






class Customer(User):

    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)        
        self.balance=0
        self.account_no=None
        self.transaction_history=""
        
        
    

    def create_account(self,customer): #customer object for create account
        if self.account_list:
          last_key = next(reversed(self.account_list))
          self.account_no=last_key+1
          print(f"Congratulations You just add an account in your Bank,account no: {self.account_no}")
          self.account_list[self.account_no]=customer
        else:
         self.account_no=1
         
         print(f"Congratulations You just add an account in your Bank,account no: {self.account_no}")
         self.account_list[self.account_no]=customer

    

        

    
    def withdrawal(self,amount):
        if (amount>self.balance):
            print("WITHDRAWAL amount exceeded")
        
        else:
            self.balance-=amount
            print(f"you have withdraw taka {amount} now your balance is {self.balance}")
            
           
            self.transaction_history += f"\nyou have withdraw taka {amount} now your balance is {self.balance}"

    def deposit(self,amount):
        if(amount<=0):
           
            print("This amount is not acceptable")
            

        else:
            self.balance+=amount
            self.transaction_history+=f"\n you have deposit {amount} now your balance is {self.balance}"
            print (f"you have deposit {amount} now your balance is {self.balance} tk")
            Admin.Bank_amoount+=amount
            



    def check_balance(self):
        print(self.balance)



    def transfer(self,amount,recieve_account_no,send_account_no): #custom is the object of customer whome ricieve the money
        reciever=False
        acceptor=False
        for account_no,customer  in  self.account_list.items():
            if account_no==send_account_no:
                acceptor=True
            

        for account_no,customer  in  self.account_list.items():
            if account_no==recieve_account_no:
                reciver=True
                if reciver==True and acceptor==True:
                     if(amount<self.balance):
                         customer.balance+=amount
                         self.balance-=amount
                         self.transaction_history+=(f"\n you send taka {amount} to {recieve_account_no}")
                         print(f"Congratulations!{customer.name} recieves tk {amount} from you,your Current balance {self.balance}")
                     else:
                         print("you dont have enough Money in account")
                
                
                else:
                    print("Account doesnot exist")


    def take_loan(self,amount,acount_no):
        if self.Loan_activation==True:
          loan_reciever=False
          for account in self.Loan_list:
            if account==acount_no:
                loan_reciever=True
                if self.Loan_list[self.account_no]==1:
                    self.Loan_list[self.account_no]=2
                    Admin.Loan_amount+=amount
                
                else:
                  print("Your already get two loans from us")

           
          if loan_reciever==False:
              self.Loan_list[self.account_no]=1
              Admin.Loan_amount+=amount
     

            
        else:
            print("our loan service is off now")



    
    def transaction(self):
        print(self.transaction_history)
 




class Admin(User):
    Loan_amount=0
    Bank_amoount=0
    
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)


    def add_acount(self,customer):
        if self.account_list:
          last_key = next(reversed(self.account_list))
          self.account_no=last_key+1
          print(f"Congratulations You just add an account in your Bank,account no: {self.account_no}")
          self.account_list[self.account_no]=customer
        else:
         self.account_no=1
         
         print(f"Congratulations You just add an account in your Bank,account no: {self.account_no}")
         self.account_list[self.account_no]=customer


    def remove_user(self,account_numb):
          account_list_copy=self.account_list.copy()
          for account_no,customer  in  account_list_copy.items():
              if account_no==account_numb:
                  del self.account_list[account_no]
                  print(f"{account_no} is remove from User List")
        

    def stop_loan(self):
        self.Loan_activation=False


    def check_loan_taker_list(self):
        print("Acoount no \t Loan times")
        for account,loan in self.Loan_list.items():
            print(f'{account} \t\t {loan}')

    
    def total_loan(self):
        print(self.Loan_amount)

    
    def check_balance(self):
        print(self.Bank_amoount)


    def accounts(self):
        print("Account no \t customer name \t email \t   address")
        for account_no,customer  in  self.account_list.items():
            print(f"{account_no}\t\t {customer.name}\t\t{customer.email}\t\t{customer.address}" )

       

