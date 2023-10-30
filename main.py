import pygame, random, asyncio  # Asnycio och dess metoder används för att kunna spela spelet
from sys import exit            # på webben från HTML-fil. Detta ledde till ännu lite rörigare
                                # kod och går att ta bort om man bara vill spela lokalt..
def player_animation():
    # Går om spelare är på marken
    # Hoppar om spelaren hoppar
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.3
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()

# Grundparametrar för spelet
screen_width, screen_height = 800, 400     # Skärmstorlek
screen = pygame.display.set_mode((screen_width, screen_height)) # Skärmvariabel
pygame.display.set_caption("Krockes Quest: Meat your Destiny")    # Titel på spelskärm
clock = pygame.time.Clock()                # FPS variabel
test_font = pygame.font.Font(None, 50)     # Font & storlek för text (None kan ändras till önskad font)

# Tar in och ändrar stl på alla sprites för att springa
player_walk_1 = pygame.image.load("run_1.png").convert_alpha()
player_walk_1 = pygame.transform.scale(player_walk_1, (60, 60))
player_walk_2 = pygame.image.load("run_2.png").convert_alpha()
player_walk_2 = pygame.transform.scale(player_walk_2, (60, 60))
player_walk_3 = pygame.image.load("run_3.png").convert_alpha()
player_walk_3 = pygame.transform.scale(player_walk_3, (60, 60))
player_walk_4 = pygame.image.load("run_4.png").convert_alpha()
player_walk_4 = pygame.transform.scale(player_walk_4, (60, 60))
player_walk_5 = pygame.image.load("run_5.png").convert_alpha()
player_walk_5 = pygame.transform.scale(player_walk_5, (60, 60))
player_walk_6 = pygame.image.load("run_6.png").convert_alpha()
player_walk_6 = pygame.transform.scale(player_walk_6, (60, 60))
player_walk_7 = pygame.image.load("run_7.png").convert_alpha()
player_walk_7 = pygame.transform.scale(player_walk_7, (60, 60))
player_walk_8 = pygame.image.load("run_8.png").convert_alpha()
player_walk_8 = pygame.transform.scale(player_walk_8, (60, 60))
player_walk_9 = pygame.image.load("run_9.png").convert_alpha()
player_walk_9 = pygame.transform.scale(player_walk_9, (60, 60))
player_walk_10 = pygame.image.load("run_10.png").convert_alpha()
player_walk_10 = pygame.transform.scale(player_walk_10, (60, 60))
player_walk_11 = pygame.image.load("run_11.png").convert_alpha()
player_walk_11 = pygame.transform.scale(player_walk_11, (60, 60))
player_walk_12 = pygame.image.load("run_12.png").convert_alpha()
player_walk_12 = pygame.transform.scale(player_walk_12, (60, 60))

# Lista med index som används till animering av spelare
player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, 
            player_walk_6, player_walk_7, player_walk_8, player_walk_9, player_walk_10, 
            player_walk_11, player_walk_12]
player_index = 0
player_surf = player_walk[player_index]


async def main(): # Denna metod lades till för att kunna spela spelet som HTML-fil.

    # Dessa variabler är röriga framför allt efter importering av Asyncio, finns säkert dubletter nånstans..
    global double_jump, increase_speed, player_rect, player_jump, meat_height

    game_active, first_jump, double_jump, increase_speed, new_game = False, False, False, False, True
    carrot_move_speed, speed_up_counter, score_counter = 4, 0, 0

    score_surf = test_font.render(f"Score: {score_counter}", False, "Black")
    score_rect = score_surf.get_rect(midtop = (400,20))

    # Tar in alla sprites till spelet. Från början låg allt i mappar i ordning och reda men Asnycio
    # hade svårt att hitta bilderna om de inte låg brevid main.py tyvärr..
    sky_surf = pygame.image.load("sky.jpg").convert()

    ground_surf = pygame.image.load("ground2.jpg").convert()
    ground_rect = ground_surf.get_rect(midleft = (0, 380))

    carrot_surf = pygame.image.load("morot_long.png").convert_alpha()
    carrot_rect = pygame.Rect(screen_width,200,20,100)

    broccoli_surf = pygame.image.load("broccoli.png").convert_alpha()
    broccoli_rect = broccoli_surf.get_rect(midbottom = (screen_width,300))

    meat_height = 200
    meat_surf = pygame.image.load("meat.png").convert_alpha()
    meat_rect = meat_surf.get_rect(midbottom = (screen_width,200))

    # Custom 'hitbox' för spelaren så att kollisionen sker smidigare
    player_rect = pygame.Rect(80,200,50,50)

    # Tar in och ändrar stl för sprite för att hoppa
    player_jump = pygame.image.load("hopp_1.png").convert_alpha()
    player_jump = pygame.transform.scale(player_jump, (60, 60))

    player_grav = 0

    while True:
        # Gör så man kan avsluta spelet
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if new_game:# Denna körs bara när startskärmen körs

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT):
                    game_active = True
                    new_game = False

            if game_active: # Denna körs när ett spel körs

                # Speedar upp morot var 5e poäng man samlar in
                if speed_up_counter == 5:
                    carrot_move_speed += 2
                    speed_up_counter = 0

                # Mekanik för hopp och dubbelhopp
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_grav = -20
                        first_jump = True
                        double_jump = False
                    elif event.key == pygame.K_SPACE and first_jump:
                        player_grav = -15
                        double_jump = True
                        first_jump = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                    if player_rect.bottom == 300:
                        player_grav = -20
                        first_jump = True
                        double_jump = False
                    elif first_jump:
                        player_grav = -15
                        double_jump = True
                        first_jump = False

            else: # Denna körs när ett spel är över: Tryck för nytt spel, nollställ poäng
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT):

                    hiscores_list.sort(reverse = True)
                    hiscores_list = hiscores_list[:3]

                    with open("hiscore.txt", "w") as f:
                        for score in hiscores_list:
                            score = score.replace("<<<","")
                            f.write(f"{score}\n")

                    # Nollställer alla parametrar för nytt spel
                    broccoli_rect.x = screen_width
                    carrot_rect.x = screen_width
                    score_rect = score_surf.get_rect(midtop = (400,20))
                    score_counter = 0
                    speed_up_counter = 0
                    carrot_move_speed = 4
                    score_surf = test_font.render(f"Score: {score_counter}", False, "Black")
                    game_active = True

                # Tryck q för att avsluta, spara highscore i fil och stäng spel
                # Har ingen bra lösning för om man spelar på telefon ännu, eventuellt 
                # lägga till en liten quit-knapp på skärmen.
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    hiscores_list.sort(reverse = True)
                    hiscores_list = hiscores_list[:3]

                    with open("hiscore.txt", "w") as f:
                        for score in hiscores_list:
                            score = score.replace("<<<","")
                            f.write(f"{score}\n")

                    pygame.quit()
                    exit()

        # Startskärm vid uppstart av spel
        if new_game:
            screen.fill("Yellow")
            screen.blit(test_font.render("~ Krockes Quest: Meat your Destiny ~", False, "Black"),(90,50))
            screen.blit(test_font.render("Collect the meat, avoid the carrots!", False, "Black"),(120,100))
            screen.blit(test_font.render("Press [SPACEBAR] to play", False, "Black"), (190,150))

        if game_active:

            # Sätter ut bakgrund
            screen.blit(sky_surf, (0, 0))

            # Flyttar hindret åt vänster
            carrot_rect.x -= carrot_move_speed
            
            if carrot_rect.left <= -50:
                carrot_rect.x = random.randint(800, 1600)
                carrot_rect.y = random.randint(150,220)

            # Flyttar marken år vänster i takt med hindret
            ground_rect.x -= carrot_move_speed
            if ground_rect.left <= -210:
                ground_rect.midleft = (0,380)

            # Flyttar broccoli åt vänster dubbelt så snabbt som morot
            broccoli_rect.left -=  (carrot_move_speed + 4)
            if broccoli_rect.right <= -500:
                broccoli_rect.x = random.randint(800,1600)
                broccoli_rect.y = random.randint(50,250)

            # Flyttar köttbit åt vänster, randomiserar spawn
            meat_rect.x -=4
            if meat_rect.right <= -333:
                meat_rect.x = screen_width
                meat_rect.y = random.randint(50,250)

            # Sätter ut resterande objekt
            screen.blit(broccoli_surf, broccoli_rect)
            screen.blit(meat_surf, meat_rect)
            screen.blit(carrot_surf, carrot_rect)
            screen.blit(ground_surf, ground_rect)
            screen.blit(score_surf, score_rect)

            # Sköter spelaren
            player_grav += 1
            player_rect.y += player_grav
            if player_rect.bottom >= 300:
                player_rect.bottom = 300
            player_animation()
            screen.blit(player_surf, player_rect)

            # Respawna kött och lägg till poäng om man når köttbit
            if meat_rect.colliderect(player_rect):
                score_counter += 1
                speed_up_counter += 1
                meat_rect.x = -40
                score_surf = test_font.render(f"Score: {score_counter}", False, "Black")

            # Avslutar spel om man träffar moroten
            if carrot_rect.colliderect(player_rect) or broccoli_rect.colliderect(player_rect):
                game_active = False
                
        elif game_active == False and new_game == False:
            # Hämta highscore från fil
            with open("hiscore.txt", "r", encoding="utf-8") as f:
                hiscores_list = f.readlines()

            highscore_header_surf = test_font.render(f"Highscore:", False, "Black")
            highscore_header_rect = highscore_header_surf.get_rect(midtop = (400,175))

            # Game over skärmen
            screen.fill("Yellow")
            screen.blit(test_font.render("Press [SPACEBAR] to play again..", False, "Black"),(120,20))
            screen.blit(test_font.render("Press [Q] to quit", False, "Black"),(250,50))
            score_rect.midtop = (400,100)
            screen.blit(score_surf, score_rect)
            screen.blit(highscore_header_surf, highscore_header_rect)

            # Sköter highscore, SUPER RÖRIGT.
            # Läser in listan, konverterar, sorterar, lägger in ny highscore etc..
            scores_line_height = 30

            hiscores_list.append(score_counter)
            
            hiscores_list = [int(score) for score in hiscores_list]
            hiscores_list.sort(reverse=True)
            hiscores_list = hiscores_list[:3]

            hiscores_list = [str(score) for score in hiscores_list]

            new_highscore_bool = False
            for i, score in enumerate(hiscores_list):
                if not new_highscore_bool and int(score) == score_counter:
                    hiscores_list[i] = str(score) + "<<<"
                    new_highscore_bool = True

            hiscores_list = [str(score) for score in hiscores_list]
            hiscores_list = sorted(hiscores_list, key=lambda x: int(x.rstrip("<<<")), reverse=True)

            for n in range(3):
                score_rect = highscore_header_rect.copy()
                score_rect.top = 200 + (n + 1) * scores_line_height
                screen.blit(test_font.render(str(hiscores_list[n].replace("\n","")), False, "Black"), score_rect)
            
        # FPS för spelet
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)

asyncio.run(main()) # Denna metod lades till för att kunna spela spelet som HTML-fil.