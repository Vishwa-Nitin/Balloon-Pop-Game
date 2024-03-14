import sys
from button import Button
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Balloon Pop-UP")

BG = pygame.image.load("assets/background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/vaca.ttf", size)


def balloon():

    # Initialize
    pygame.init()
    sfx_volume = 0.0

    # Create Window/Display
    width, height = 1280, 720
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop Game")


    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()

    # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # width
    cap.set(4, 720)  # height

    # Images
    imgBalloon = pygame.image.load('assets/BalloonRed.png').convert_alpha()
    # imgBalloon = pygame.image.load('blueBalloon (1).png').convert_alpha()
    rectBalloon = imgBalloon.get_rect()

    rectBalloon.x, rectBalloon.y = 500, 300



    # Variables
    speed = 15
    score = 0
    startTime = time.time()
    totalTime = 60

    # Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    def resetBalloon():
        rectBalloon.x = random.randint(100, img.shape[1] - 100)
        rectBalloon.y = img.shape[0] + 50

    # Main loop
    start = True
    while start:
        # Get Events
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         start = False
        #         pygame.quit()

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # Apply Logic
        timeRemain = int(totalTime - (time.time() - startTime))
        if timeRemain < 0:
            window.fill((255, 255, 255))

            font = pygame.font.Font('assets/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time UP', True, (50, 50, 255))
            window.blit(textScore, (450, 350))
            window.blit(textTime, (530, 275))
            image = pygame.image.load('assets/Restart.jpg')

# Set the size for the image
            DEFAULT_IMAGE_SIZE = (100, 100)

            # Scale the image to your needed size
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)





            OPTIONS_Restart = Button(image, pos=(640,560),text_input="",
                               font=get_font(60), base_color="Black", hovering_color="Light Green")




            OPTIONS_Restart.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_Restart.update(SCREEN)
            cap.release()

            # if int(score) >= 30:
            #         print("Passed")
            # else :
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_Restart.checkForInput(OPTIONS_MOUSE_POS):
                               main_menu()


           # return "Finished"

        else:
            # OpenCV
            success, img = cap.read()
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)

            rectBalloon.y -= speed  # Move the balloon up

            # check if balloon has reached the top without pop
            if rectBalloon.y < 0 :
                resetBalloon()
                speed += 1



            if hands:
                hand = hands[0]

                x, y = hand['lmList'][8][0:2]

                if rectBalloon.collidepoint(x, y):
                    resetBalloon()
                    score += 10
                    speed += 1


            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)

            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)


            font = pygame.font.Font('assets/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Score: {score}', True, (255,255,255))
            textTime = font.render(f'Time: {timeRemain}', True, (255,255,255))
            window.blit(textScore, (35, 35))
            window.blit(textTime, (1000, 35))

        # Update Display
        pygame.display.update()
        # Set FPS
        clock.tick(fps)




def balloon1():
    # Initialize
    pygame.init()

    # Create Window/Display
    width, height = 1280, 720
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Balloon Pop Game")

    # Initialize Clock for FPS
    fps = 30
    clock = pygame.time.Clock()

    # Webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)  # width
    cap.set(4, 720)  # height

    # Images
    imgBalloon = pygame.image.load('assets/BalloonRed.png').convert_alpha()

    rectBalloon = imgBalloon.get_rect()

    rectBalloon.x, rectBalloon.y = 500, 300
    imgBalloon1 = pygame.image.load('assets/blueballoon (1).png').convert_alpha()

    rectBalloon1 = imgBalloon1.get_rect()

    rectBalloon1.x, rectBalloon1.y = 400, 300

    imgBalloon2 = pygame.image.load('assets/green_balloon.png').convert_alpha()

    rectBalloon2 = imgBalloon2.get_rect()

    rectBalloon2.x, rectBalloon2.y = 600, 300


    # Variables
    speed = 15
    score = 0
    startTime = time.time()
    totalTime = 60

    # Detector
    detector = HandDetector(detectionCon=0.8, maxHands=1)

    def resetBalloon():
        rectBalloon.x = random.randint(100, img.shape[1] - 100)
        rectBalloon.y = img.shape[0] + 50
    def resetBalloon1():
        rectBalloon1.x = random.randint(100, img.shape[1] - 100)
        rectBalloon1.y = img.shape[0] + 50

    def resetBalloon2():
        rectBalloon2.x = random.randint(100, img.shape[1] - 100)
        rectBalloon2.y = img.shape[0] + 50
    # Main loop
    start = True
    while start:
        # Get Events
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         start = False
        #         pygame.quit()
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        # Apply Logic
        timeRemain = int(totalTime - (time.time() - startTime))
        if timeRemain < 0:
            window.fill((255, 255, 255))

            font = pygame.font.Font('assets/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time UP', True, (50, 50, 255))
            window.blit(textScore, (450, 350))
            window.blit(textTime, (530, 275))
            image = pygame.image.load('Restart.jpg')

# Set the size for the image
            DEFAULT_IMAGE_SIZE = (100, 100)

            # Scale the image to your needed size
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

            # Set a default position



            OPTIONS_Restart = Button(image, pos=(640,560),
                              text_input="", font=get_font(75), base_color="Black", hovering_color="Light Green")



            OPTIONS_Restart.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_Restart.update(SCREEN)
            cap.release()
            # if int(score) >= 30:
            #         print("Passed")
            # else :
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_Restart.checkForInput(OPTIONS_MOUSE_POS):
                                main_menu()
           # return "Finished"

        else:
            # OpenCV
            success, img = cap.read()
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)

            rectBalloon.y -= speed  # Move the balloon up
            rectBalloon1.y -= speed
            rectBalloon2.y -= speed
            # check if balloon has reached the top without pop
            if rectBalloon.y < 0 :
                resetBalloon()
                speed += 1
            if rectBalloon1.y < 0 :
                resetBalloon1()
                speed += 1
            if rectBalloon2.y < 0 :
                resetBalloon2()
                speed += 1


            if hands:
                hand = hands[0]
                x, y = hand['lmList'][8][0:2]

                if rectBalloon.collidepoint(x, y):
                    resetBalloon()
                    score += 10
                    speed += 1
                if rectBalloon1.collidepoint(x, y):
                    resetBalloon1()
                    score += 10
                    speed += 1
                if rectBalloon2.collidepoint(x, y):
                    resetBalloon2()
                    score += 10
                    speed += 1

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            imgRGB1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # imgRGB1 = np.rot90(imgRGB)
            # frame1 = pygame.surfarray.make_surface(imgRGB1).convert()
            # frame1 = pygame.transform.flip(frame1, True, False)
            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)
            # window.blit(frame, (0, 0))
            window.blit(imgBalloon1, rectBalloon1)
            window.blit(imgBalloon2, rectBalloon2)

            font = pygame.font.Font('assets/Marcellus-Regular.ttf', 50)
            textScore = font.render(f'Score: {score}', True, (255,255,255))
            textTime = font.render(f'Time: {timeRemain}', True, (255,255,255))
            window.blit(textScore, (35, 35))
            window.blit(textTime, (1000, 35))

        # Update Display
        pygame.display.update()
        # Set FPS
        clock.tick(fps)






def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        SCREEN.blit(balloon())

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def options():
    # BG = pygame.image.load("assets/background.png")
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()



        BG = pygame.image.load("assets/background.png")
        SCREEN.fill("white")
        OPTIONS_Level1 = Button(image=None, pos=(640,200),
                              text_input="Level 1", font=get_font(75), base_color="Black", hovering_color="Light Green")


        OPTIONS_Level1.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Level1.update(SCREEN)
        OPTIONS_Level2 = Button(image=None, pos=(640,300),
                              text_input="Level 2", font=get_font(75), base_color="Black", hovering_color="Light Green")


        OPTIONS_Level2.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Level2.update(SCREEN)


        #SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 500),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Light Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_Level1.checkForInput(OPTIONS_MOUSE_POS):
                    balloon()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_Level2.checkForInput(OPTIONS_MOUSE_POS):
                    balloon1()



        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
