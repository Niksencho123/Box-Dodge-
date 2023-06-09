import pygame
import random
from pygame import locals
pygame.init()
DISPLAY = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Box Dodge")
Box1 = pygame.image.load("Assets/RTS_Crate_0.png")
pygame.display.set_icon(Box1)
Score = 0
difficulty = 0
BACKGROUND = pygame.image.load("Assets/high_mountain_nature_game_background_dribbble.webp")
Ground = pygame.image.load("Assets/Ground_floor.png").convert_alpha()
Ground_rect = Ground.get_rect(topleft=(0, 500))
Player = pygame.image.load("Assets/player_stand.png")
Player_scaled = pygame.transform.scale2x(Player)
Player_rect = Player.get_rect(midbottom=(100, 520))
Font1 = pygame.font.Font("Assets/ARCADECLASSIC.TTF", 50)
Font2 = pygame.font.Font("Assets/ARCADECLASSIC.TTF", 35)
Box2 = pygame.image.load("Assets/RTS_Crate_0.png")
Box3 = pygame.image.load("Assets/RTS_Crate_0.png")
Box1 = pygame.transform.scale(Box1, (100, 100))
Box2 = pygame.transform.scale(Box2, (100, 100))
Box3 = pygame.transform.scale(Box3, (100, 100))
y = 30
Played = 0
speed = 3
Box1_rect = Box1.get_rect(midbottom=(150, y))
Box2_rect = Box1.get_rect(midbottom=(100, y))
Box3_rect = Box1.get_rect(midbottom=(100, y))
Sign = Font1.render("Box Dodge", False, "Teal")
Sign1 = Font2.render("Press SPACE to start!", False, "Teal")
Sign2 = Font2.render(f"Score {Score}", False, "Black")
Sign3 = Font2.render(f"Your score is {Score}", False, "Teal")
Easy_sign = Font2.render("Easy", False, "Green")
Easy_sign_rect = Easy_sign.get_rect(bottomleft=(370, 150))
Medium_sign = Font2.render("Medium", False, "Yellow")
Medium_sign_rect = Easy_sign.get_rect(bottomleft=(370, 300))
Hard_sign = Font2.render("Hard", False, "Red")
Hard_sign_rect = Easy_sign.get_rect(bottomleft=(370, 450))
Sign_rect = Sign.get_rect(center=(400, 50))
Sign1_rect = Sign.get_rect(center=(350, 480))
FPS = pygame.time.Clock()
running = True
game = False
title = True
difficulty_choser = False
while running:
    Sign2 = Font2.render(f"Score  {Score}", False, "Black")
    if Score == 5:
        speed = 2 + difficulty
    if Score == 10:
        speed = 5 + difficulty
    if Score == 15:
        speed = 7 + difficulty
    if Score == 20:
        speed = 9 + difficulty
    if Score == 25:
        speed = 11 + difficulty
    if Score == 30:
        speed = 13 + difficulty
    if Score == 35:
        speed = 15 + difficulty
    if Score == 40:
        speed = 17 + difficulty
    if Score == 45:
        speed = 19 + difficulty
    if Score == 50:
        speed = 21 + difficulty
    if Score == 55:
        speed = 23 + difficulty
    if Score == 60:
        speed = 25 + difficulty
    if game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_d]:
            Player_rect.x += 10
        if key_pressed[pygame.K_a]:
            Player_rect.x -= 10
        if not Box1_rect.colliderect(Ground_rect):
            Box1_rect.y += speed
            Box2_rect.y += speed
            Box3_rect.y += speed
        else:
            Score += 1
            Box1_rect.y = -100
            Box1_rect.x = random.randint(0, 250)
            Box2_rect.y = -100
            Box2_rect.x = random.randint(300, 500)
            Box3_rect.y = -100
            Box3_rect.x = random.randint(600, 800)
        DISPLAY.blit(BACKGROUND, (0, 0))
        DISPLAY.blit(Ground, (0, 500))
        DISPLAY.blit(Player, Player_rect)
        DISPLAY.blit(Box1, Box1_rect)
        DISPLAY.blit(Box2, Box2_rect)
        DISPLAY.blit(Box3, Box3_rect)
        DISPLAY.blit(Sign2, (310, 560))
        pygame.display.flip()
        if Player_rect.x < -10:
            Player_rect.x = 800
        if Player_rect.x > 810:
            Player_rect.x = 0
        if Player_rect.colliderect(Box1_rect):
            game = False
            title = True
            Played += 1
            Sign3 = Font2.render(f"Your score is {Score}", False, "Teal")
        if Player_rect.colliderect(Box2_rect):
            game = False
            title = True
            Played += 1
            Sign3 = Font2.render(f"Your score is {Score}", False, "Teal")
        if Player_rect.colliderect(Box3_rect):
            game = False
            title = True
            Played += 1
            Sign3 = Font2.render(f"Your score is {Score}", False, "Teal")
        FPS.tick(60)
    elif title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                title = False
                difficulty_choser = True
        DISPLAY.fill((31, 147, 167))
        DISPLAY.blit(Sign, Sign_rect)
        if Played == 0:
            DISPLAY.blit(Sign1, Sign1_rect)
        else:
            DISPLAY.blit(Sign3, (Sign1_rect.x + 40,Sign1_rect.y))
        DISPLAY.blit(Player_scaled, (330, 200))
        pygame.display.flip()
    elif difficulty_choser:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        DISPLAY.fill((31, 147, 167))
        DISPLAY.blit(Easy_sign, Easy_sign_rect)
        DISPLAY.blit(Medium_sign, Medium_sign_rect)
        DISPLAY.blit(Hard_sign, Hard_sign_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and Easy_sign_rect.collidepoint(pygame.mouse.get_pos()):
                difficulty = 3
                difficulty_choser = False
                game = True
                Score = 0
                speed = 3
                Box1_rect.y = -100
                Box1_rect.x = random.randint(0, 250)
                Box2_rect.y = -100
                Box2_rect.x = random.randint(300, 500)
                Box3_rect.y = -100
                Box3_rect.x = random.randint(600, 800)
                Player_rect.x = 400
            if event.type == pygame.MOUSEBUTTONDOWN and Medium_sign_rect.collidepoint(pygame.mouse.get_pos()):
                difficulty = 5
                difficulty_choser = False
                game = True
                Score = 0
                speed = 3
                Box1_rect.y = -100
                Box1_rect.x = random.randint(0, 250)
                Box2_rect.y = -100
                Box2_rect.x = random.randint(300, 500)
                Box3_rect.y = -100
                Box3_rect.x = random.randint(600, 800)
                Player_rect.x = 400
            if event.type == pygame.MOUSEBUTTONDOWN and Hard_sign_rect.collidepoint(pygame.mouse.get_pos()):
                difficulty = 7
                difficulty_choser = False
                game = True
                Score = 0
                speed = 3
                Box1_rect.y = -100
                Box1_rect.x = random.randint(0, 250)
                Box2_rect.y = -100
                Box2_rect.x = random.randint(300, 500)
                Box3_rect.y = -100
                Box3_rect.x = random.randint(600, 800)
                Player_rect.x = 400
        pygame.display.flip()
pygame.quit()