import subprocess as subp
import data.JsonUtils as jsu
import threading
from time import sleep as wait
from os import system as sys
import multiprocessing
print("[40m[97m")
sys("cls")
global threadcount
threadcount = 0
maxthreads = int(multiprocessing.cpu_count()*.7)

#maxthreads = 12


def rich(user, key):
    for i in range(3):
        print(f"[35mclaiming points for user: {user}[97m")
        try:
            subp.run(
                f"cmd /c python data\BingRewards\BingRewards.py -r -hl -e {user} -p {key} -d chrome"
            )
            print(f"[93mclaimed available points for user: {user}[97m")
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
            wait(1)
            print(
                f"                {person[0].split('@outlook.com')[0].split('@hotmail.com')[0]} waiting for thread")
        print(f" starting thread ({threadcount+1}/{maxthreads})")
        threading.Thread(target=lambda: rich(person[0], person[1])).start()
        threadcount += 1
