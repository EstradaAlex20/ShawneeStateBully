from Newdialog import *
import pygame

class quest:
    def __init__(self,list,var,npc,numb):
        self.convolist = list
        self.var = var
        self.phase = 0
        self.npc = npc
        self.numb = numb
        self.complete = False


    def check(self,var,screen,clock):
        if int(var[self.numb]) >= int(self.var):
            self.phase = 2
            # print(self.var)
        if self.phase == 0:
            self.now = self.convolist[0]
            self.phase +=1
        elif self.phase == 1:
            self.now = self.convolist[1]
        elif self.phase == 2 and not self.complete:
            self.now = self.convolist[2]
            var[self.numb] -= int(self.var)
            self.phase += 1
            self.complete = True
        elif self.phase == 3 or self.complete :
            self.now = self.convolist[3]
        convo(screen,self.now,clock)
        return var
def quest_set(file):
    fp = open(file)
    questlist = []
    list = []
    for line in fp:
        line = line.strip()
        if line.count("=") > 0:
            a = line.split("=")
            numb = a[0]
        if line.count(":") != 1:
            continue
        line = line.split(":")
        if line[0] == "npc":
            npc = line[1]
        if line[0] == "var":
            var = line[1]
        if line[0] == "convo":
            list.append(line[1])
        if line[0] == "break":
            questlist.append(quest(list,var,npc,numb))
            list = []

    return questlist

def quest_var(file):
    var_list = {}
    fp = open(file)
    for line in fp:
        line = line.strip()
        if line.count("=") != 1:
            continue
        line = line.split("=")
        var_list[line[0]]= line[1]
    return var_list
if __name__ == "__main__":
    test = quest_set("quests")
    var = quest_var("quests")

    print(test[0].phase)
    test[0].check(var)
    print(test[0].phase)











