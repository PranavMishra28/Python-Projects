#HANGMAN BY PRANAV
import random
import tkinter
listm=["forest gump","dark knight","la la land","black panther","anna","ready player one","","the grand budapest","iron man","joker","fast and furious","bohemian rhapsody","pulp fiction","avengers endgame","spiderman homecoming"]
x=len(listm)
y=random.randrange(0,x)
movie=listm[y]
cname=movie
points=0
for i in cname:
    if i not in ["a","e","i","o","u"," "]:
        cname=cname.replace(i,"*")
ee=[]
ctr=0
checklist=[cname]
name2=list(cname)
print(name2)
window=tkinter.Tk()
window.title("HANGMAN")
window.geometry("1300x700")
h1=tkinter.Label(window, text="welcome to hangman", font=("algerian",50))
h1.place(relx=0.5,rely=0.05,anchor="center")
h2=tkinter.Label(window, text="points")
label=tkinter.Label(window,text=cname,font=("courier new CE",52))
label.place(relx=0.67,rely=0.19,anchor="center")
canvas=tkinter.Canvas(window,width=400,height=750)
canvas.place(relx=0,rely=0.7,anchor="w")
canvas.create_line(23,0,23,550,fill="black")
canvas.create_line(0,550,350,550)
canvas.create_line(23,2,250,2,fill="black")
canvas.create_line(250,0,250,25,fill="black")
#def check("l"):
#    global name2
#    global movie
#    global ctr
#    ctr2=0
#    name1=movie
#    for i in name1:
#        if i not in ["a","e","i","o","u"," ","l"]:
#            if name2[ctr2]=="*":
#                name1=name1.replace(i,"*")
#        ctr2+=1
#    label["text"]=name1
#    b.config(state="disabled")
#   name2=list(name1)    
#    b["bg"]="red"
#   lenlist=len(checklist)
#    print(lenlist)
#    if name1==checklist[len(checklist)-1]:
#        ctr+=1
#    draw()
#    checklist.append(name1)
#    if name1==movie:
#        label["text"]="YOU WIN!!!"
#cannot be used as entering a value in the bracket of the function
#while definig function of the button called the function without pressing
#the button hence each button had to be programmed individually
def draw():
    global ctr
    if ctr==0:
        None
    if ctr==1:
        canvas.create_oval(175,25,325,150,fill="black")
    if ctr==2:
        canvas.create_oval(190,25,310,120,fill="black")
        canvas.create_line(250,100,250,400,fill="black")
    if ctr==3:
        canvas.create_oval(190,25,310,120,fill="black")
        canvas.create_line(250,100,250,400,fill="black")
        canvas.create_line(150,100,250,200,fill="black")
    if ctr==4:
        canvas.create_oval(190,25,310,120,fill="black")
        canvas.create_line(250,100,250,400,fill="black")
        canvas.create_line(150,100,250,200,fill="black")
        canvas.create_line(350,100,250,200,fill="black")
    if ctr==5:
        canvas.create_oval(190,25,310,120,fill="black")
        canvas.create_line(250,100,250,400,fill="black")
        canvas.create_line(150,100,250,200,fill="black")
        canvas.create_line(350,100,250,200,fill="black")
        canvas.create_line(350,499,250,399,fill="black")
    if ctr==6:
        canvas.create_oval(190,25,310,120,fill="black")
        canvas.create_line(250,100,250,400,fill="black")
        canvas.create_line(150,100,250,200,fill="black")
        canvas.create_line(350,100,250,200,fill="black")
        canvas.create_line(350,499,250,399,fill="black")
        canvas.create_line(150,499,250,399)
        label["text"]="GAME OVER"
    if ee==["k","n","y"]:
        label["text"]="aryaman is a god"
    print(ee)
    
    
        
    
def checkb():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","b"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    b.config(state="disabled")
    name2=list(name1)    
    b["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
    
    
def checkc():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","c"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    c.config(state="disabled")
    name2=list(name1)    
    c["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkd():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","d"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    d.config(state="disabled")
    name2=list(name1)    
    d["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkf():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","f"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    f.config(state="disabled")
    name2=list(name1)    
    f["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkg():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","g"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    g.config(state="disabled")
    name2=list(name1)    
    g["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkh():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","h"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    h.config(state="disabled")
    name2=list(name1)    
    h["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkj():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","j"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    j.config(state="disabled")
    name2=list(name1)    
    j["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkk():
    global name2
    global movie
    global ctr
    global ee
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","k"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    k.config(state="disabled")
    name2=list(name1)    
    k["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
    ee.append("k")
def checkl():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","l"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    l.config(state="disabled")
    name2=list(name1)    
    l["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkm():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","m"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    m.config(state="disabled")
    name2=list(name1)    
    m["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkn():
    global name2
    global movie
    global ctr
    global ee
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","n"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    n.config(state="disabled")
    name2=list(name1)    
    n["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
    ee.append("n")
def checkp():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","p"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    p.config(state="disabled")
    name2=list(name1)    
    p["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkq():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","q"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    q.config(state="disabled")
    name2=list(name1)    
    q["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkr():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","r"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    r.config(state="disabled")
    name2=list(name1)    
    r["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checks():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","s"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    s.config(state="disabled")
    name2=list(name1)    
    s["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkt():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","t"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    t.config(state="disabled")
    name2=list(name1)    
    t["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkv():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","v"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    v.config(state="disabled")
    name2=list(name1)    
    v["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkw():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","w"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    w.config(state="disabled")
    name2=list(name1)    
    w["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checkx():
    global name2
    global movie
    global ctr
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","x"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    x.config(state="disabled")
    name2=list(name1)    
    x["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
def checky():
    global name2
    global movie
    global ctr
    global ee
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","y"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    y.config(state="disabled")
    name2=list(name1)    
    y["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    ee.append("y")
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
    
def checkz():
    global name2
    global movie
    global ctr
    global points
    ctr2=0
    name1=movie
    for i in name1:
        if i not in ["a","e","i","o","u"," ","z"]:
            if name2[ctr2]=="*":
                name1=name1.replace(i,"*")
        ctr2+=1
    label["text"]=name1
    z.config(state="disabled")
    name2=list(name1)    
    z["bg"]="red"
    lenlist=len(checklist)
    print(lenlist)
    if name1==checklist[len(checklist)-1]:
        ctr+=1
    draw()
    checklist.append(name1)
    if name1==movie:
        label["text"]="YOU WIN!!!"
        points+=1

    

b=tkinter.Button(window,text="b",font=("calibiri",22),command=checkb)
b.place(relx=0.44,rely=0.31,anchor="center")
c=tkinter.Button(window,text="c",font=("calibiri",22),command=checkc)
c.place(relx=0.48,rely=0.31,anchor="center")
d=tkinter.Button(window,text="d",font=("calibiri",22),command=checkd)
d.place(relx=0.52,rely=0.31,anchor="center")
f=tkinter.Button(window,text="f",font=("calibiri",22),command=checkf)
f.place(relx=0.56,rely=0.31,anchor="center")
g=tkinter.Button(window,text="g",font=("calibiri",22),command=checkg)
g.place(relx=0.6,rely=0.31,anchor="center")
h=tkinter.Button(window,text="h",font=("calibiri",22),command=checkh)
h.place(relx=0.64,rely=0.31,anchor="center")
j=tkinter.Button(window,text="j",font=("calibiri",22),command=checkj)
j.place(relx=0.68,rely=0.31,anchor="center")
k=tkinter.Button(window,text="k",font=("calibiri",22),command=checkk)
k.place(relx=0.72,rely=0.31,anchor="center")
l=tkinter.Button(window,text="l",font=("calibiri",22),command=checkl)
l.place(relx=0.76,rely=0.31,anchor="center")
m=tkinter.Button(window,text="m",font=("calibiri",22),command=checkm)
m.place(relx=0.8,rely=0.31,anchor="center")
n=tkinter.Button(window,text="n",font=("calibiri",22),command=checkn)
n.place(relx=0.84,rely=0.31,anchor="center")
p=tkinter.Button(window,text="p",font=("calibiri",22),command=checkp)
p.place(relx=0.46,rely=0.42,anchor="center")
q=tkinter.Button(window,text="q",font=("calibiri",22),command=checkq)
q.place(relx=0.50,rely=0.42,anchor="center")
r=tkinter.Button(window,text="r",font=("calibiri",22),command=checkr)
r.place(relx=0.54,rely=0.42,anchor="center")
s=tkinter.Button(window,text="s",font=("calibiri",22),command=checks)
s.place(relx=0.58,rely=0.42,anchor="center")
t=tkinter.Button(window,text="t",font=("calibiri",22),command=checkt)
t.place(relx=0.62,rely=0.42,anchor="center")
v=tkinter.Button(window,text="v",font=("calibiri",22),command=checkv)
v.place(relx=0.66,rely=0.42,anchor="center")
w=tkinter.Button(window,text="w",font=("calibiri",22),command=checkw)
w.place(relx=0.70,rely=0.42,anchor="center")
x=tkinter.Button(window,text="x",font=("calibiri",22),command=checkx)
x.place(relx=0.74,rely=0.42,anchor="center")
y=tkinter.Button(window,text="y",font=("calibiri",22),command=checky)
y.place(relx=0.78,rely=0.42,anchor="center")
z=tkinter.Button(window,text="z",font=("calibiri",22),command=checkz)
z.place(relx=0.82,rely=0.42,anchor="center")
restart=tkinter.Button(window,text="reset",font=("calibiri",25),command=reset)
restart.place(relx=0.95,rely=0.62,anchor="center")
window.mainloop()


