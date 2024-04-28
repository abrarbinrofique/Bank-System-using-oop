from User import Customer,Admin
class Main:


    def __init__(self) -> None:
        pass
    def __repr__(self) -> str:
       flag=True 
       adm=True
       ctm=True
       custom=True
       while(flag==True):
           
          print( "Choose Your Service\n")
          print("1.Admin")
          print("2.Customer")
          print("3.exit")
          d=input("Your one: ")
          if (d=="1"):
              admin_name=input("print your name: ")
              admin_email=input("print your email: ")
              admin_address=input("print your address: ")
              ad=Admin(admin_name,admin_email,admin_address)
              while(adm):
                print(f"Welcome in Admin site Mr. {ad.name}")
                print("1.Add acountt")
                print("2.Remove an User account")
                print("3.Loan list of Bank")
                print("4.Total Loan of the bank")
                print("5.User Account List")
                print("6.view Bank Total Amount")
                print("7.Stop Loan")
                print("8.EXIT")
                a=(input('choose your option: '))
                if a=="1":
                   n=input("Customer name: ")
                   e=input("Customer email: ")
                   address=input("Customer address: ")
                   customer=Customer(n,e,address)
                   ad.add_acount(customer)
                elif a=="2":
                    id=int(input("Enter the account id you want to remove: "))
                    ad.remove_user(id)

                elif a=="3":
                    ad.check_loan_taker_list()

                elif a=="4":
                    ad.total_loan()

                elif a=="5":
                    ad.accounts()

                elif a=="6":
                    ad.check_balance()

                elif a=="7":
                    ad.stop_loan()
                    self.Loan_activation=False

                elif a=="8":
        
                    print("\n<<  Exit Admin Pannel  >>\n")
                    break
                else:
                   print("Wrong Input please Try again")

          elif d=="2":
            admin_name=input("print your name: ")
            admin_email=input("print your email: ")
            admin_address=input("print your address: ")
            custom=Customer(admin_name,admin_email,admin_address)
            while(ctm):
                print(f"Welcome in Customer Service Mr. {custom.name}")
                print("1.Create Account")
                print("2.Deposit Money in Your Account")
                print("3.Withdraw amount from bank")
                print("4.Check my account balance")
                print("5.Transfer money in other account")
                print("6.Take Loan from Bank")
                print("7.My transaction History")
                print("8.Exit System")
                c=input("Choose Your Option: ")
                if c=="1":
                    custom.create_account(custom)
                elif c=="2":
                    amount=int(input("Enter Your Deposit amount: "))
                    custom.deposit(amount)

                elif c=="3":
                    amount=int(input("Enter Your  amount for withdraw: "))
                    custom.withdrawal(amount)

                elif c=="4":
                    custom.check_balance()

                elif c=="5":
                    idd=int(input("Enter your  account No: "))
                    id=int(input("Enter account No: "))
                    amount=int(input("Amount You want to send: "))
                    custom.transfer(amount,id,idd)

                elif c=="6":
                    id=int(input("Enter your  account No: "))
                    amount=int(input("Amount You want to get Loan: "))
                    custom.take_loan(amount,id)

                elif c=="7":
                    custom.transaction()
                
                elif c=="8":
                    print("\n<<  Exit Customer Service  >>\n")
                   
                    break
                else:
                    print("Wrong Input please Try again")
         
          elif d=="3":
              
               print("\n<<  Exit System  >>\n")

          else:
             print("Your Input is wrong , please Try again")
              



            



                



                

              
                

                
                   







   



main=Main()
print(main)
