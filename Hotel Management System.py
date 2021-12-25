#PRANAV MISHRA
#12 ARYABHATTA
#=====================================================
'''INTRODUCTION

This is a basic hotel management system.
This can perform:
1.      Input and storage of customer Information.
2.	Connection of MySQL with python.
3.	Updation of records using python.
4.	Input and storage of ward alloted.
5.	Updation of alloted ward.
6.	Generation of bill.'''
##########################PRELIMINARY CODE######################################


import mysql.connector 
mycon=mysql.connector.connect(host='localhost',user='root',passwd='',database='test')
mycur=mycon.cursor()
from datetime import date
#======================================================
def p1():
    l1=[]
    mycur.execute('select * from customer')
    r=mycur.fetchall()
    for row in r:
        for col in row:
            l1.append(col,)
            #print(l1)
    a=float(input('Enter cNo For Information Diplay: '))
    b=l1.index(a)
    i=int(b)
            #print(i)
    return(l1[i:i+8])
#======================================================
def Delete():
    a=input('Enter The cNo to Delete The Data')
    sql="DELETE FROM customer WHERE cNo={}".format(a)
    mycur.execute(sql)
    mycon.commit()
#======================================================
def UpdateN():
    a=input('Enter Which column to update: ')
    b=input('Enter New value: ')
    c=input('Enter cNo: ')
    st="UPDATE customer SET {}='{}' WHERE cNo={}".format(a,b,c)
    mycur.execute(st)
    mycon.commit()
#=======================================================
def UpdateN1():
    a=input('Enter Which column to update: ')
    b=input('Enter New value: ')
    c=input('Enter cNo: ')
    st="UPDATE room SET {}={} WHERE cno={}".format(a,b,c)
    mycur.execute(st)
    mycon.commit()
#======================================================
def roomE():
    l2=[]
    q1='select * from room'
    mycur.execute(q1)
    r=mycur.fetchall()
    for i in r:
        for j in i:
            l2.append(j)
            print(l2)
    a=int(input('Enter pNo: '))
    k=a
    d=0
    c=len(l2)
    for n in range(k*4+1,k*4+4,1):
        d=d+(l2[n])
        print(n)
        return d
    mycon.commit()
#======================================================
def roomIN():
    w1='select * from room'
    mycur.execute(w1)
    r1=mycur.fetchall()
#======================================================
def roomCHEK():
    a=['AC','nonAC','smoking']
    l1=[]
    q='select * from customer'
    mycur.execute(q)
    r=mycur.fetchall()
    for i in r:
        for j in i:
            l1.append(j)
#print(l1)
    a=int(input('Enter cno: '))
    d=8*a
    c=l1[d-1]
    return c
#======================================================
def Head():
    print('Turquoise Tree Hotel')
    print('Goa')
    print('123456')
    print('Ph:01124345656',' ','Mobile:09876543214')
    print('E-mail:Turquoisehotels123@gmail.com')
    print('Date:',date.today())
    return('-------------------------------------------------------')
#======================================================
def view():
    mycur.execute('select * from customer')
    records=mycur.fetchall()
    print('CNO\tNAME\tAGE\tCONTACT\t\tADDRESS\t\tOCCUPATION\tDOA\tROOM')
    for row in records:
        print()
        for col in row:
            print(col,end="\t")
    mycon.close()
#====================================================
def view1():
    mycur.execute('select * from room')
    records=mycur.fetchall()
    print('cno\tAC\tnonAC\Smoking')
    for row in records:
        print()
        for col in row:
            print(col,end="\t")
    mycon.close()
def passwd():
    while True:
        a=input("Enter username: ")
        if a=="pranav":
            while True:
                b=input("Enter password: ")
                if b=="cs123":
                    break
                else:
                    print("Wrong password")
                    continue
            break
        else:
            print("Wrong username")
            pass


        
#############################################MAIN CODE##########################################
passwd()
ch='y'
while ch=='y':
    print('WELCOME TO Turquoise Tree Hotel')
    print('-------------------------------')
    print('Customer Information-1')
    print('Customer room allocation-2')
    print('Billing-3')
    print('------------------------------')
    ai=int(input('Enter Your Choice--'))
    if ai==2:
        print('----------------------------')
        print("Let's alot room-1")
        print('Room updation-2')
        print('View room table-3')
        bi=int(input('Type in your choice--'))
        if bi==1:
            str1="INSERT INTO room values({},{},{},{})"
            print('Enter the following Record for room ALLOTMENT: ')
            c1=int(input('cno-'))
            c2=int(input('AC'))
            c3=int(input('nonAC-'))
            c4=int(input('Smoking-'))
            query=str1.format(c1,c2,c3,c4)
            mycur.execute(query)
            mycon.commit()
            mycur.execute('select * from room')
            records=mycur.fetchall()
            print('cno\tAC\tnonAC\tsmoking')
            for row in records:
                print()
                for col in row:
                    print(col,end="\t")
            mycon.close()
        if bi==2:
            q=UpdateN1()
            print(q)
        if bi==3:
            h=view1()
            print(h)
    if ai==1:
        print('To view info 1')
        print('To add info 2')
        print('To update info 3')
        aiii=int(input('Enter your choice: '))
        if aiii==1:
            d=view()
            print(d)
        if aiii==2:
            str1="INSERT INTO customer values({},'{}',{},{},\t'{}','{}','{}','{}')"
            print('Enter the following Record for Customer INFORMATION: ')
            c1=int(input('cno'))
            c2=str(input('Name'))
            c3=int(input('Age'))
            c4=int(input('Contact'))
            c5=str(input('Address'))
            c6=str(input('Occupation'))
            c7=str(input('Date of Arrival'))
            c8=str(input('Room'))
            query=str1.format(c1,c2,c3,c4,c5,c6,c7,c8)
            mycur.execute(query)
            mycon.commit()
            mycur.execute('select * from customer')
            records=mycur.fetchall()
            print('CNO\tNAME\tAGE\tCONTACT\t\tADDRESS\t\tOCCUPATION\tDOA\tROOM')
            for row in records:
                print()
                for col in row:
                    print(col,end="\t")
            mycon.close()
        if aiii==3:
            q=UpdateN()
            print(q)
    if ai==3:
        print("Let's Bill it UP")
        c1,c2,c3=input('Enter the Day of allocation space seperated yyyy/mm/dd').split()
        FD=date(int(c1),int(c2),int(c3))
        i1,i2,i3=input('Enter the DAY of leaving space seperated yyyy/mm/dd').split()
        SD=date(int(i1),int(i2),int(i3))
        c=(SD-FD).days
        a=roomCHEK()
        if a=='Smoking':
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('Customer INFORMATION')
            print('pNo--',g[0],' Name--',g[1])
            print('Age--',g[2],' Contact--',g[3])
            print('Address--',g[4],' Occupation--',g[5])
            print('DOA--',g[6],' Room--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('AC per day-4,237.28')
            print('NonAC per day-1,694.91')
            print('Smoking per day-1184.74')
            print('18% GST on each type of Room/Bed')
            print('----------------------------------------------------------')
            print('Number of days stayed',c)
            print('Room alloted',a)
            q=100*c
            print('Smoking room per day charges+GST+Hotel surcharges=100')
            print('Your Outstanding Bill is', q)
            st="Insert into bills values ({},{})".format(g[0],q)
            mycur.execute(st)
            mycon.commit()
        if a=='AC':
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('Customer INFORMATION')
            print('pNo--',g[0],' Name--',g[1])
            print('Age--',g[2],' Contact--',g[3])
            print('Address--',g[4],' Occupation--',g[5])
            print('DOA--',g[6],' room--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('AC per day-4,237.28')
            print('NonAC per day-1,694.91')
            print('Smoking per day-1184.74')
            print('18% GST on each type of Room/Bed')
            print('--------------------------------------------------------')
            print('Number of days stayed',c)
            print('Room alloted',a)
            q=5000*c
            print('AC room per day charges+GST+Hotel surcharges=5000')
            print('Your Outstanding Bill is', q)
            st="Insert into bills values ({},{})".format(g[0],q)
            mycur.execute(st)
            mycon.commit()
        if a=='nonAC':
            g=p1()
            print('------------------------------------------------------')
            b=Head()
            print(b)
            print('-------------------------------------------------------')
            print('Customer INFORMATION')
            print('pNo--',g[0],' Name--',g[1])
            print('Age--',g[2],' Contact--',g[3])
            print('Address--',g[4],' Occupation--',g[5])
            print('DOA--',g[6],' room--',g[7])
            print('-------------------------------------------------------')
            print('RECIEPT')
            print('--------------------------------------------------------')
            print('AC per day-4,237.28')
            print('NonAC per day-1,694.91')
            print('Smoking per day-1184.74')
            print('18% GST on each type of Room/Bed')
            print('-------------------------------------------------------')
            print('Number of days stayed',c)
            print('room alloted',a)
            q=2000*c
            print('nonAC room per day charges+GST+Hotel surcharges=2000')
            print('Your Outstanding Bill is', q)
            st="insert into bills values ({},{})".format(g[0],q)
            mycur.execute(st)
            mycon.commit()
            #print(c)
    print()
    ch=input('Want to continue(y/n): ')
print("Finished.......")



            
