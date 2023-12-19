class Bank:
    Bank_name='SBI'
    IFSC='SBINO0123'
    Branch_name='Marathalli'
    ROI=0.06
    def __init__(self,name,accno,mno,Bal,pin):
        self.name=name
        self.accno=accno
        self.mno=mno
        self.Bal=Bal
        self.pin=pin
        print(name,accno,mno,Bal,pin)
    @staticmethod
    def validation():
        return int(input("Enter 4digit pin:"))
    def deposite(self):
        if self.pin==self.validation():
            amount=int(input("enter amount:"))
            self.Bal+=amount
            print("amount deposited successfully: ")
            print(self.Bal)
        else:
            print("incorrect pin")
    def withdraw(self):
        if self.pin==self.validation():
            amount=int(input("enter amount:"))
            if(amount<=self.Bal):
                self.Bal-=amount
                print("amount debited successfully")
            else:
                print("balance insufficient")
        else:
            print("incorrect pin")
    def checkbal(self):
        if self.pin==self.validation():
            print(self.Bal)
        else:
            print("incorrect pin")
    @classmethod
    def changeROI(cls):
        cls.ROI=float(input("enter new ROI"))
    def changepin(self):
        if self.pin==self.validation():
            pin1=int(input("enter new pin"))
            pin2=int(input("enter new pin"))
            if(pin1==pin2):
                self.pin=pin1
                print("pin changed successfully")
            else:
                print("pin not matching")
        else:
            print("incorrect pin")
pin1=Bank("Arun",123456789101,8249181431,10000,1234)
pin2=Bank("Kumar",123456789111,8249181432,12000,4321)
pin1.deposite()
pin1.withdraw()

