import random

versuche = 0
name = (input('Dein Name : '))

print("""
\033[38;5;46mHerzlich Wilkommen zu unserem Spiel,
      """)
print("""\033[38;5;46mWollen sie die Regeln erklärt bekommen?
Wenn Ja, dann antworten sie mit Ja und wenn Sie sie nicht erklärt bekommen wollen, antworten sie mit Nein.""")

rulewhile = 0

while rulewhile == 0:

    rules = input("Ja oder Nein : ")

    if rules == "JA".lower():

        print("""Das Spiel ist ganz einfach, wir suchen uns eine zufällige Zahl zwischen 1 und 100 aus und sie müssen sie erraten. 
!!!Sie haben 15 Versuche und bei dem 10 Versuch können sie sich einen Tipp holen!!!

Also los gehts!!!
""")

    rulewhile = 2

    if rules == "NEIN".lower():
        print("Sehr schön, dann wird nun alles vorbereitet!")
        rulewhile = "Nein"

    if rules != "JA".lower() and rules != "NEIN".lower():
        print("Tut mir leid, das konnte ich nicht erkennen! Schreibe bitte erneut, ob du die Regeln erklärt haben möchtest!")
        input("Ja oder Nein : ")


result = random.randint(1, 100)

for versuche in range(15):
    if versuche == 10:
        print("Willst du einen Tipp?")
        ftipp = input("Ja oder Nein :")
        while (ftipp != "Ja" and ftipp != "Nein"):
            ftipp = input()

        if ftipp == "Ja":

            tipp = random.randint(5, 15)
            print(f"\033[36mDie Zahl liegt zwischen {result - tipp} und {result + 20 - tipp}")

    number = input("Eine Zahl bitte : ")
    number = int(number)

    if number > 100:
        print("Gebe bitte eine Zahl zwischen 1 und 100 ein")

    if number > result:
        print("Deine Zahl ist größer, als die zufällige Zahl")

    if number < result:
        print("Deine Zahl ist kleiner, als die zufällige Zahl")

    if number == result:
        break

if number == result:
    versuche = str(versuche + 1)
    print("Gut gemacht!!! " + name + ' du hast meine Zahl in ' + versuche + " Versuchen erraten ")

if number != result:
    number = str(number)
    print("Das war nicht die Zufällige Zahl, das Spiel wurde wegen 13 fehversuchen abgebrochen ")
    print(f"Die Zufällige Zahl war {result}")

