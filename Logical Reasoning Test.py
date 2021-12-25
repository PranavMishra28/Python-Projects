user=input('NAME')
school=bool(input('Are you in school? (True/False)'))
if school==True:
    var=bool(input('Are you in class 12? (True/False)'))
print('''WELCOME TO THE APTITUDE TEST!
DEVELOPED BY: LORD PRANAV MISHRA
THIS TEST WILL TEST YOUR APTITUDE IN FOUR CATEGORIES:

1) LOGICAL REASONING
2) NUMERICAL ABILITY
3) SCIENTIFIC APTITUDE
4) INFORMATIC APTITUDE

UPON COMPLETION OF THE TEST, YOUR SCORES FROM EACH TEST WOULD BE DISPLAYED AND A RECOMMENDED STREAM/COLLEGE WOULD BE SHOWN

TYPE 'yes' TO BEGIN THE TEST
''')
ch='yes'
ch=input('BEGIN?')
while ch=='yes':
    ############################################################################################logical##############################################################################################
        l1=[]
        print("LOGICAL REASONING")
        print('''
    Q1 - What is next in the sequence?
    BXJ,ETL,HPN,KLP,_
    a - NHR
    b - MHQ
    c - MIP
    d - none
    ''')
        answer=input().lower()
        if answer=='a':
              print('correct')
              l1.append(1)
        else:
              print('incorrect')
              l1.append(0)
        print('''
    Q2 - Rahul told Anand, "Yesterday I defeated the only brother of the daughter of my grandmother." Whom did Rahul defeat?
    a - Son
    b - Brother
    c - Father
    d - Cousin
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q3 - In a certain code, '467' means 'leaves are green' ; '485' means 'green is good' and '639' means 'they are playing'. Which digit stands for 'leaves' in that code?
    a - 4
    b - 7
    c - 6
    d - 3
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q4 - What can you conclude from the given statements :

    Some cats are dogs

    Some dogs are rats
    a - Some dogs are rats
    b - Some dogs are not rats
    c - All cats are dogs
    d - All cats are not dogs
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q5 - Find the letter in the 9th position when the alphabets are written in reverse alphabetical order from the right.
    a - M
    b - J
    c - I
    d - K
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q6 - Tina walks 4 km towards north, turns right and walks 5 km. Then he turns towards south and walks 2 km. Again he takes a turn towards west walks 3 km and stops for a while. Then he further walks 2 km in the same direction. What is the distance of Tina from starting point? 
    a - 2 km
    b - 8 km
    c - 16 km
    d - 4 km
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q7 - If rose is called popy, popy is called lily, lily is called lotus and lotus is called glandiola, which is the king of flowers?
    a - Rose
    b - Glandiola
    c - Popy
    d - Lily
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q8 - Pointing to a gentleman, Deepak said, "His only brother is the father of my daughter's father." How is the gentleman related to Deepak?
    a - Father
    b - Brother
    c - Uncle
    d - None
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q9 - What can you conclude from the given statement :

    All ants are tigers
    a - Some tigers are ants
    b - All tigers are ants
    c - All tigers are not ants
    d - None
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q10 - What should be the third step of the following input?
    Input: 239 123 58 361 495 37
    a - 495 37 361 239 123 58
    b - 495 37 361 123 239 58
    c - 495 37 58 123 361 239
    d - 495 37 361 239 123 58
    ''')
        answer=input().lower()
        if answer=='d':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Thank you for completing the Logical Reasoning Test
    your score is
    ''')
        logical=sum(l1)
        print(logical,'out of 10')
    ###################################################################################################logical end numerical begin################################################################################
        Numerical=[]
        print('NUMERICAL')
        print('''
    Q1 - An amount is to be distributed among A,B and C in the ratio 3:5:7. If B's share is 3000, then what is the difference between A and C's share
    a- 2400
    b- 2500
    c- 1800
    d- 4200
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            Numerical.append(0)
            print('incorrect')
        print('''
    Q2- The ages of two brothers are in the ratio 7:6 If the age of the older brother is 15 years and 9 months, then what is the age of the younger brother?
    a- 12 years and 6 months
    b- 13 years and 9 months
    c- 13 years and 6 months
    d- 12 years and 9 months
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q3- Find a number which is greater than 18 in the same ratio as 11 is greater than 9.
    a- 12
    b- 22
    c- 32
    d- 42
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q4- The ratio 6 1/2:5:2 is equal to
    a- 5:4
    b- 6:5
    c- 8:7
    d- 13:1
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q5- What number must be subtracted from 22, 41, 60 and 117 so that the remainders may be proportional?
    a- 2
    b- 3
    c- 4
    d- 5
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q6- A 2 digit number is 4 times the sum of the digits Find the ratio of digits in units place to tens place
    a- 2:3
    b- 3:2
    c- 2:1
    d- 1:2
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q7- 60000 is divided among A,B and C so that if 40, 80 and 120 rupees is taken from their shares respectively,
    they will have money in the ratio 3:4:5. The share of B is
    a- 2080
    b- 2000
    c- 1920
    d- 2100
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q8- complete the identity (a+b)*2
    a- a*2 + b*2 +2AB
    b- AB*2 + AB
    c- 2AB + b*2
    d- AB + a*2
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q9- What is the correct Pythagores theorem C being the longest side
    a- A*2 + B*2= C*2
    b- AB*2 =C*2
    c- A + B = C*2
    d- None of these
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q10- Which number should be added to the antecedent and consequent of 7/11 so, That the ratio becomes 3/4
    a- 3
    b- 5
    c- 7
    d- 9
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Thank you for the completing the Numerical Test
    your score is
    ''')
        num=sum(Numerical)
        print(num,'out of 10')
    #############################################################################Numerical end scientific begin###################################################################################################
        sc=[]
        print('SCIENTIFIC')
        print('''
    Q1 - Knot is a unit of?
    a- speed
    b- time
    c- depth
    d- distance
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q2 - Ohm is used to measure?
    a- current
    b- voltage
    c- resistance
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q3 - What do we call the minimum velocity with which a body must be projected up, so as to enable it to just overcome the gravitational pull?
    a- orbital velocity
    b- escape velocity
    c- gravitational velocity
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q4 - Who is the author of 'A Brief History of Time?
    a- Stephen Hawking
    b- Richard Feynman
    c- Albert Einstein
    d- Erwin Schrodinger
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q5 - Amalgam is a term used for an alloy of a metal with?
    a- mercury
    b- gold
    c- copper
    d- tin
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q6 - LPG is a hydrocarbon containing a mixture of?
    a- ethane and butane
    b- methane and butane
    c- propane and butane
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q7 - Which of the following substances undergo sublimation on heating?
    a- camphor
    b- iodine
    c- napthalene
    d- all of the above
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q8 - BowmanÃ¢â‚¬â„¢s CapsuleÃ¢â‚¬â„¢ works as a part of the functional unit of which among the following human physiological system?
    a- circulatory system
    b- respiratory system
    c- excretory system
    d- digestive system
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q9 - The bacterium Ã¢â‚¬ËœEscherichia coliÃ¢â‚¬â„¢ is found mainly in:?
    a- root Nodules of leguminous plants
    b- human instestine
    c- human mouth
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q10 - Anemophily is pollination by?
    a- wind
    b- water
    c- insects
    d- none
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Thank you for the completing the Scientific Test
    your score is
    ''')
        science=sum(sc)
        print(science,'out of 10')
    ##########################################################################scientific end informatic begin######################################################################################
        xD=[]
        print('Informatic')
        print('''
    Q1- How many types of data extractions are there
    a- 1
    b- 2
    c- 3
    d- 4
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q2- What is the data format you prefer for informatica server
    a- ASCII
    b- EBCDIC
    c- UNICODE
    d- Decimal
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q3- An informatica variable contains
    a- Starvalue/end value
    b- start value/current value
    c- start value
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q4- Which of the following are active Transformations?
    a- Sorter
    b- Expression
    c- Normalizer
    d- Filter
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q5- What manages the scheduling and execution of workflows?
    a- Informatica server
    b- Repository Server
    c- Designer
    d- Monitor
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q6- Which Client component can be used for creating Repository?
    a- Manager
    b- Designer
    c- Worflow Manager
    d- Repository server Admin Console
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q7- Can an output port be used in the editable area of widgets
    a- Yes
    b- No
    c- Depends
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q8- Joiner Can?
    a- Join any two heterogeneous sources
    b- same data base
    c- Join only flatfiles
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q9- Who made Windows
    a- Steve Jobs
    b- Harvey Clint
    c- Larry Page
    d- Bill Gates
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q10- Which component gets metadata from Repository
    a- informatica server
    b- Informatica workflow Designer
    c- Informatica designer
    d- Informatica repository Server
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Thank you for completing the Informatic test
    your score is
    ''')
        mess=sum(xD)
        print(mess,'Out of 10')
        break
    ################################################END OF TEST###############################################################
print('')
print('FINAL SCORES FOR',user,'(OUT OF 10)')
print("")
print('LOGICAL REASONING',logical)
print('NUMERICAL ABILITY',num)
print('SCIENTIFIC REASONING',science)
print('INFROMATIC APTITUDE',mess)
print('')
if logical+num+science+mess>30:
    if school==True:
        print('OPT FOR PCM WITH COMPUTER SCIENCE!')
    else:
        print('LOOK INTO GOOD ENGINEERING COLLEGES SUCH AS IITs/NIITs')
elif logical+num>science+mess:
    if school==True:
        print('OPT FOR COMMERCE!')
    else:
        print('LOOK INTO GOOD COLLEGES FOR COMMERCE, SUCH AS IIM')
elif logical+science>logical+num:
    if school==True:
        print('OPT FOR PCB!')
    else:
        print('LOOK INTO GOOD MEDICAL COLLEGES SUCH AS AIIMS')
elif logical+mess>15:
    if school==True:
        print('WORK ON YOUR IT SKILLS!')
    else:
        print('LOOK INTO GOOD IT COURSES SUCH AS THOSE OFFERED BY ABROAD UNIVERSITIES')
else:
    if school==True:
        print('OPT FOR HUMANITIES')
    else:
        print('LOOK INTO GOOD ARTS COLLEGES SUCH AS ST.STEPHENS')
###########################################END MADE BY ARYAN AND YASH##########################################################################################user=input('NAME')
school=bool(input('Are you in school? (True/False'))
if school==True:
    var=bool(input('Are you in class 12? (True/False'))
print('''WELCOME TO THE APTITUDE TEST!
DEVELOPED BY: ARYAN KAUSHIK AND YASH SRIVASTAVA
THIS TEST WILL TEST YOUR APTITUDE IN FOUR CATEGORIES:

1) LOGICAL REASONING
2) NUMERICAL ABILITY
3) SCIENTIFIC APTITUDE
4) INFORMATIC APTITUDE

UPON COMPLETION OF THE TEST, YOUR SCORES FROM EACH TEST WOULD BE DISPLAYED AND A RECOMMENDED STREAM/COLLEGE WOULD BE SHOWN

TYPE 'yes' TO BEGIN THE TEST
''')
ch='yes'
ch=input('BEGIN?')
while ch=='yes':
    ############################################################################################logical##############################################################################################
        l1=[]
        print("LOGICAL REASONING")
        print('''
    Q1 - What is next in the sequence?
    BXJ,ETL,HPN,KLP,_
    a - NHR
    b - MHQ
    c - MIP
    d - none
    ''')
        answer=input().lower()
        if answer=='a':
              print('correct')
              l1.append(1)
        else:
              print('incorrect')
              l1.append(0)
        print('''
    Q2 - Rahul told Anand, "Yesterday I defeated the only brother of the daughter of my grandmother." Whom did Rahul defeat?
    a - Son
    b - Brother
    c - Father
    d - Cousin
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q3 - In a certain code, '467' means 'leaves are green' ; '485' means 'green is good' and '639' means 'they are playing'. Which digit stands for 'leaves' in that code?
    a - 4
    b - 7
    c - 6
    d - 3
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q4 - What can you conclude from the given statements :

    Some cats are dogs

    Some dogs are rats
    a - Some dogs are rats
    b - Some dogs are not rats
    c - All cats are dogs
    d - All cats are not dogs
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q5 - Find the letter in the 9th position when the alphabets are written in reverse alphabetical order from the right.
    a - M
    b - J
    c - I
    d - K
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q6 - Tina walks 4 km towards north, turns right and walks 5 km. Then he turns towards south and walks 2 km. Again he takes a turn towards west walks 3 km and stops for a while. Then he further walks 2 km in the same direction. What is the distance of Tina from starting point? 
    a - 2 km
    b - 8 km
    c - 16 km
    d - 4 km
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q7 - If rose is called popy, popy is called lily, lily is called lotus and lotus is called glandiola, which is the king of flowers?
    a - Rose
    b - Glandiola
    c - Popy
    d - Lily
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q8 - Pointing to a gentleman, Deepak said, "His only brother is the father of my daughter's father." How is the gentleman related to Deepak?
    a - Father
    b - Brother
    c - Uncle
    d - None
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q9 - What can you conclude from the given statement :

    All ants are tigers
    a - Some tigers are ants
    b - All tigers are ants
    c - All tigers are not ants
    d - None
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q10 - What should be the third step of the following input?
    Input: 239 123 58 361 495 37
    a - 495 37 361 239 123 58
    b - 495 37 361 123 239 58
    c - 495 37 58 123 361 239
    d - 495 37 361 239 123 58
    ''')
        answer=input().lower()
        if answer=='d':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Thank you for completing the Logical Reasoning Test
    your score is
    ''')
        logical=sum(l1)
        print(logical,'out of 10')
    ###################################################################################################logical end numerical begin################################################################################
        Numerical=[]
        print('NUMERICAL')
        print('''
    Q1 - An amount is to be distributed among A,B and C in the ratio 3:5:7. If B's share is 3000, then what is the difference between A and C's share
    a- 2400
    b- 2500
    c- 1800
    d- 4200
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            Numerical.append(0)
            print('incorrect')
        print('''
    Q2- The ages of two brothers are in the ratio 7:6 If the age of the older brother is 15 years and 9 months, then what is the age of the younger brother?
    a- 12 years and 6 months
    b- 13 years and 9 months
    c- 13 years and 6 months
    d- 12 years and 9 months
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q3- Find a number which is greater than 18 in the same ratio as 11 is greater than 9.
    a- 12
    b- 22
    c- 32
    d- 42
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q4- The ratio 6 1/2:5:2 is equal to
    a- 5:4
    b- 6:5
    c- 8:7
    d- 13:1
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q5- What number must be subtracted from 22, 41, 60 and 117 so that the remainders may be proportional?
    a- 2
    b- 3
    c- 4
    d- 5
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q6- A 2 digit number is 4 times the sum of the digits Find the ratio of digits in units place to tens place
    a- 2:3
    b- 3:2
    c- 2:1
    d- 1:2
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q7- 60000 is divided among A,B and C so that if 40, 80 and 120 rupees is taken from their shares respectively,
    they will have money in the ratio 3:4:5. The share of B is
    a- 2080
    b- 2000
    c- 1920
    d- 2100
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q8- complete the identity (a+b)*2
    a- a*2 + b*2 +2AB
    b- AB*2 + AB
    c- 2AB + b*2
    d- AB + a*2
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q9- What is the correct Pythagores theorem C being the longest side
    a- A*2 + B*2= C*2
    b- AB*2 =C*2
    c- A + B = C*2
    d- None of these
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q10- Which number should be added to the antecedent and consequent of 7/11 so, That the ratio becomes 3/4
    a- 3
    b- 5
    c- 7
    d- 9
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Thank you for the completing the Numerical Test
    your score is
    ''')
        num=sum(Numerical)
        print(num,'out of 10')
    #############################################################################Numerical end scientific begin###################################################################################################
        sc=[]
        print('SCIENTIFIC')
        print('''
    Q1 - Knot is a unit of?
    a- speed
    b- time
    c- depth
    d- distance
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q2 - Ohm is used to measure?
    a- current
    b- voltage
    c- resistance
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q3 - What do we call the minimum velocity with which a body must be projected up, so as to enable it to just overcome the gravitational pull?
    a- orbital velocity
    b- escape velocity
    c- gravitational velocity
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q4 - Who is the author of 'A Brief History of Time?
    a- Stephen Hawking
    b- Richard Feynman
    c- Albert Einstein
    d- Erwin Schrodinger
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q5 - Amalgam is a term used for an alloy of a metal with?
    a- mercury
    b- gold
    c- copper
    d- tin
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q6 - LPG is a hydrocarbon containing a mixture of?
    a- ethane and butane
    b- methane and butane
    c- propane and butane
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q7 - Which of the following substances undergo sublimation on heating?
    a- camphor
    b- iodine
    c- napthalene
    d- all of the above
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q8 - BowmanÃ¢â‚¬â„¢s CapsuleÃ¢â‚¬â„¢ works as a part of the functional unit of which among the following human physiological system?
    a- circulatory system
    b- respiratory system
    c- excretory system
    d- digestive system
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q9 - The bacterium Ã¢â‚¬ËœEscherichia coliÃ¢â‚¬â„¢ is found mainly in:?
    a- root Nodules of leguminous plants
    b- human instestine
    c- human mouth
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q10 - Anemophily is pollination by?
    a- wind
    b- water
    c- insects
    d- none
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Thank you for the completing the Scientific Test
    your score is
    ''')
        science=sum(sc)
        print(science,'out of 10')
    ##########################################################################scientific end informatic begin######################################################################################
        xD=[]
        print('Informatic')
        print('''
    Q1- How many types of data extractions are there
    a- 1
    b- 2
    c- 3
    d- 4
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q2- What is the data format you prefer for informatica server
    a- ASCII
    b- EBCDIC
    c- UNICODE
    d- Decimal
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q3- An informatica variable contains
    a- Starvalue/end value
    b- start value/current value
    c- start value
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q4- Which of the following are active Transformations?
    a- Sorter
    b- Expression
    c- Normalizer
    d- Filter
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q5- What manages the scheduling and execution of workflows?
    a- Informatica server
    b- Repository Server
    c- Designer
    d- Monitor
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q6- Which Client component can be used for creating Repository?
    a- Manager
    b- Designer
    c- Worflow Manager
    d- Repository server Admin Console
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q7- Can an output port be used in the editable area of widgets
    a- Yes
    b- No
    c- Depends
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q8- Joiner Can?
    a- Join any two heterogeneous sources
    b- same data base
    c- Join only flatfiles
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q9- Who made Windows
    a- Steve Jobs
    b- Harvey Clint
    c- Larry Page
    d- Bill Gates
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q10- Which component gets metadata from Repository
    a- informatica server
    b- Informatica workflow Designer
    c- Informatica designer
    d- Informatica repository Server
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Thank you for completing the Informatic test
    your score is
    ''')
        mess=sum(xD)
        print(mess,'Out of 10')
        break
    ################################################END OF TEST###############################################################
print('')
print('FINAL SCORES FOR',user,'(OUT OF 10)')
print("")
print('LOGICAL REASONING',logical)
print('NUMERICAL ABILITY',num)
print('SCIENTIFIC REASONING',science)
print('INFROMATIC APTITUDE',mess)
print('')
if logical+num+science+mess>30:
    if school==True:
        print('OPT FOR PCM WITH COMPUTER SCIENCE!')
    else:
        print('LOOK INTO GOOD ENGINEERING COLLEGES SUCH AS IITs/NIITs')
elif logical+num>science+mess:
    if school==True:
        print('OPT FOR COMMERCE!')
    else:
        print('LOOK INTO GOOD COLLEGES FOR COMMERCE, SUCH AS IIM')
elif logical+science>logical+num:
    if school==True:
        print('OPT FOR PCB!')
    else:
        print('LOOK INTO GOOD MEDICAL COLLEGES SUCH AS AIIMS')
elif logical+mess>15:
    if school==True:
        print('WORK ON YOUR IT SKILLS!')
    else:
        print('LOOK INTO GOOD IT COURSES SUCH AS THOSE OFFERED BY ABROAD UNIVERSITIES')
else:
    if school==True:
        print('OPT FOR HUMANITIES')
    else:
        print('LOOK INTO GOOD ARTS COLLEGES SUCH AS ST.STEPHENS')
###########################################END MADE BY ARYAN AND YASH##########################################################################################user=input('NAME')
school=bool(input('Are you in school? (True/False'))
if school==True:
    var=bool(input('Are you in class 12? (True/False'))
print('''WELCOME TO THE APTITUDE TEST!
DEVELOPED BY: ARYAN KAUSHIK AND YASH SRIVASTAVA
THIS TEST WILL TEST YOUR APTITUDE IN FOUR CATEGORIES:

1) LOGICAL REASONING
2) NUMERICAL ABILITY
3) SCIENTIFIC APTITUDE
4) INFORMATIC APTITUDE

UPON COMPLETION OF THE TEST, YOUR SCORES FROM EACH TEST WOULD BE DISPLAYED AND A RECOMMENDED STREAM/COLLEGE WOULD BE SHOWN

TYPE 'yes' TO BEGIN THE TEST
''')
ch='yes'
ch=input('BEGIN?')
while ch=='yes':
    ############################################################################################logical##############################################################################################
        l1=[]
        print("LOGICAL REASONING")
        print('''
    Q1 - What is next in the sequence?
    BXJ,ETL,HPN,KLP,_
    a - NHR
    b - MHQ
    c - MIP
    d - none
    ''')
        answer=input().lower()
        if answer=='a':
              print('correct')
              l1.append(1)
        else:
              print('incorrect')
              l1.append(0)
        print('''
    Q2 - Rahul told Anand, "Yesterday I defeated the only brother of the daughter of my grandmother." Whom did Rahul defeat?
    a - Son
    b - Brother
    c - Father
    d - Cousin
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q3 - In a certain code, '467' means 'leaves are green' ; '485' means 'green is good' and '639' means 'they are playing'. Which digit stands for 'leaves' in that code?
    a - 4
    b - 7
    c - 6
    d - 3
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q4 - What can you conclude from the given statements :

    Some cats are dogs

    Some dogs are rats
    a - Some dogs are rats
    b - Some dogs are not rats
    c - All cats are dogs
    d - All cats are not dogs
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q5 - Find the letter in the 9th position when the alphabets are written in reverse alphabetical order from the right.
    a - M
    b - J
    c - I
    d - K
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q6 - Tina walks 4 km towards north, turns right and walks 5 km. Then he turns towards south and walks 2 km. Again he takes a turn towards west walks 3 km and stops for a while. Then he further walks 2 km in the same direction. What is the distance of Tina from starting point? 
    a - 2 km
    b - 8 km
    c - 16 km
    d - 4 km
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q7 - If rose is called popy, popy is called lily, lily is called lotus and lotus is called glandiola, which is the king of flowers?
    a - Rose
    b - Glandiola
    c - Popy
    d - Lily
    ''')
        answer=input().lower()
        if answer=='b':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
            print('''
    Q8 - Pointing to a gentleman, Deepak said, "His only brother is the father of my daughter's father." How is the gentleman related to Deepak?
    a - Father
    b - Brother
    c - Uncle
    d - None
    ''')
        answer=input().lower()
        if answer=='c':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q9 - What can you conclude from the given statement :

    All ants are tigers
    a - Some tigers are ants
    b - All tigers are ants
    c - All tigers are not ants
    d - None
    ''')
        answer=input().lower()
        if answer=='a':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Q10 - What should be the third step of the following input?
    Input: 239 123 58 361 495 37
    a - 495 37 361 239 123 58
    b - 495 37 361 123 239 58
    c - 495 37 58 123 361 239
    d - 495 37 361 239 123 58
    ''')
        answer=input().lower()
        if answer=='d':
            print('correct')
            l1.append(1)
        else:
            print('incorrect')
            l1.append(0)
        print('''
    Thank you for completing the Logical Reasoning Test
    your score is
    ''')
        logical=sum(l1)
        print(logical,'out of 10')
    ###################################################################################################logical end numerical begin################################################################################
        Numerical=[]
        print('NUMERICAL')
        print('''
    Q1 - An amount is to be distributed among A,B and C in the ratio 3:5:7. If B's share is 3000, then what is the difference between A and C's share
    a- 2400
    b- 2500
    c- 1800
    d- 4200
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            Numerical.append(0)
            print('incorrect')
        print('''
    Q2- The ages of two brothers are in the ratio 7:6 If the age of the older brother is 15 years and 9 months, then what is the age of the younger brother?
    a- 12 years and 6 months
    b- 13 years and 9 months
    c- 13 years and 6 months
    d- 12 years and 9 months
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q3- Find a number which is greater than 18 in the same ratio as 11 is greater than 9.
    a- 12
    b- 22
    c- 32
    d- 42
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q4- The ratio 6 1/2:5:2 is equal to
    a- 5:4
    b- 6:5
    c- 8:7
    d- 13:1
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q5- What number must be subtracted from 22, 41, 60 and 117 so that the remainders may be proportional?
    a- 2
    b- 3
    c- 4
    d- 5
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q6- A 2 digit number is 4 times the sum of the digits Find the ratio of digits in units place to tens place
    a- 2:3
    b- 3:2
    c- 2:1
    d- 1:2
    ''')
        answer2=input().lower()
        if answer2=='c':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q7- 60000 is divided among A,B and C so that if 40, 80 and 120 rupees is taken from their shares respectively,
    they will have money in the ratio 3:4:5. The share of B is
    a- 2080
    b- 2000
    c- 1920
    d- 2100
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q8- complete the identity (a+b)*2
    a- a*2 + b*2 +2AB
    b- AB*2 + AB
    c- 2AB + b*2
    d- AB + a*2
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q9- What is the correct Pythagores theorem C being the longest side
    a- A*2 + B*2= C*2
    b- AB*2 =C*2
    c- A + B = C*2
    d- None of these
    ''')
        answer2=input().lower()
        if answer2=='a':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Q10- Which number should be added to the antecedent and consequent of 7/11 so, That the ratio becomes 3/4
    a- 3
    b- 5
    c- 7
    d- 9
    ''')
        answer2=input().lower()
        if answer2=='b':
            print('correct')
            Numerical.append(1)
        else:
            print('incorrect')
            Numerical.append(0)
        print('''
    Thank you for the completing the Numerical Test
    your score is
    ''')
        num=sum(Numerical)
        print(num,'out of 10')
    #############################################################################Numerical end scientific begin###################################################################################################
        sc=[]
        print('SCIENTIFIC')
        print('''
    Q1 - Knot is a unit of?
    a- speed
    b- time
    c- depth
    d- distance
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q2 - Ohm is used to measure?
    a- current
    b- voltage
    c- resistance
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q3 - What do we call the minimum velocity with which a body must be projected up, so as to enable it to just overcome the gravitational pull?
    a- orbital velocity
    b- escape velocity
    c- gravitational velocity
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q4 - Who is the author of 'A Brief History of Time?
    a- Stephen Hawking
    b- Richard Feynman
    c- Albert Einstein
    d- Erwin Schrodinger
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q5 - Amalgam is a term used for an alloy of a metal with?
    a- mercury
    b- gold
    c- copper
    d- tin
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q6 - LPG is a hydrocarbon containing a mixture of?
    a- ethane and butane
    b- methane and butane
    c- propane and butane
    d- none
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q7 - Which of the following substances undergo sublimation on heating?
    a- camphor
    b- iodine
    c- napthalene
    d- all of the above
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q8 - BowmanÃ¢â‚¬â„¢s CapsuleÃ¢â‚¬â„¢ works as a part of the functional unit of which among the following human physiological system?
    a- circulatory system
    b- respiratory system
    c- excretory system
    d- digestive system
    ''')
        answer3=input().lower()
        if answer3=='c':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q9 - The bacterium Ã¢â‚¬ËœEscherichia coliÃ¢â‚¬â„¢ is found mainly in:?
    a- root Nodules of leguminous plants
    b- human instestine
    c- human mouth
    d- none
    ''')
        answer3=input().lower()
        if answer3=='b':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Q10 - Anemophily is pollination by?
    a- wind
    b- water
    c- insects
    d- none
    ''')
        answer3=input().lower()
        if answer3=='a':
            print('correct')
            sc.append(1)
        else:
            sc.append(0)
            print('incorrect')
        print('''
    Thank you for the completing the Scientific Test
    your score is
    ''')
        science=sum(sc)
        print(science,'out of 10')
    ##########################################################################scientific end informatic begin######################################################################################
        xD=[]
        print('Informatic')
        print('''
    Q1- How many types of data extractions are there
    a- 1
    b- 2
    c- 3
    d- 4
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q2- What is the data format you prefer for informatica server
    a- ASCII
    b- EBCDIC
    c- UNICODE
    d- Decimal
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q3- An informatica variable contains
    a- Starvalue/end value
    b- start value/current value
    c- start value
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q4- Which of the following are active Transformations?
    a- Sorter
    b- Expression
    c- Normalizer
    d- Filter
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q5- What manages the scheduling and execution of workflows?
    a- Informatica server
    b- Repository Server
    c- Designer
    d- Monitor
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q6- Which Client component can be used for creating Repository?
    a- Manager
    b- Designer
    c- Worflow Manager
    d- Repository server Admin Console
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q7- Can an output port be used in the editable area of widgets
    a- Yes
    b- No
    c- Depends
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='b':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q8- Joiner Can?
    a- Join any two heterogeneous sources
    b- same data base
    c- Join only flatfiles
    d- None of the above
    ''')
        answer4=input().lower()
        if answer4=='a':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q9- Who made Windows
    a- Steve Jobs
    b- Harvey Clint
    c- Larry Page
    d- Bill Gates
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Q10- Which component gets metadata from Repository
    a- informatica server
    b- Informatica workflow Designer
    c- Informatica designer
    d- Informatica repository Server
    ''')
        answer4=input().lower()
        if answer4=='d':
            print('correct')
            xD.append(1)
        else:
            xD.append(0)
            print('incorrect')
        print('''
    Thank you for completing the Informatic test
    your score is
    ''')
        mess=sum(xD)
        print(mess,'Out of 10')
        break
    ################################################END OF TEST###############################################################
print('')
print('FINAL SCORES FOR',user,'(OUT OF 10)')
print("")
print('LOGICAL REASONING',logical)
print('NUMERICAL ABILITY',num)
print('SCIENTIFIC REASONING',science)
print('INFROMATIC APTITUDE',mess)
print('')
if logical+num+science+mess>30:
    if school==True:
        print('OPT FOR PCM WITH COMPUTER SCIENCE!')
    else:
        print('LOOK INTO GOOD ENGINEERING COLLEGES SUCH AS IITs/NIITs')
elif logical+num>science+mess:
    if school==True:
        print('OPT FOR COMMERCE!')
    else:
        print('LOOK INTO GOOD COLLEGES FOR COMMERCE, SUCH AS IIM')
elif logical+science>logical+num:
    if school==True:
        print('OPT FOR PCB!')
    else:
        print('LOOK INTO GOOD MEDICAL COLLEGES SUCH AS AIIMS')
elif logical+mess>15:
    if school==True:
        print('WORK ON YOUR IT SKILLS!')
    else:
        print('LOOK INTO GOOD IT COURSES SUCH AS THOSE OFFERED BY ABROAD UNIVERSITIES')
else:
    if school==True:
        print('OPT FOR HUMANITIES')
    else:
        print('LOOK INTO GOOD ARTS COLLEGES SUCH AS ST.STEPHENS')
###########################################END MADE BY ARYAN AND YASH##########################################################################################

