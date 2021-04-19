if __name__=="project_9":
    class Update:
        def __init__(self):
            #show available items
            print("Available products and unit prises(Rs)")
            print("-"*110)
            print()
            with open("project_1.txt",'r') as bill:
                print(bill.read()) 
        def x(self):
            print()
            print("TO STOP UPDATING REPLACE THE ITEM WITH '@' MARK!")
            print("-"*110)
            with open("project_1.txt",'r') as bill:
                a=bill.readlines()
                b=list(map(lambda i:i.split(),a))
                list_items=[j[0] for j in b]
            #read stock bill to update price of items
            with open("project_3.txt",'r') as billStock:
                c=billStock.readlines()
                d=list(map(lambda i:i.split(),c))
            while True:
                item=input("ENTER ITEM: ")
                
                item=item.casefold()
                if len(item.split())==0:
                    print("-"*110)
                    print("You have not Entered Item! Try Again!")
                    print("-"*110)
                    print()
                    continue
                #end of the updating
                if item=="@":
                    print("="*110)
                    print("UPDAING IS SUCCESSFULL")
                    print("="*110)
                    print()
                    break
                if item not in list_items:
                    print("-"*110)
                    print(item,"is not here")
                    print("-"*110)
                    continue
                update_value=input("ENTER UPDATE PRISE: ")
                if not update_value.isdigit():
                    print("-"*110)
                    print("INVALID VALUE FOR UPDATE PRISE")
                    print("-"*110)
                    print()
                    continue
                if update_value=="0" or len(update_value.split())==0:
                    print("-"*110)
                    print("INVALID VALUE FOR UPDATE PRISE")
                    print("-"*110)
                    print()
                    continue
                j=0
                #update price of items
                for i in b:
                    a[j]=a[j].strip()
                    c[j]=c[j].strip()
                    if item==i[0]:
                        i[1]=update_value
                        d[j][1]=update_value
                        a[j]=item+" "*(55-len(item))+update_value
                        c[j]=item+" "*(55-len(item))+update_value+" "*(22-len(update_value))+d[j][2]
                    j+=1
            #write items with update prices    
            with open("project_1.txt",'w') as bill:
                a="\n".join(a)
                bill.write(a)
            #write items with update prices and counts
            with open("project_3.txt",'w') as bill:
                c="\n".join(c)
                bill.write(c)
