if __name__=="__main__":
    import project_6
    import project_12
    print(project_6.print_wel)
    list_receipt=[]
    list_cusInfor=[]
    list_cusInforAdd=[]
    value=0
    while True:
        import project_8
        def common():
            global list_receipt
            global list_cusInfor
            global list_cusInforAdd
            global value
            while True:
                print(project_6.print_1)
                sell_num=input("Enter Number: ")
                print("-"*110)
                #Enter to buy items System
                if sell_num=="1":
                    value=0
                    list_receipt,list_cusInfor=project_12.buy()
                    list_receipt.append(project_12.normal_bill(list_receipt))
                    break
                #Enter details of customers who Add items
                elif sell_num=="2":
                    value=2
                    import project_5
                    list_cusInforAdd=project_5.enter()
                    break
                #show Available Items
                elif sell_num=="3":
                    with open("project_1.txt",'r') as bill:
                        print("Item"+" "*49+"Unit Price")
                        print()
                        print(bill.read())
                        print("-"*110)
                    continue
                #go back
                elif sell_num=="4":
                    print("~"*48+"Back to Start"+"~"*49)
                    print()
                    break
                else:
                    print("Invalid Number! Please Try Again!")
                    print("-"*110)
                    print()
                    continue    
        input_num=""
        while True:
            print(project_6.print_infor)
            in_num=input("Enter Number: ")
            if in_num=="1" or in_num=="2" or in_num=="3":
                input_num=in_num
                break
            else:
                print("-"*110)
                print("Invalid Number! Try Again!")
                print("-"*110)
                continue
        print("-"*110)
        
        print()
        #Enter to Customer System
        if input_num=="1":
            print("="*42+"WELCOME TO CUSTOMER SYSTEM"+"="*42)
            common()
            continue
        #Enter to Seller System    
        elif input_num=="2":
            print("="*43+"WELCOME TO SELLER SYSTEM"+"="*43)
            print("-"*110)
            break_loop=0
            while True:
                print(project_6.print_seller)
                input_sell=input("Enter Number: ")
                print("-"*110)
                #view customers details
                if input_sell=="1":
                    print("~"*110)
                    print("YOU CAN TRY ONLY THREE TIMES TO ENTER THE PASSWORD!")
                    print("~"*110)
                    for i in range(3):
                        password=input("Enter Password: ")
                        #password>>>>  6737432986977
                        if password=="6737432986977":
                            print()
                            print(project_6.print_view)
                            print("-"*110)
                            while True:
                                int_num=input("Enter Number: ")
                                print("-"*110)
                                #show customers details who bought items
                                if int_num=="1":
                                    with open("custemer.txt",'r') as bill:
                                        print(bill.read())
                                    break
                                #show customers details who add items
                                elif int_num=="2":
                                    with open("project_2.txt",'r') as bill:
                                        print(bill.read())
                                    break
                                
                                else:
                                    print("-"*110)
                                    print("Invalid Number! Try Again!")
                                    print("-"*110)
                                    continue
                                    
                            break
                        else:
                            print("-"*110)
                            print("Wrong Password! Try Again!")
                            print("-"*110)
                            continue
                    else:
                        break_loop=1
                        break
                #Enter to Update System
                elif input_sell=="2":
                    import project_9
                    p1=project_9.Update()
                    p1.x()
                    break
                #Enter to Add item
                elif input_sell=="3":
                    if value==2:
                        p1=project_8.Add_item()
                        ax=p1.x()
                        list_receipt=list(ax)
                        list_receipt.append(project_12.normal_bill(ax))
                        break
                    else:
                        print("-"*110)
                        print("You haven't fill your details!")
                        print("Please Enter to Customer System and Next Enter to Attendance for Customers who Add Items!")
                        print("-"*110)
                        break
                #print receipt
                elif input_sell=="4":
                    if value==2:
                        list_cusInfor=list_cusInforAdd
                    
                    if len(list_receipt)==0:
                        print("-"*110)
                        print("You haven't dealt goods! Go Back!")
                        print("-"*110)
                        continue
                    
                    project_12.inf(list_cusInfor[0],list_cusInfor[1],list_cusInfor[2],list_cusInfor[3])
                    ax=list_receipt
                    project_12.receipt(ax)
                    break
                #show stock
                elif input_sell=="5":
                    print()
                    print(project_6.printStock)
                    print()
                    with open("project_3.txt",'r') as bill:
                        print(bill.read())
                    print("-"*110)
                    print()
                    break
                #go back
                elif input_sell=="6":
                    print("~"*48+"Back to Start"+"~"*49)
                    print()
                    break
                else:
                    print("-"*110)
                    print("Invalid Number! Try Again!")
                    print("-"*110)
                    continue                
            if break_loop==1:
                print("="*110)
                print("Shutdown System!")
                print("Stay Safe!")
                print("="*110)
                break
            else:
                continue
        #Shutdown System
        elif input_num=="3":
            print("="*110)
            print("Shutdown System!")
            print("Stay Safe!")
            print("="*110)
            break
        else:
            print("-"*110)
            print("Invalid Number! Try Again!")
            print("-"*110)
            continue
                    
