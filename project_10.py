if __name__=="project_10":
    #create reciept
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
        def addItem(self):
            #create reciept with items,unit cost,....
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
        def m(self):
            print("+"+"-"*108+"+")
        def row(self):
            print("|  S.No |"+" "*7+"Description"+" "*42+"|Unit cost(Rs.)|  Qty |      Amount(Rs.)|") 
            self.n() 
        
    class Total:
        def __init__(self,total,amount):
            self.total=total
            self.amount=amount    
        def final(self):
            print("|"+" "*45+"THANK YOU! COME AGAIN!   Stay Safe!"+" "*28+"|")
            PrintBill.m(self)    
        def total_func(self):
            #create reciept with total,paid amount, remain
            self.list_total=["|"+" "*79+"Total(Rs.) |","|"+" "*80+"Paid(Rs.) |","|"+" "*78+"Remain(Rs.) |"]
            self.list_value=[str(self.total),str(self.amount),str(self.amount-self.total)]
            for i in range(3):
                print(self.list_total[i]+self.list_value[i]+".00"+" "*(14-len(self.list_value[i]))+"|")
                print("+"+"-"*90+"|"+"-"*17+"+") 
            self.final()




