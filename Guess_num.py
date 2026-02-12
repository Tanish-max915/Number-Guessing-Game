# Always use pip install playsound 3 instead of pip install playsound [Doesnt work??]
import random
import time as t
import winsound

print("Game booting up.....")
num = random.randint(1, 11)
lives = 3
print("Game Begin!")
t.sleep(0.7)
print("The max number is 11!")
t.sleep(1)
print(f"Lives left: {lives}")
t.sleep(0.5)

# Always use snd #filename when using path and only wav files work. Also switch the \ to / or put r in front of ''
# Sounds?? --Done


def game(life):
    lives = 3
    while True:
        guess = int(input("Enter Guessed Number: "))
        t.sleep(0.5)
        if guess == num:
            print(f"Congrats! You guessed it right, The number was {num}.")
            break
        else:
            print("Wrong! Try again")
            lives -= 1
            t.sleep(0.5)
            print(f"Lives left: {lives}")

        if lives == 0:
            print("Game Over")
            print(f"The number was {num}")
            t.sleep(1)
            break

        elif lives == 2:
            numc1 = random.randint(1, 5)
            numc2 = random.randint(1, 5)
            print("Number is betwen", num - numc1, "and", num + numc2)

        elif lives == 1:
            numc3 = random.randint(1, 4)
            numc4 = random.randint(1, 4)
            print("Number is betwen", num - numc3, "and", num + numc4)

        else:
            print("System Error....")
            t.sleep(0.7)
            print("Rebooting....")
            winsound.PlaySound(
                "C:/Users/THANISH/Python/273736__squashy555__computer-startup.wav",
                winsound.SND_FILENAME,
            )
            t.sleep(0.5)
            quit("--File.exe Deleted--")


game(lives)

while True:
    cont = str(input("Would you like to countinue?(Y/n): "))
    if cont == "Y":
        num = random.randint(1, 11)
        lives = 3
        print("Game Begin!")
        t.sleep(0.7)
        print("The max number is 11!")
        t.sleep(1)
        print(f"Lives left: {lives}")
        t.sleep(0.5)

        game(lives)

    elif cont == "n":
        t.sleep(0.5)
        quit("Game quit...")

    else:
        print("System error....")
        t.sleep(0.3)
        print("Rebooting....")
        winsound.PlaySound(
            "C:/Users/THANISH/Python/273736__squashy555__computer-startup.wav",
            winsound.SND_FILENAME,
        )
        t.sleep(0.5)
        quit("--File.exe Deleted--")
