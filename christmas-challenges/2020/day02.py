# Crackers!
# Challenge :
# Write a program that plays christmas crackers with you - that is a program that asks if you want to pull a cracker with it and if so outputs a random prize & joke (the jokes have to be good, or else...)
import random
import requests

def get_joke():
    headers = {"Accept":"text/plain","Accept-Charset":"UTF-8"}
    req = requests.get("https://icanhazdadjoke.com/",headers=headers)
    return req.text

res = input("Does polly want a cracker? [y/N]\n>> ")
num = random.uniform(0.,1.)
if res.lower() in ["y","yes"]:
    if num < 0.75:
        print(f"Here's your cracker:\n{get_joke()}")
    else:
        print("No! No cracker for you!")
elif num < 0.5:
    print(f"Take the damn cracker:\n{get_joke()}")
else:
    print("Ok bai :(")