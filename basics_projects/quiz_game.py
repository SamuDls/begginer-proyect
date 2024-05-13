print("Hello wellcome to the Quiz Game")

start = input("Do you want to play? yes or no ").lower()

if start != "yes":
    quit()
else:
    print("Nice let's  started")
    score = 0

answer = input("¿What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct you earn 1 point")
    score += 1
else:
    print("Incorrect")

answer = input("¿What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct you earn 1 point")
    score += 1
else:
    print("Incorrect")

answer = input("¿What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct you earn 1 point")
    score += 1
else:
    print("Incorrect")

answer = input("¿What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct you earn 1 point")
    score += 1
else:
    print("Incorrect")

print("Your final score was " + str(score) + " point")