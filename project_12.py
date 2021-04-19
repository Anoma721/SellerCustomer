if __name__=="project_12":
    def inf(name,address,date,phone):
        #print sellers details
        print()
        print("="*110)
        print("|"+" "*52+"SL  Shop"+" "*48+"|")
        print("|"+" "*44+"Address: No 25, Kensingtan Garden, Colombo 04                   |")
        print("|"+" "*50+"Phone: **********"+" "*41+"|")
        print("|"+" "*50+"Email: ********@gmail.com                                 |")
        print("|"+" "*108+"|")
        print("|"+" "*108+"|")
        #print customers details
        print("|    BILLED TO")
        print("|    Date/Time: ",date)
        print("|    Client Name/Name of the Company: ",name)
        print("|    Address: ",address)
        print("|    Phone:  "+phone+" "*86+"|")
        print("|"+" "*108+"|")
        print("="*110)
    def buy():
        import project_8
        import project_2
        callEnterFunc=project_2.enter()
        p1=project_8.BuyItems()
        ax=list(p1.x())
        #return customers details and buy items & total of items
        return ax,callEnterFunc
    #print reciept
    def receipt(ax):
        import project_10
        p1=project_10.PrintBill()
        p1.row()
        p2=project_10.Column(ax[0])
        p2.addItem()
        p3=project_10.Total(ax[1],ax[2])
        p3.total_func()
    #show bill
    def normal_bill(ax):
        import project_3
        p1=project_3.PrintBill()
        p1.row()
        p2=project_3.Column(ax[0])
        p2.addItem()
        p3=project_3.Total(ax[1])
        p3.total_func()
        paidAmount=project_3.paid(ax[1])
        #return paid amount that customer was paid
        return paidAmount
        
