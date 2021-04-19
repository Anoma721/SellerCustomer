if __name__=="project_5":
    from datetime import datetime
    date=datetime.now()
    date=date.strftime("%m/%d/%Y,%H:%M:%S")
    class Custemor:
        def __init__(self,name,tele,address,date):
            self.name=name
            self.__tele=tele
            self.date=date
            self.address=address
        #write customers details who add items
        def newcustomer(self):
            with open("project_2.txt",'a') as bill:
                
                bill.write(self.name+" "*(80-len(self.name)))
                bill.write(self.date+"     "+self.__tele+" "*4+self.address+"\n")
            
                
    def enter():
        
        name=""
        while True:
            name=input("Enter Company name: ")
            if len(name.split())==0:
                print()
                print("~"*110)
                print("You haven't Entered Name. Please Enter Company Name.")
                print("~"*110)
                print()
                continue
            
            break
        tele=""
        while True:
            tele=input("Enter Phone No: ")
            if len(tele.split())==0:
                print()
                print("~"*110)
                print("You haven't Entered Phone Number. Please Enter that.")
                print("~"*110)
                print()
                continue
            elif len(tele)!=10 or tele[0]!="0":
                print()
                print("~"*110)
                print("Entered number is incorrect. Please Enter Phone number.")
                print("~"*110)
                print()
                continue
            if not tele.isdigit():
                print()
                print("~"*110)
                print("Entered number is incorrect. Please Enter correct number")
                print("~"*110)
                print()
                continue
            break
        address=""
        while True:
            address=input("Enter Company Address: ")
            if len(address.split())==0:
                print()
                print("~"*110)
                print("You haven't entered Address. Please Enter Company Address")
                print("~"*110)
                print()
                continue
            
            break
        print("-"*110)
        print()
        p1=Custemor(name,tele,address,date)
        p1.newcustomer()
        return name,address,date,tele

