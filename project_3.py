if __name__=="project_3":
    from datetime import date
    today=date.today()

    class Main:
        def __init__(self):
            pass
        def n(self):
            print("+-------|"+"-"*60+"|--------------|------|-----------------+")     
    class Column(Main):
        def __init__(self,list_1):
            super().__init__()
            self.list_1=list_1
        #create bill with item,unit cost,....
        def addItem(self):
            
            for k in range(len(self.list_1)):
                
                list_3=[self.list_1[k][0],self.list_1[k][1],self.list_1[k][2]]
                amount_=str(int(list_3[1])*int(list_3[2]))
                if k<9:
                    print("|0"+str(k+1)+")"+" "*(5-len(str(k+1)))+"|",end="")
                else:
                    print("|"+str(k+1)+")"+" "*(6-len(str(k+1)))+"|",end="")
                print(list_3[0]+" "*(60-len(list_3[0]))+"|"+list_3[2]+" "*(14-len(list_3[2]))+"|"+list_3[1]+" "*(6-len(list_3[1]))+"|"+amount_+".00"+" "*(14-len(amount_))+"|")
                
                self.n()    
    class PrintBill(Main):
        def __init__(self):
            super().__init__()
            print("+"+"-"*108+"+")
            print("|"+" "*52+"SL  Shop"+" "*48+"|")
            self.n()
            
        def m(self):
            print("+"+"-"*108+"+")
            
        def row(self):
            print("|  S.No |"+" "*7+"Description"+" "*42+"|Unit cost(Rs.)|  Qty |      Amount(Rs.)|") 
            self.n() 
        
    class Total:
        def __init__(self,total):
            self.total=total
        def final(self):
            print("|"+" "*45+"THANK YOU! COME AGAIN!   Stay Safe!"+" "*28+"|")
            PrintBill.m(self) 
        #create bill with total   
        def total_func(self):
            print("|"+" "*79+"Total(Rs.) |"+str(self.total)+".00"+" "*(14-len(str(self.total)))+"|")
            print("+"+"-"*90+"|"+"-"*17+"+")
            self.final()
    #calculate paid amount
    def paid(total):
        amount_1=0
        while True:
            try:
                amount=int(input("Enter paid amount: "))
                amount_1+=amount
                print("-"*110)
            except ValueError:
                print()
                print("~"*110)
                print("Invalid Price")
                print("~"*110)
                print()
                continue
            else:
                #calculate the paid
                if amount_1<total:
                    total_1=total-amount_1
                    print("-"*110)
                    print("You have given ",amount_1,"Rs .....Please give ",total_1,"Rs")
                    print("-"*110)
                    print()
                    continue
                else:
                    print("-"*110)
                    print()
                    return amount_1

