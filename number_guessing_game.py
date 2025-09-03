import random
random_integer = random.randint(1, 50)
s = random_integer

playernum = int(input("Enter your guess: "))
count=0
while playernum != s:
    if playernum > s:
        print("Guess lower")
        count+=1
    elif playernum < s:
        print("Guess higher")
        count+=1
    playernum = int(input("Enter your guess: "))

print("Correct!")
count+=1
print ("Total attempts", count)