import data.JsonUtils as jsu
import pyautogui as gui
from json import loads as jsls
datafile = "settings.json"
title = "Bingbo"
while 1:
    data = jsu.read(datafile)
    users = []
    for i, user in enumerate(data):
        users.append(user)
    enabled=[]
    for i , user in enumerate(users):
        if user[2]:
            enabled.append(user)
    where = gui.confirm(f"enabled users:\n{enabled}", title, ["edit", "new", "exit"])

    if where == "edit":
        if users==[]:
            gui.alert("no users in database",title)
        _ = gui.confirm("select account", title,users)
        who=None
        for i,user in enumerate(users):
            if _==str(user):
                who=user
                break
        what = gui.confirm(who, title, ["edit", "delete","toggle"])

        if what == "edit":
            name = gui.prompt("new user", title, who[0])
            key = gui.prompt("new pass", title)
            for i, user in enumerate(data):
                if user[0] == who[0]:
                    data[i] = [name, key,1]
                    jsu.write(data, datafile)
                    gui.alert("entry changed", title)
                    break

        if what == "delete":
            for i, user in enumerate(data):
                if who[0] == user[0]:
                    data.remove(data[i])
                    # data[i]=None
                    jsu.write(data, datafile)
                    gui.alert("entry deleted", title)
        if what == "toggle":
            index=None
            for _,user in enumerate(data):
                if who==user:
                    index=_
                    break
            if who[2]==1:
                data[index][2]=0
            elif who[2]==0:
                data[index][2]=1
            jsu.write(data, datafile)
            gui.alert("entry toggled", title)
            
    if where == "new":
        name = gui.prompt("new user", title)
        key = gui.prompt("new pass", title)
        data.append([name, key,1])
        jsu.write(data, datafile)

    if where == "exit":
        break
