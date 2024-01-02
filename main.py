import pygame
import draw
import cmpt120image
import random

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

print ("""MAIN MENU
1. Learn - Word Flash Cards
2. Play - Seek and Find Game
3. Settings - Change Difficulty
4. Exit
""")
response = int(input("Choose an option:").strip("."))
print("\n")

# initialize
file = open("blackfoot.csv")
n = 3

while response!=4:

    # Learn
    if response == 1:

        print("LEARN")
        print("\n")
        file.seek(0)

        for i in range(n):
            canvas = cmpt120image.getWhiteImage(400, 300)
            cmpt120image.showImage(canvas)
            
            word = file.readline().strip()
            img = cmpt120image.getImage("images/{}.png".format(word))

            draw.drawItem(canvas,img,random.randint(0,220),random.randint(0,320))
            cmpt120image.showImage(canvas)
            
            playSound(word,"i")

            input(str(i+1)+". Press Enter To Continue...")

        print("\n")
        print ("""MAIN MENU
1. Learn - Word Flash Cards
2. Play - Seek and Find Game
3. Settings - Change Difficulty
4. Exit
""")
        response = int(input("Choose an option: ").strip("."))
        print("\n")

    # Play

    # Initialize an empty list
    data_list = []

    file.seek(0)
    for line in file:
        data_list += line.strip().split(",")

    if response == 2:

        print('''PLAY
This is a seek and find game. You will hear a word.
Count how many of that item you find!
''')
    
        rounds = int(input("How many rounds would you like to play? ").strip(". ,"))
        learning_list = data_list[:n]
        canvas = cmpt120image.getWhiteImage(400,300)
        cmpt120image.showImage(canvas)
        for i in range(rounds):
            
            random.shuffle(learning_list)
            challenge_list = learning_list[0:3]
            canvas = cmpt120image.getWhiteImage(400,300)
            cmpt120image.showImage(canvas)
            answer = random.choice(challenge_list)
           
            for word in challenge_list:
                #random color
                r= random.randint(0,200)
                g=random.randint(0,200)
                b=random.randint(0,200)
                color = [r,g,b]
                img = cmpt120image.getImage("images/{}.png".format(word))
                
                item_number = random.randint(1,4)

                if word == answer:
                    answer_number = item_number

                new_img = draw.recolorImage(img,color)
                mirror_img = draw.mirror(new_img)
                minify_img = draw.minify(new_img)
                all_img = draw.minify(mirror_img)
                image = random.choice([minify_img, mirror_img, all_img])
                draw.distributeItems(canvas,image,item_number)
                cmpt120image.showImage(canvas)

            playSound(answer,"i")
            response = int(input("Listen to the word and how many of them can you find? "))
            if response == answer_number:
                input("Right! Press enter to continue")
            else:
                input("Sorry the correct answer is "+str(answer_number)+" .Press Enter to continue!")

        print("\n")
        print ("""MAIN MENU
1. Learn - Word Flash Cards
2. Play - Seek and Find Game
3. Settings - Change Difficulty
4. Exit
""")
        response = int(input("Choose an option: ").strip("."))
        print("\n")



    # Settings
    if response == 3:
        print("SETTINGS")
        print("\n")
        print("You are currently learning", n, "words")
        n = int(input("How many would you like to learn (3-12) "))
        if n > 12 or n < 3:
            print("Sorry, that's not a valid number. Resetting to 3 words.")
            n = 3

        print("\n")
        print ("""MAIN MENU
1. Learn - Word Flash Cards
2. Play - Seek and Find Game
3. Settings - Change Difficulty
4. Exit
""")
        response = int(input("Choose an option: ").strip("."))
        print("\n")

print("Goodbye!")
