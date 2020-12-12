# Secret Santa! (Day 6)
# Challenge :
# Write a program that, after inputting all members, generates a secret santa ‘sequence’. For those who don’t know what secret santa is: you get a random name (which is not yourself) for whom you have to buy a present. Everyone should get a present from 1 person and everyone should have to buy a present for 1.
# This is a hard challenge, and as such is worth 5 points. The next hard challenge will be on the 12th
import random

def print_pair(giver,receiver,max_length,is_header=False):
    s = "{} | {}".format(giver + (" " * (max_length - len(giver))),receiver)
    print(s)
    if is_header:
        print("-" * len(s))

names = input("Who are the participants? Enter all names separated by commas\n>> ")
names = [x.strip() for x in names.split(",")]
random.shuffle(names)
max_length = max(max(len(x) for x in names),len('giver'))
giver = names.pop()
first_giver = giver
print_pair("giver","receiver",max_length,True)
while len(names) > 0:
    receiver = names.pop()
    print_pair(giver,receiver,max_length)
    giver = receiver
print_pair(giver,first_giver,max_length)