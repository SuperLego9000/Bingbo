import subprocess as subp
import data.JsonUtils as jsu
import threading
from time import sleep as wait
from os import system as sys
import multiprocessing
print("[40m[97m")
sys("cls")
sys("title Bingbo")
global threadcount
threadcount = 0
maxthreads = int(multiprocessing.cpu_count()*.7)

#maxthreads = 12


def rich(user, key):
    for i in range(3):
        print(f"[35mchecking points for user:[103m[30m {user} [40m[35m...[40m[30m")
        try:
            subp.run(
                f"cmd /c python data\BingRewards\BingRewards.py -r -hl -e {user} -p {key} -d chrome",
                stdout=subp.DEVNULL,
                stderr=subp.STDOUT
            )
            print(f"[93mclaimed available points for user: {user}[40m[30m")
        except:
            print("ERROR>OH GOD WHAT DID YOU DO?")
        global threadcount
        threadcount -= 1


data = "settings.json"
data = jsu.read(data)
if data == []:
    raise(ValueError("no users in database"))
for _, person in enumerate(data):
    if person[2]:
        while threadcount+1 > maxthreads:
            wait(5)
            print(
                f"                [41m{person[0].split('@outlook.com')[0].split('@hotmail.com')[0]} waiting for thread[40m")
        print(f"[40m[97mstarting thread ({threadcount+1}/{maxthreads})[30m")
        threading.Thread(target=lambda: rich(person[0], person[1])).start()
        threadcount += 1
