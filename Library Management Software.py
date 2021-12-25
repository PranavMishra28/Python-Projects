#To do:
#(1) Make it menu driven
# 

# Extracting information from the two files:

f = open('booklist-1.txt','r')
a = f.readlines()
booklist = []
for i in a: 
    i = i.rstrip('\n')
    b = i.split("#")
    booklist.append(b)
print("Booklist.txt: ")
print(booklist)
print()
f.close()

f1 = open('librarylog-2.txt','r')
a1 = f1.readlines()
librarylog = []
test = []
for i in a1:
    i = i.rstrip('\n')
    b1 = i.split("#")
    test.append(b1) 
librarylog.append(test)
print("Librarylog.txt: ")
print(librarylog)
f1.close()

# Questions:

#1 Can a student borrow a book on a particular day for a certain number of days (this depends on how many copies remain in the library, if the person has any pending fines or too many borrowed books and consider book restriction conditions:
c = 0
name = input("Enter the name of the book: ")
person = input("Enter your name: ")
length = int(input("Enter borrowing duration: "))
res = []
unres = []
def length_check(): #Checks to see if borrow duration is permissible 
    global c
    if name in res:
        if length < 7:
            c += 1
    elif name in unres:
        if length < 28:
            c += 1
            
    
def stock_check(name,booklist): #Checks if the book is in stock or not
    global c
    for i in booklist:
        if i[0] == name and int(i[1]) > 0:
            c += 1
            break

def fines(): #Calculates the fines for books in the restricted section only because Pranav forgot to add the unrestricted section as well
    global c
    fine = 0
    for i in librarylog:
        for j in i:
            days = int(i[1][1]) - 7
    if name in res:
        flag = True
    else:
        flag = False
            
    if days > 0 and flag == True:
        fine = 5*days
    elif days > 0 and flag == False:
        fine = 1*days
    elif days < 0:
        fine = 0
        c += 1
        

def reserved(): #Puts all books in the reserved section into a list
    for i in booklist:
        if i[2] == 'TRUE':
            res.append(i[0])
        else:
            unres.append(i[0])##l=[]
##for i in librarylog:
##    for j in i:
##        if j[0]=="B":

        
def borrowlimit(): #Checks to see if borrower has exceeded the borrow limit or not
    global c
    c2 = 0
    for i in librarylog:
        for j in i:
            if j[0] == 'B' and j[2] == person:
                c2 += 1
    if c2 < 3:
        c += 1
    else:
        c += 0

reserved()
length_check()
stock_check(name,booklist)
borrowlimit()
fines()

print("Counter: ",c)
if c == 4:
    print(person,"you can borrow",name)
else:
    print(person,"you cannot borrow",name)

#2 What are the most borrowed/popular books in the library (How many days were they borrowed vs not borrowed:
b_lst = []
t_lst = []
t1_lst = []
t2_lst = []
def popcheck(): #Tells you what the most popular book in the library is
    for i in librarylog:
        for j in i:
            if j[0] == "B":
                b_lst.append(j)
    for i in b_lst:
        t_lst.append(i[3])
    for i in t_lst:
        if i not in t1_lst:
            t1_lst.append(i)
    for i in t1_lst:
        t2_lst.append(t_lst.count(i))
    a = max(t2_lst)
    b = t1_lst[t2_lst.index(a)]
    print()
    print("The most popular book in the library is: ",b)
    
popcheck()

#3 Which books have the highest borrow ratio. You have to consider how many copies are there for this also . For example if a book has 10 copies from day 1 and 1 copy was always borrowed but another book has only 2 copies and 1 copy was borrowed half the number of days. The 2nd book has more borrow ratio. Basically for how much of the books were available vs how much they got borrowed:
##days_borrowed_for = []
##total_days = []
##total_copies = []
##bratio = []
##
##
##
##for i in librarylog:
##    for j in i:
##        if j[0] == 'B':
##            days_borrowed_for.append(j[4])
##        elif j[0] == 'R':
##            total_days.append(j[1])
##
##
##for i in booklist:
##    total_copies.append(i[1])
##
##print("Days borrowed for: ",days_borrowed_for)
##print("Total Days: ",total_days)
##print("Total Copies: ",total_copies)
##print(bratio)
##
##for i in range(0,len(days_borrowed_for)):
##    bratio.append(int(days_borrowed_for[i])/((int(total_days[i]))*(int(total_copies[i]))))
##
##s = max(bratio)
##s1 = bratio.index(s)
##
##print()
##print("highest borrow ratio: ",booklist[s1][0])

##
##l=[]
##for i in librarylog:
##    for j in i:
##        if j[0]=="B":
l1=[]
all_books=res+unres
num=0
nums=0

for i in all_books:#Counts the number of days each book has been borrowed for, then appends it along with the name of the book
    l=[]
    for j in librarylog:
        for k in j:
            if len(k) < 4:
                continue
            if k[3] == i and k[0] == "R":
                num+=int(k[1])
        l.append(i)
        l.append(num)
            
    print("l: ",l)
    l1.append(l)
    

x=[]
for i in all_books:#Counts the total days each book has been borrowed for, then inserts it 
    l=[]
    for j in librarylog:
        for k in j:
            if len(k) < 4:
                continue
            if k[3] == i and k[0] == "B":
                nums+=int(k[-1])
        x.append(nums)
#print("x: ",x)


for i in booklist:
    for j in i:
        number=i[1]
        for k in l1:
            if len(k)>=3:
                continue
            if k[0]==i[0]:
                k.append(int(number))
#print("L1 before: ",l1)


for i in x:
    for j in l1:
        if len(j) > 3:
            continue
        j.insert(2,i)

#print("L1 after: ",l1) #L1=[<name>,<number_of_days_kept_away_from_library>,<number_of_days_claimed_to_withold_book>,<number_of_copies>]
bratio=[]
for i in l1:
    c=int(i[1]/((i[2])*(i[3])))
    bratio.append(c)
    

            

#4 Be able to produce sorted lists of most borrowed books/ books with highest usage ratio:
index_list = []
for i in bratio:
    a = str(i) +'v'+str(booklist[bratio.index(i)][0])
    index_list.append(a)
index_list.sort()
print_list = []
for i in index_list:
    a = i.split('v')
    print_list.append(a[1])
print("Highest borrowed ratios in ascending order: ",print_list)

#5 What are the pending fines at the end of the log/at a specific day in the log:
resfine = 0
unresfine = 0
def t_pend_fines():
    global resfine,unresfine
    for i in librarylog:
        for j in i:
            if j[0] == "R" and j[3] in res:
                resdays = int(j[1]) - 7
                if resdays > 0:
                    resfine += resdays * 5
                elif resdays <= 0:
                    resfine += 0
            elif j[0] == "R" and j[3] in unres:
                unresdays = int(j[1]) - 28
                if unresdays > 0:
                    unresfine += unresdays * 1
                elif unresdays <= 0:
                    unresfine += 0
    print()
    print("Total fines for reserved books: ",resfine)
    print("Total fines for unreserved books: ",unresfine)
    print("Total fines for all books: ",resfine + unresfine)
    print()

reserved()
t_pend_fines()  

def userfine():
    print("Just for information fine for reserved books starts getting added after 7 days and unreserved books after 28 days")
    print()
    userdays = int(input("Enter number of days until which fines have to be calculated: "))
    newresfine = 0
    newunresfine = 0
    flag = 0
    for i in librarylog:
        for j in i:
            if j[0] == "R" and j[3] in res:
                flag = 1
            else:
                 flag = 2
            if flag == 1:
                if j[0] == "P":
                    if userdays > int(j[1]):
                        newresfine = resfine - int(j[3])
                    else:
                        newresfine = resfine  
            elif flag == 2:
                if j[0] == "P":
                    if userdays > int(j[1]):
                        newunresfine = unresfine - int(j[3])
                    else:
                        newunresfine = unresfine 
    print("Total fine on",userdays,":",newresfine + newunresfine)

userfine()


             
                 
               

    
    
    
    
    
    
    
    
    
    
    
    
# Check Q5. Answer not correct
#Will log follow the order BRAP; No
# Can the log have 2 consecutive P entries by 2 different people; yes
#For question 5 should we print cumulative fines or the marginal fine on that day; cumulative

    



    

    



