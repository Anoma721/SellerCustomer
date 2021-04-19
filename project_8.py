if __name__=="project_8":
    import project_6
    class Seller_manage:
        def __init__(self):
            #open project_1 file to remove blanck lines if there are
            with open("project_1.txt",'r') as bill:
                self.list_withBlank=list(map(lambda x:x.split("\n"),bill.readlines()))
                self.list_withoutBlank=[line[0] for line in self.list_withBlank if line[0].strip()!="" ]
            #string that has not blanck lines   
            self.withoutBlank=""
            with open("project_1.txt",'w') as bill:
                for i in self.list_withoutBlank:
                    self.withoutBlank+=i+"\n"
                bill.write(self.withoutBlank)
            #print items and prices    
            print("Available products and unit prises(Rs)")
            print("-"*110)
            print(self.withoutBlank)
            print()
            #open project_3 file to remove blanck lines if there are
            with open("project_3.txt",'r') as bill:
                self.list_withBlank3=list(map(lambda x:x.split("\n"),bill.readlines()))
                self.list_withoutBlank3=[line[0] for line in self.list_withBlank3 if line[0].strip()!="" ]
            #string that has not blanck lines    
            self.withoutBlank3=""
            with open("project_3.txt",'w') as bill:
                for i in self.list_withoutBlank3:
                    self.withoutBlank3+=i+"\n"
                bill.write(self.withoutBlank3)
            #create dictionary >>>key=item >>>value=price and count    
            with open("project_3.txt",'r') as stockBill:
                self.stock=stockBill.readlines()
                self.stockKey=list(map(lambda x:(x.split())[0],self.stock))
                self.stockValue=list(map(lambda x:(x.split())[1:],self.stock))
                self.dictStock=dict(zip(self.stockKey,self.stockValue))
                
        def x(self):
            pass
    class BuyItems(Seller_manage):
        def __init__(self):
            super().__init__() 
              
        def x(self):
            self.dic={}
            total=0
            #create dict >>>key=item >>>value=price
            with open("project_1.txt",'r') as bill:
                list_item=bill.readlines()
                def dic_item(ke):
                    global dic
                    self.item=ke.split()
                    self.dic[self.item[0]]=self.item[1]
                a=list(map(dic_item,list_item)) 
            list_bill=[]
            print("-"*110)
            print("TO STOP THE PURCHASE OF GOODS ENTER '@' MARK!")
            print("-"*110)
            print()
            while True:
                item_1=input("ENTER ITEM AND COUNT OF ITEMS: ")
                 
                if item_1=="@":
                    #write  in project_1 file after buying items
                    with open("project_1.txt",'w') as bill:
                        new_list=list(map(lambda x,y:x+" "*(55-len(x))+y,self.dic.keys(),self.dic.values()))
                        newBill="\n".join(new_list)
                        bill.write(newBill)
                    #write  in project_3 file after buying items
                    with open("project_3.txt",'w') as bill:
                        new_listStock=list(map(lambda x,y:x+" "*(55-len(x))+(" "*(22-len(y[0]))).join(y),self.dictStock.keys(),self.dictStock.values()))
                        newBill="\n".join(new_listStock)
                        bill.write(newBill)
                    return  list_bill,total
                split_item=item_1.split()
                
                #if entered input has a mistake
                if len(split_item)<=1:
                    print("-"*110)
                    print("PLEASE ENTER ITEM AND COUNT CORRECTLY!")
                    print("-"*110)
                    print()
                    continue
                split_item[0]=split_item[0].casefold()
                if not split_item[1].isdigit():
                    print("-"*110)
                    print("PLEASE ENTER COUNT CORRECTLY!")
                    print("-"*110)
                    print()
                    continue
                #if item not in items list
                if split_item[0] not in self.dic.keys():
                    print("-"*110)
                    print(split_item[0]+" is not. Please Enter another item that you want")
                    print("-"*110)
                    print()
                    continue
                else:
                    #if count of items grater than count of items that have
                    if int(split_item[1])>int((self.dictStock[split_item[0]])[1]):
                        print("-"*110)
                        print("PLEASE ENTER ANOTHER COUNT OF ITEMS! WE HAVE ONLY",(self.dictStock[split_item[0]])[1],split_item[0])
                        print("-"*110)
                        print()
                        continue
                    else:
                        #calculate the total
                        split_item.append(self.dic[split_item[0]])
                        list_bill.append(split_item)
                        total+=int(self.dic[split_item[0]])*int(split_item[1])
                        #if count==count of items that have ,remove the item from the dict
                        if split_item[1]==(self.dictStock[split_item[0]])[1]:
                            self.dictStock.pop(split_item[0])
                            self.dic.pop(split_item[0])
                        else:
                            #calculate the count of items
                            self.dictStock[split_item[0]][1]=str(int(self.dictStock[split_item[0]][1])-int(split_item[1]))
                
                            
    class Add_item(Seller_manage):
        def __init__(self):
            super().__init__()
        def x(self):
            #list of items 
            self.itemList=[(x.split())[0] for x in self.list_withoutBlank]
            print("-"*110)
            print("TO STOP ADDING ITEMS REPLACE ITEM WITH '@' MARK")
            print("-"*110)
            print()
            list_add=[]
            total=0
            while True:
                list_new=[]
                new_item=input("ENTER ITEM: ")
                if len(new_item.split())==0:
                    print("-"*110)
                    print("You have not Entered Item! Try Again!")
                    print("-"*110)
                    print()
                    continue
                if new_item=="@":
                    with open("project_1.txt",'w') as bill:
                        new_list=list(map(lambda x,y:x+" "*(55-len(x))+y[0],self.dictStock.keys(),self.dictStock.values()))
                        newBill="\n".join(new_list)
                        bill.write(newBill)
                    #write  in project_3 file after Adding items
                    with open("project_3.txt",'w') as bill:
                        new_listStock=list(map(lambda x,y:x+" "*(55-len(x))+(" "*(22-len(y[0]))).join(y),self.dictStock.keys(),self.dictStock.values()))
                        newBill="\n".join(new_listStock)
                        bill.write(newBill)         
        
                            
                    return  list_add,total
                    
                price=input("ENTER PRISE OF THE ITEM: ")
                if not price.isdigit():
                    print("-"*110)
                    print("PLEASE ENTER PRICE CORRECTLY!")
                    print("-"*110)
                    print()
                    continue
                if len(price.split())==0:
                    print("-"*110)
                    print("You have not Entered Price! Try Again!")
                    print("-"*110)
                    print()
                    continue
                count=input("ENTER COUNT OF THE ITEM: ")
                if not count.isdigit():
                    print("-"*110)
                    print("PLEASE ENTER COUNT CORRECTLY!")
                    print("-"*110)
                    print()
                    continue
                if len(count.split())==0:
                    print("-"*110)
                    print("You have not Entered Count! Try Again!")
                    print("-"*110)
                    print()
                    continue
                #calculate total
                total+=int(price)*int(count)
                list_new.append(new_item.casefold())
                list_new.append(str(price))
                list_new.append(str(count))
                list_add.append(list_new)
                #if items is a new item
                if new_item.casefold() not in self.itemList:
                    #add new item
                    self.dictStock[new_item.casefold()]=[price,count]
                else:
                    #change the count
                    count=str(int((self.dictStock[new_item.casefold()])[1])+int(count))
                    (self.dictStock[new_item.casefold()])[1]=count
                    #if the original amount is different than the later amount, change the later price to original price
                    (self.dictStock[new_item.casefold()])[0]=price
                    
