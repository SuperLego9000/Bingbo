import subprocess as subp
import data.JsonUtils as jsu
import threading
from time import sleep as wait
from os import system as sys
print("[40m[97m")
sys("cls")
def rich(user, key):
    print(f"[35mclaiming points for user: {user}[97m")
    try:
        subp.run(
            f"cmd /c python data\BingRewards\BingRewards.py -r -hl -e {user} -p {key} -d chrome"
        )
        print(f"[93mclaimed available points for user: {user}[97m")
    except:
        print("ERROR>OH GOD WHAT DID YOU DO?")


data = "settings.json"
data = jsu.read(data)
if data == []:
    raise(ValueError("no users in database"))
for _, person in enumerate(data):
    if person[2]:
        for i in range(3):
            rich(person[0], person[1])