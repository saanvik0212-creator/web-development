name = input("Please enter your name: ")
mood = input("What's your mood today? happy/sad/tired/stressed/excited: ")
energy = int(input("Enter your energy level from 1 to 10: "))
if energy < 3:
    print("Alert: You're on low energy today and have a relaxed break.")

if energy >= 10:
    print("You have enough energy to do something productive today!")
else:
    print("Take it slow today and do something relaxing.")

if mood == "happy":
    advice = "Keep being energetic and spread knowledge!"
elif mood == "sad":
    advice = "Have a talk with someone you like to share things and do something that makes you feel better."
elif mood == "tired":
    advice = "Eat food you like and take some rest."
elif mood == "stressed":
    advice = "Stop for a moment and think back what went wrong,and refresh yourself."
elif mood == "excited":
    advice = "Keep building new ideas and start without hesitation!"
else:
    advice = "It's okay, It doesn't matter what you were like today, what matters is only what you did ."

import datetime

today = datetime.datetime.now()

print("\n================================")
print("DAILY MOOD ADVISOR REPORT")
print("================================")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("================================")
