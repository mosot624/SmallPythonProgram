# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:09:49 2018

@author: Michael
"""

from tkinter import*
from tkinter import messagebox

"""variables that you would be using"""


class VarialbeToUse:
    event_dic = {1:{"Event":"Running","Type":"Sports","Team":True}, 2:{"Event":"Swimming","Type":"Sports","Team":True}, 3:{"Event":"Maths Quiz","Type":"Academics","Team":False}, 4:{"Event":"Science Quiz","Type":"Academics","Team":False}, 5:{"Event":"Football","Type":"Sports","Team":True}}
    i = 1
    root1 = 0
    ifInTeam = False
    team_dic = {}
    

class VarialbeForScoringSystem:
    entEvent1 = ""
    entEvent2 = ""
    entEvent3 = ""
    entEvent4 = ""
    
    
    Entry1Team1 = 0
    Entry2Team1= 0
    Entry3Team1= 0
    Entry4Team1= 0
    Entry5Team1= 0
    
    
    Entry1Team2= 0
    Entry2Team2= 0
    Entry3Team2= 0
    Entry4Team2= 0
    Entry5Team2= 0

    Entry1Team3= 0
    Entry2Team3= 0
    Entry3Team3= 0
    Entry4Team3= 0
    Entry5Team3= 0

    
    Entry1Team4= 0
    Entry2Team4= 0
    Entry3Team4= 0
    Entry4Team4= 0
    Entry5Team4= 0
    
    Answer1Label=""
    Answer2Label=""
    Answer3Label=""
    Answer4Label=""


def checkValueIfTheyAreTeam():
    l = entry1.get()
    if l == "individual":
        VarialbeToUse.ifinTeam = False
        root.destroy()
        whatIsthereYourName()

    elif l == "team":
        VarialbeToUse.ifInTeam = True
        root.destroy()
        whatIsthereTeamName()
    else:
        messagebox.showinfo("Warning","Could you type that again.")



def openStartingQuestion():
        global entry1
        global root
        root = Tk()
        
    
        Label1 = Label(root,text="Are you a team or individual?")
        entry1 = Entry(root)
        button1 = Button(root,text= "Enter",command = checkValueIfTheyAreTeam)
        
    
        Label1.grid(row=0)
        entry1.grid(row=0,column = 1)
        button1.grid(row=1,column = 0)
    
        root.mainloop()


def whatIsthereTeamName():
        global AskTeamEnt
        global AmountTeamEnt
        VarialbeToUse.root1 = Tk()
        teamName = "What is your team name, group %d" % VarialbeToUse.i

        AskTeamLab = Label(VarialbeToUse.root1,text= teamName)
        AmountTeamLab = Label(VarialbeToUse.root1,text="How many are you in the team?")
        AskTeamEnt = Entry(VarialbeToUse.root1)
        AmountTeamEnt = Entry(VarialbeToUse.root1)
        button1 = Button(VarialbeToUse.root1,text= "Enter",command=addingValueToteamDic)
        
        
        AskTeamLab.grid(row=0)
        AskTeamEnt.grid(row=0,column = 1)
        AmountTeamLab.grid(row=1)
        AmountTeamEnt.grid(row=1,column = 1)
        button1.grid(row=3,column = 0)
        VarialbeToUse.root1.mainloop()

        
def whatIsthereYourName():
        global AskTeamEnt1
        
        VarialbeToUse.root1 = Tk()
        teamName = "Who are you, group %d" %  VarialbeToUse.i
        
        AskTeamLab = Label(VarialbeToUse.root1,text= teamName)
        AskTeamEnt1 = Entry(VarialbeToUse.root1)
        button1 = Button(VarialbeToUse.root1,text= "Enter",command=addingValueToteamDicSinglePerson)
        
        
        AskTeamLab.grid(row=0)
        AskTeamEnt1.grid(row=0,column = 1)
        
        button1.grid(row=1,column = 0)
        VarialbeToUse.root1.mainloop()
        
        
def addingValueToteamDic():
    TeamName = AskTeamEnt.get()
    Members = int(AmountTeamEnt.get())
    
    if Members >5 or Members <2:
        messagebox.showinfo("Warning","Memeber bigger than 5 or smaller than 2")
    else:
        VarialbeToUse.team_dic.update({VarialbeToUse.i:{"team_name":TeamName,"Members":Members}})
        VarialbeToUse.root1.destroy()
        OnlyJoinOneEvent()

        
    

def addingValueToteamDicSinglePerson():
    TeamName = AskTeamEnt1.get()
    VarialbeToUse.team_dic.update({VarialbeToUse.i:{"team_name":TeamName,"Members":1}})
    VarialbeToUse.root1.destroy()
    OnlyJoinOneEvent()
    
    
def checkWherToGoToAnotherSceen():
    VarialbeToUse.i +=1
    if VarialbeToUse.i < 5:
        openStartingQuestion()
        
    else:
        print(VarialbeToUse.team_dic)
        ScoreBoardTemplate()


def OnlyJoinOneEvent():
        global JoinSportVarEnt
        VarialbeToUse.root1 = Tk()

        JoinSportVarLab = Label(VarialbeToUse.root1,text="Would You like to only join one event? y/n")
        JoinSportVarEnt = Entry(VarialbeToUse.root1)
        
        button1 = Button(VarialbeToUse.root1,text= "Enter",command=JoinOnlyOneEvent)
        
        """button1.bind("<Button-1>", checkValueIfTheyAreTeam)"""
        
        JoinSportVarLab.grid(row=0)
        JoinSportVarEnt.grid(row=0,column = 1)
        button1.grid(row=3,column = 0)
        VarialbeToUse.root1.mainloop()
    
def JoinOnlyOneEvent():
    answer = JoinSportVarEnt.get()
    
    if answer == "y":
        VarialbeToUse.root1.destroy()
        askWhatEvent()

    elif answer == "n":
        VarialbeToUse.team_dic[VarialbeToUse.i].update({"OnlyJoinOneEvent":False})
        VarialbeToUse.root1.destroy()
        checkWherToGoToAnotherSceen()
    else:
        messagebox.showinfo("Warning","Could you type that again.")
        
def askWhatEvent():
        global WhatEventEnt
        VarialbeToUse.root1 = Tk()

        WhatEventLab = Label(VarialbeToUse.root1,text="What Event would you like to join?")
        WhatEventEnt = Entry(VarialbeToUse.root1)
        
        button1 = Button(VarialbeToUse.root1,text= "Enter",command=checkIfEventExist)
        
        
        WhatEventLab.grid(row=0)
        WhatEventEnt.grid(row=0,column = 1)
        button1.grid(row=3,column = 0)
        VarialbeToUse.root1.mainloop()

def checkIfEventExist():
    eventChosen = WhatEventEnt.get()
    eventExist = False
    for items in VarialbeToUse.event_dic.values():
        if eventChosen == items["Event"]:
            eventExist = True
            
    if eventExist == True:
        VarialbeToUse.team_dic[VarialbeToUse.i].update({"OnlyJoinOneEvent":True,"Event":eventChosen})
        VarialbeToUse.root1.destroy()
        checkWherToGoToAnotherSceen()
    else:
         messagebox.showinfo("Warning","That event doens't exist")
    
    
def ScoreBoardTemplate():
    """
    root2 = Tk()
    Event1 = str(VarialbeToUse.event_dic[1]["Event"])
    Event2 = VarialbeToUse.event_dic[2]["Event"]
    Event3 = VarialbeToUse.event_dic[3]["Event"]
    Event4 = VarialbeToUse.event_dic[4]["Event"]
    Event5 = VarialbeToUse.event_dic[5]["Event"]
    
    Team1 = str(VarialbeToUse.team_dic[1]["team_name"])
    Team2 = VarialbeToUse.team_dic[2]["team_name"]
    Team3 = VarialbeToUse.team_dic[3]["team_name"]
    Team4 = VarialbeToUse.team_dic[4]["team_name"]


    Event1Label = Label(root2 , text = "Hello")
    Event2Label = Label(root2 , text = Event2)
    Event3Label = Label(root2 , text = Event3)
    Event4Label = Label(root2 , text = Event4)
    Event5Label = Label(root2 , text = Event5)
    
    Team1Label = Label(root2 , text = Team1)
    
    Team2Label = Label(VarialbeToUse.root1 , text = Team2)
    Team3Label = Label(VarialbeToUse.root1 , text = Team3)
    Team4Label = Label(VarialbeToUse.root1 , text = Team4)
    
    
    WhatEventLab = Label(VarialbeToUse.root1,text="What Event would you like to join?")
        
        
        
    WhatEventLab.grid(row=0)

    
    root2.mainloop()
    """
    VarialbeToUse.root1 = Tk()
    


    Event1 = str(VarialbeToUse.event_dic[1]["Event"])
    Event2 = str(VarialbeToUse.event_dic[2]["Event"])
    Event3 = str(VarialbeToUse.event_dic[3]["Event"])
    Event4 = str(VarialbeToUse.event_dic[4]["Event"])
    Event5 = str(VarialbeToUse.event_dic[5]["Event"])

    
    Team1 = str(VarialbeToUse.team_dic[1]["team_name"])
    Team2 = str(VarialbeToUse.team_dic[2]["team_name"])
    Team3 = str(VarialbeToUse.team_dic[3]["team_name"])
    Team4 = str(VarialbeToUse.team_dic[4]["team_name"])

    

    
    Event1Label = Label(VarialbeToUse.root1,text=Event1)
    Event2Label = Label(VarialbeToUse.root1,text=Event2)
    Event3Label = Label(VarialbeToUse.root1,text=Event3)
    Event4Label = Label(VarialbeToUse.root1,text=Event4)
    Event5Label = Label(VarialbeToUse.root1,text=Event5)

    VarialbeForScoringSystem.Answer1Label = Label(VarialbeToUse.root1,text="0")
    VarialbeForScoringSystem.Answer2Label = Label(VarialbeToUse.root1,text="0")
    VarialbeForScoringSystem.Answer3Label = Label(VarialbeToUse.root1,text="0")
    VarialbeForScoringSystem.Answer4Label = Label(VarialbeToUse.root1,text="0")
     
    VarialbeForScoringSystem.Entry1Team1 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry2Team1 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry3Team1 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry4Team1 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry5Team1 = Entry(VarialbeToUse.root1)
 
    VarialbeForScoringSystem.Entry1Team1.insert(0,"0")
    VarialbeForScoringSystem.Entry2Team1.insert(0,"0")
    VarialbeForScoringSystem.Entry3Team1.insert(0,"0")
    VarialbeForScoringSystem.Entry4Team1.insert(0,"0")
    VarialbeForScoringSystem.Entry5Team1.insert(0,"0")
    
    VarialbeForScoringSystem.Entry1Team2 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry2Team2 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry3Team2 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry4Team2 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry5Team2 = Entry(VarialbeToUse.root1)
    
    VarialbeForScoringSystem.Entry1Team2.insert(0,"0")
    VarialbeForScoringSystem.Entry2Team2.insert(0,"0")
    VarialbeForScoringSystem.Entry3Team2.insert(0,"0")
    VarialbeForScoringSystem.Entry4Team2.insert(0,"0")
    VarialbeForScoringSystem.Entry5Team2.insert(0,"0")
    
    VarialbeForScoringSystem.Entry1Team3 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry2Team3 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry3Team3 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry4Team3 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry5Team3 = Entry(VarialbeToUse.root1)
    
    VarialbeForScoringSystem.Entry1Team3.insert(0,"0")
    VarialbeForScoringSystem.Entry2Team3.insert(0,"0")
    VarialbeForScoringSystem.Entry3Team3.insert(0,"0")
    VarialbeForScoringSystem.Entry4Team3.insert(0,"0")
    VarialbeForScoringSystem.Entry5Team3.insert(0,"0")
    
    VarialbeForScoringSystem.Entry1Team4 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry2Team4 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry3Team4 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry4Team4 = Entry(VarialbeToUse.root1)
    VarialbeForScoringSystem.Entry5Team4 = Entry(VarialbeToUse.root1)
    
    VarialbeForScoringSystem.Entry1Team4.insert(0,"0")
    VarialbeForScoringSystem.Entry2Team4.insert(0,"0")
    VarialbeForScoringSystem.Entry3Team4.insert(0,"0")
    VarialbeForScoringSystem.Entry4Team4.insert(0,"0")
    VarialbeForScoringSystem.Entry5Team4.insert(0,"0")
    
    Team1Label = Label(VarialbeToUse.root1,text=Team1)
    Team2Label = Label(VarialbeToUse.root1,text=Team2)
    Team3Label = Label(VarialbeToUse.root1,text=Team3)
    Team4Label = Label(VarialbeToUse.root1,text=Team4)

    

    
    VarialbeForScoringSystem.Entry1Team1.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam1(1)))
    VarialbeForScoringSystem.Entry2Team1.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam1(2)))
    VarialbeForScoringSystem.Entry3Team1.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam1(3)))
    VarialbeForScoringSystem.Entry4Team1.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam1(4)))
    VarialbeForScoringSystem.Entry5Team1.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam1(5)))
    
    VarialbeForScoringSystem.Entry1Team2.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(1)))
    VarialbeForScoringSystem.Entry2Team2.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(2)))
    VarialbeForScoringSystem.Entry3Team2.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(3)))
    VarialbeForScoringSystem.Entry4Team2.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(4)))
    VarialbeForScoringSystem.Entry5Team2.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(5)))

    VarialbeForScoringSystem.Entry1Team3.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(1)))
    VarialbeForScoringSystem.Entry2Team3.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(2)))
    VarialbeForScoringSystem.Entry3Team3.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(3)))
    VarialbeForScoringSystem.Entry4Team3.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(4)))
    VarialbeForScoringSystem.Entry5Team3.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(5)))

    VarialbeForScoringSystem.Entry1Team4.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(1)))
    VarialbeForScoringSystem.Entry2Team4.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(2)))
    VarialbeForScoringSystem.Entry3Team4.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(3)))
    VarialbeForScoringSystem.Entry4Team4.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(4)))
    VarialbeForScoringSystem.Entry5Team4.bind("<Button-1>", (lambda event: checkWhetherUserCanAccessItteam2(5)))

    
        
    Event1Label.grid(row=0,column = 1)
    Event2Label.grid(row=0,column = 2)
    Event3Label.grid(row=0,column = 3)
    Event4Label.grid(row=0,column = 4)
    Event5Label.grid(row=0,column = 5)

    Team1Label.grid(row=1)
    Team2Label.grid(row=2)
    Team3Label.grid(row=3)
    Team4Label.grid(row=4)
   
    
    VarialbeForScoringSystem.Answer1Label.grid(row=1,column=6)
    VarialbeForScoringSystem.Answer2Label.grid(row=2,column=6)
    VarialbeForScoringSystem.Answer3Label.grid(row=3,column=6)
    VarialbeForScoringSystem.Answer4Label.grid(row=4,column=6)
    
    VarialbeForScoringSystem.Entry1Team1.grid(row=1,column=1)
    VarialbeForScoringSystem.Entry2Team1.grid(row=1,column=2)
    VarialbeForScoringSystem.Entry3Team1.grid(row=1,column=3)
    VarialbeForScoringSystem.Entry4Team1.grid(row=1,column=4)
    VarialbeForScoringSystem.Entry5Team1.grid(row=1,column=5)
    
    VarialbeForScoringSystem.Entry1Team2.grid(row=2,column=1)
    VarialbeForScoringSystem.Entry2Team2.grid(row=2,column=2)
    VarialbeForScoringSystem.Entry3Team2.grid(row=2,column=3)
    VarialbeForScoringSystem.Entry4Team2.grid(row=2,column=4)
    VarialbeForScoringSystem.Entry5Team2.grid(row=2,column=5)
    
    VarialbeForScoringSystem.Entry1Team3.grid(row=3,column=1)
    VarialbeForScoringSystem.Entry2Team3.grid(row=3,column=2)
    VarialbeForScoringSystem.Entry3Team3.grid(row=3,column=3)
    VarialbeForScoringSystem.Entry4Team3.grid(row=3,column=4)
    VarialbeForScoringSystem.Entry5Team3.grid(row=3,column=5)
    
    VarialbeForScoringSystem.Entry1Team4.grid(row=4,column=1)
    VarialbeForScoringSystem.Entry2Team4.grid(row=4,column=2)
    VarialbeForScoringSystem.Entry3Team4.grid(row=4,column=3)
    VarialbeForScoringSystem.Entry4Team4.grid(row=4,column=4)
    VarialbeForScoringSystem.Entry5Team4.grid(row=4,column=5)
    
    
    buttonList = Button(VarialbeToUse.root1,text= "Enter",command=FindOverAllValue)
        
        
  
    buttonList.grid(row=6,column = 0)
    VarialbeToUse.root1.mainloop()
    
def FindOverAllValue():
    answerTeam1= int(VarialbeForScoringSystem.Entry1Team1.get()) + int(VarialbeForScoringSystem.Entry2Team1.get()) + int(VarialbeForScoringSystem.Entry3Team1.get()) + int(VarialbeForScoringSystem.Entry4Team1.get()) + int(VarialbeForScoringSystem.Entry5Team1.get())
    answerTeam2= int(VarialbeForScoringSystem.Entry1Team2.get()) + int(VarialbeForScoringSystem.Entry2Team2.get()) + int(VarialbeForScoringSystem.Entry3Team2.get()) + int(VarialbeForScoringSystem.Entry4Team2.get()) + int(VarialbeForScoringSystem.Entry5Team2.get())
    answerTeam3= int(VarialbeForScoringSystem.Entry1Team3.get()) + int(VarialbeForScoringSystem.Entry2Team3.get()) + int(VarialbeForScoringSystem.Entry3Team3.get()) + int(VarialbeForScoringSystem.Entry4Team3.get()) + int(VarialbeForScoringSystem.Entry5Team3.get())
    answerTeam4= int(VarialbeForScoringSystem.Entry1Team4.get()) + int(VarialbeForScoringSystem.Entry2Team4.get()) + int(VarialbeForScoringSystem.Entry3Team4.get()) + int(VarialbeForScoringSystem.Entry4Team4.get()) + int(VarialbeForScoringSystem.Entry5Team4.get())
    
    
    VarialbeForScoringSystem.Answer1Label.config(text = answerTeam1)
    VarialbeForScoringSystem.Answer2Label.config(text = answerTeam2)
    VarialbeForScoringSystem.Answer3Label.config(text = answerTeam3)
    VarialbeForScoringSystem.Answer4Label.config(text = answerTeam4)
    print("Hello world")

def checkWhetherUserCanAccessItteam1(l):
    VarialbeForScoringSystem.entEvent1 = VarialbeToUse.event_dic[l]["Event"]
    if(VarialbeToUse.team_dic[1]["OnlyJoinOneEvent"] == True):
        if(VarialbeToUse.team_dic[1]["Event"] != VarialbeForScoringSystem.entEvent1):
            messagebox.showinfo("Warning","You can only choose one")
def checkWhetherUserCanAccessItteam2(l):
    VarialbeForScoringSystem.entEvent2 = VarialbeToUse.event_dic[l]["Event"]
    if(VarialbeToUse.team_dic[2]["OnlyJoinOneEvent"] == True):
        if(VarialbeToUse.team_dic[2]["Event"] != VarialbeForScoringSystem.entEvent2):
            messagebox.showinfo("Warning","You can only choose one")
            
def checkWhetherUserCanAccessItteam3(l):
    VarialbeForScoringSystem.entEvent3 = VarialbeToUse.event_dic[l]["Event"]
    if(VarialbeToUse.team_dic[3]["OnlyJoinOneEvent"] == True):
        if(VarialbeToUse.team_dic[3]["Event"] != VarialbeForScoringSystem.entEvent3):
            messagebox.showinfo("Warning","You can only choose one")
def checkWhetherUserCanAccessItteam4(l):
    VarialbeForScoringSystem.entEvent4 = VarialbeToUse.event_dic[l]["Event"]
    if(VarialbeToUse.team_dic[4]["OnlyJoinOneEvent"] == True):
        if(VarialbeToUse.team_dic[4]["Event"] != VarialbeForScoringSystem.entEvent4):
            messagebox.showinfo("Warning","You can only choose one")
            
def checkWhetherUserCanAccessItteam5(l):
    VarialbeForScoringSystem.entEvent5 = VarialbeToUse.event_dic[l]["Event"]
    if(VarialbeToUse.team_dic[5]["OnlyJoinOneEvent"] == True):
        if(VarialbeToUse.team_dic[5]["Event"] != VarialbeForScoringSystem.entEvent4):
            messagebox.showinfo("Warning","You can only choose one")
openStartingQuestion()
