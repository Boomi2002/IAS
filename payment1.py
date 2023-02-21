import time
class Payment:
    @classmethod
    def paymentmethod(self):
        print("\t1.Direct Booking\n\t2.Credit/Debit Card\n\t3.Net Banking\n\t4.UPI Payment")
        pay=int(input("\n\tEnter Your Payment Method:"))
        
        if pay==1:
            print("_"*50,"!Booking Directly! Visit Again ","_"*50)
            
        
        elif pay==2:
            flag = True
            while flag:
                pin1=int(input("\tEnter your Card number:"))
                if pin1>1000000000000000 and pin1 < 9999999999999999:
                    time.sleep(6)
                cvv=int(input("\tEnter you cvv:"))
                if cvv == 123:
                    time.sleep(10)
                    print("\t\t\t\t\tPayment successfully!!!!!!!\n")
                    time.sleep(5)
                    print("_"*50,"!Thank you for Booking! Visit Again ","_"*50)
                    flag = False
                else:
                    print("\tInvalid pin try again")
        
        elif pay==3:
                flag = True          
                while flag:
                    num=input("\tEnter your Bank Type:")
                    time.sleep(6)
                    num=int(input("\tEnter your Transaction Details: "))
                    Payment.paymentmethod()
                    if num == 1234:
                        time.sleep(5)
                        print("_"*50,"!Thank you for Booking! Visit Again ","_"*50)
                        flag = False
                    else:
                        print("\tIncorrect Pin")
                        
        elif pay==4:
            flag = True          
            while flag:
                upi=int(input("\tEnter your UPI-ID:"))
                if upi==1234:
                    time.sleep(5)
                    print("_"*50,"!Thank you for Booking! Visit Again ","_"*50)
                    flag = False
                else:
                    print("\tInvalid UPI-PIN")
        time.sleep(5)
                    
