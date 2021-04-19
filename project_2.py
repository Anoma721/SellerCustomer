if __name__=="project_2":
    from datetime import datetime
    date=datetime.now()
    date=date.strftime("%m/%d/%Y,%H:%M:%S")
    class Custemor:
        def __init__(self,name,tele,date,address,id):
            self.name=name
            self.__tele=tele
            self.date=date
            self.address=address
            self.id=id
        #write customers details who bought items
        def newcustomer(self):
            with open("custemer.txt",'a') as bill:
                for i in self.name:
                    bill.write(i)
                bill.write(" "*(32-len(self.name)))
                bill.write(self.__tele+"\t"+self.date+"\t"+self.id+"\t"+self.address+"\n")
           
            print("-"*110)
            print()
                
    def enter():
        
        name=""
        while True:
            name=input("Enter your name: ")
            if len(name.split())==0:
                print()
                print("~"*110)
                print("You haven't Entered your Name. Please Enter your Name")
                print("~"*110)
                print()
                continue
            if len(name)>33:
                print()
                print("~"*110)
                print("Entered name is too long. Please Enter a short name")
                print("~"*110)
                print()
                continue
            break
        tele=""
        while True:
            tele=input("Enter your Phone No: ")
            if len(tele.split())==0:
                print()
                print("~"*110)
                print("You haven't Entered your phone number. Please Enter your phone number")
                print("~"*110)
                print()
                continue
            elif len(tele)!=10 or tele[0]!="0":
                print()
                print("~"*110)
                print("Entered number is incorrect. Please Enter correct number")
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
            address=input("Enter your Äddress: ")
            if len(address.split())==0:
                print()
                print("~"*110)
                print("You haven't entered your Address!. Please Enter your Address.")
                print("~"*110)
                print()
                continue
            break
        id_num=""
        while True:
            id_num=input("Enter your ID No: ")
            if len(id_num.split())==0:
                print()
                print("~"*110)
                print("You haven't entered your ID Number. Please Enter your ID Number")
                print("~"*110)
                print()
                continue
            elif len(id_num)!=10 and len(id_num)!=12:
                print()
                print("~"*110)
                print("You have entered a invalid ID number!. Please Enter a valid ID number.")
                print("~"*110)
                print()
                continue
            
            break
        p1=Custemor(name,tele,date,address,id_num)
        p1.newcustomer()
        return name,address,date,tele

