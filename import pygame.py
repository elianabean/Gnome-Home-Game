import pygame
from sys import exit 

pygame.init() 
screen = pygame.display.set_mode((600, 600)) 
screen.fill('white') # put in background image
pygame.display.set_caption('Gnome Home Crisis') 
clock = pygame.time.Clock()

text_font = pygame.font.Font(None, 50) 
text_welcome = text_font.render('The Gnome Home Crisis', True, 'Orange')
text_welcome_rect = text_welcome.get_rect(midbottom = (300, 200))

text_font = pygame.font.Font(None, 30)
text_begin = text_font.render('Press SPACE to begin', True, 'Black')
text_begin_rect = text_begin.get_rect(midbottom = (300, 300))

player = pygame.image.load('export.PNG').convert_alpha() 
player = pygame.transform.rotozoom(player, 0.15, 0.15)  
player_rect = player.get_rect(center = (300, 500))

egghouse = pygame.image.load('egghouse.png').convert_alpha()
egghouse = pygame.transform.rotozoom(egghouse, 0.2, 0.2)
egghouse_rect = egghouse.get_rect(midbottom = (440,575))

stump = pygame.image.load('stump.png').convert_alpha()
stump = pygame.transform.rotozoom(stump, 0.3, 0.3)
stump_rect = stump.get_rect(midbottom = (150,485))

mushroom = pygame.image.load('mushroom.png').convert_alpha()
mushroom = pygame.transform.rotozoom(mushroom, 0.3, 0.3)
mushroom_rect = mushroom.get_rect(midbottom = (500, 200))

stone = pygame.image.load('stone.png').convert_alpha()
stone = pygame.transform.rotozoom(stone, 0.3, 0.3)
stone_rect = stone.get_rect(midbottom = (100, 200))

gnome_main = pygame.image.load('startplayer.PNG').convert_alpha() 
gnome_main = pygame.transform.rotozoom(gnome_main, 0.2, 0.2)  
gnome_main_rect = gnome_main.get_rect(midbottom = (300, 500))

endplayer = pygame.image.load('player.png').convert_alpha()
endplayer = pygame.transform.rotozoom(endplayer, 0.2, 0.2)
endplayer_rect = endplayer.get_rect(midbottom = (300, 500))

bg_home = pygame.image.load('homebg.png').convert_alpha()
bg_home = pygame.transform.rotozoom(bg_home, 0.3, 0.3)
bg_home_rect = bg_home.get_rect(topleft = (0, 0))

bg_surf = pygame.image.load('export.jpeg').convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0.6, 0.6)
bg_surf_rect = bg_surf.get_rect(topleft = (0,0))

inegghouse = pygame.image.load('inegghouse.png').convert_alpha()
inegghouse = pygame.transform.rotozoom(inegghouse, 0.3, 0.3)   
inegghouse_rect = inegghouse.get_rect(topleft = (0,0))

waterfountain = pygame.image.load('waterfountain.png').convert_alpha()
waterfountain = pygame.transform.rotozoom(waterfountain, 0.3, 0.3)
waterfountain_rect = waterfountain.get_rect(midbottom = (30, 400))
    
computer = pygame.image.load('computer.png').convert_alpha()
computer = pygame.transform.rotozoom(computer, 0.3, 0.3)
computer_rect = computer.get_rect(midbottom = (560, 350))
    
lamp = pygame.image.load('lamp.png').convert_alpha()
lamp = pygame.transform.rotozoom(lamp, 0.3, 0.3)
lamp_rect = lamp.get_rect(midbottom = (525, 580))

toaster = pygame.image.load('toaster.png').convert_alpha()
toaster = pygame.transform.rotozoom(toaster, 0.6, 0.6)
toaster_rect = toaster.get_rect(midbottom = (20, 500))

inegghousefull = pygame.image.load('inegghousefull.jpeg').convert_alpha()
inegghousefull = pygame.transform.rotozoom(inegghousefull, 0.6, 0.6)   
inegghousefull_rect = inegghousefull.get_rect(topleft = (0,0))

seed = pygame.image.load('seed.png').convert_alpha()
seed = pygame.transform.rotozoom(seed, 0.6, 0.6)
seed_rect = seed.get_rect(midbottom = (30, 500))

can = pygame.image.load('can.png').convert_alpha()
can = pygame.transform.rotozoom(can, 0.5, 0.5)
can_rect = can.get_rect(midbottom=(30, 490))

bottle = pygame.image.load('bottle.png').convert_alpha()
bottle = pygame.transform.rotozoom(bottle, 0.5, 0.5)
bottle_rect = bottle.get_rect(midbottom=(100, 300))

paper = pygame.image.load('paper.png').convert_alpha()
paper = pygame.transform.rotozoom(paper, 0.5, 0.5)
paper_rect = paper.get_rect(midbottom=(475, 225))

bin = pygame.image.load('bin.png').convert_alpha()
bin = pygame.transform.rotozoom(bin, 0.5, 0.5)
bin_rect = bin.get_rect(midbottom=(325, 250))

hole = pygame.image.load('hole.png').convert_alpha()
hole = pygame.transform.rotozoom(hole, 1, 1)
hole_rect = hole.get_rect(midbottom = (525, 400))

tree = pygame.image.load('tree.png').convert_alpha()
tree = pygame.transform.rotozoom(tree, 1.5, 1.5)
tree_rect = tree.get_rect(midbottom = (525, 410))

sentiment1 = False
instructions = False
beginning = False
inside = False
inside_egghouse = False
inside_mushroom = False
inside_stone = False
inside_stump = False
lampd = True
fountd = True
compd = True
toasterd = True
lampd2 = True
compd2 = True
toasterd2 = True
seedd = True
finishegghouse = False
finishmushroom = False
finishstone = False
finishstump = False
can_r = True
bottle_r = True
paper_r = True
count_recycle = 0
canrr = False
bottler = False
paperr = False
treeclick = False
finishseed = False

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    
    if(sentiment1):
        sentiment1 = pygame.image.load('Avgmonth.png').convert_alpha()
        sentiment1_rect = sentiment1.get_rect(topleft = (0,70))
        sentiment1 = pygame.transform.rotozoom(sentiment1, 0.51, 0.51)  
        screen.blit(sentiment1, sentiment1_rect)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            instructions = True
            beginning = False

    if(instructions):
      instruction = pygame.image.load('instructions2.png').convert_alpha()
      instruction_rect = instruction.get_rect(topleft = (0,0))
      screen.blit(instruction, instruction_rect)

      if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        beginning = True
        instructions = False 

    if(beginning):
      if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP and pygame.Rect.colliderect(player_rect, stump_rect):
            player_rect.y += 0
            inside_stump = True
            beginning = False
        elif event.key == pygame.K_UP and pygame.Rect.colliderect(player_rect, stone_rect):
            player_rect.y += 0
            inside_stone = True
            beginning = False
        elif event.key == pygame.K_UP and pygame.Rect.colliderect(player_rect, mushroom_rect):
            player_rect.y += 0
            inside_mushroom = True
            beginning = False
        elif event.key == pygame.K_UP and pygame.Rect.colliderect(player_rect, egghouse_rect):
            player_rect.y += 0
            inside_egghouse = True
            beginning = False
        elif event.key == pygame.K_UP:
            player_rect.y -= 32

        if event.key == pygame.K_DOWN and pygame.Rect.colliderect(player_rect, stump_rect):
            player_rect.y += 0
            inside_stump = True
            beginning = False
        elif event.key == pygame.K_DOWN and pygame.Rect.colliderect(player_rect, stone_rect):
            player_rect.y += 0
            inside_stone = True
            beginning = False
        elif event.key == pygame.K_DOWN and pygame.Rect.colliderect(player_rect, mushroom_rect):
            player_rect.y += 0
            inside_mushroom = True
            beginning = False
        elif event.key == pygame.K_DOWN and pygame.Rect.colliderect(player_rect, egghouse_rect):
            player_rect.y += 0
            inside_egghouse = True
            beginning = False
        elif event.key == pygame.K_DOWN:
            player_rect.y += 32
            
        if event.key == pygame.K_LEFT and pygame.Rect.colliderect(player_rect, stump_rect):
            player_rect.x += 0
            inside_stump = True
            beginning = False
        elif event.key == pygame.K_LEFT and pygame.Rect.colliderect(player_rect, stone_rect):
            player_rect.x += 0
            inside_stone = True
            beginning = False
        elif event.key == pygame.K_LEFT and pygame.Rect.colliderect(player_rect, mushroom_rect):
            player_rect.x += 0
            inside_mushroom = True
            beginning = False
        elif event.key == pygame.K_LEFT and pygame.Rect.colliderect(player_rect, egghouse_rect):
            player_rect.x += 0
            inside_egghouse = True
            beginning = False
        elif event.key == pygame.K_LEFT:
            player_rect.x -= 32

        if event.key == pygame.K_RIGHT and pygame.Rect.colliderect(player_rect, stump_rect):
            player_rect.x += 0
            inside_stump = True
            beginning = False
        elif event.key == pygame.K_RIGHT and pygame.Rect.colliderect(player_rect, stone_rect):
            player_rect.x += 0
            inside_stone = True
            beginning = False
        elif event.key == pygame.K_RIGHT and pygame.Rect.colliderect(player_rect, mushroom_rect):
            player_rect.x += 0
            inside_mushroom = True
            beginning = False
        elif event.key == pygame.K_RIGHT and pygame.Rect.colliderect(player_rect, egghouse_rect):
            player_rect.x += 0
            inside_egghouse = True
            beginning = False
        elif event.key == pygame.K_RIGHT:
            player_rect.x += 32

        screen.blit(player, (player_rect.x, player_rect.y))
          
    else:  
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        sentiment1 = True

    if (beginning):
      screen.blit(bg_surf, bg_surf_rect) 
      screen.blit(player, player_rect)
      screen.blit(egghouse, egghouse_rect)
      screen.blit(stump, stump_rect)
      screen.blit(mushroom, mushroom_rect)
      screen.blit(stone, stone_rect)
      screen.blit(hole, hole_rect)
      if finishseed:
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (hole_rect.collidepoint(event.pos)):
                treeclick = True
        if (treeclick):
            screen.blit(tree, tree_rect)
            finishstone = True


    if(inside_egghouse or inside_mushroom):
        lampdone = pygame.image.load('lampdone.png').convert_alpha()
        lampdone = pygame.transform.rotozoom(lampdone, 0.3, 0.3)
        lampdone_rect = lampdone.get_rect(midbottom = (525, 580))

        computerdone = pygame.image.load('computerdone.png').convert_alpha()
        computerdone = pygame.transform.rotozoom(computerdone, 0.3, 0.3)
        computerdone_rect = computerdone.get_rect(midbottom = (560, 350))

        waterfountaindone = pygame.image.load('waterfountaindone.png').convert_alpha()
        waterfountaindone = pygame.transform.rotozoom(waterfountaindone, 0.3, 0.3)
        waterfountaindone_rect = waterfountaindone.get_rect(midbottom = (30, 400))

        toasterdone = pygame.image.load('toasterdone.png').convert_alpha()
        toasterdone = pygame.transform.rotozoom(toasterdone, 0.6, 0.6)
        toasterdone_rect = toasterdone.get_rect(midbottom = (20, 500))

        screen.blit(inegghouse, inegghouse_rect)
        screen.blit(player, player_rect)

    if(inside_egghouse):
        text_font = pygame.font.Font(None, 30)
        text_begin = text_font.render('Click on objects to turn them off!', True, 'Black')
        text_begin_rect = text_begin.get_rect(midbottom = (300, 590))
        screen.blit(text_begin, text_begin_rect)
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (lamp_rect.collidepoint(event.pos)):
                screen.blit(lampdone, lampdone_rect)
                lampd= False
            elif computer_rect.collidepoint(event.pos):
                screen.blit(computerdone, computerdone_rect)
                compd=False
            elif waterfountain_rect.collidepoint(event.pos):
                screen.blit(waterfountaindone, waterfountaindone_rect)
                fountd=False
        if (fountd):
            screen.blit(waterfountain, waterfountain_rect)
        if (compd):
            screen.blit(computer, computer_rect)
        if (lampd):
            screen.blit(lamp, lamp_rect)
        if (not fountd):
            screen.blit(waterfountaindone, waterfountaindone_rect)
        if (not compd):
            screen.blit(computerdone, computerdone_rect)
        if (not lampd):
            screen.blit(lampdone, lampdone_rect)
        if(not fountd and not compd and not lampd):
            inside_egghouse = False
            beginning = True
            player_rect = player.get_rect(midbottom = (300, 500))
            inside = False
            finishegghouse = True

    if (inside_mushroom):
        text_font = pygame.font.Font(None, 30)
        text_begin = text_font.render('Click on objects to unplug them!', True, 'Black')
        text_begin_rect = text_begin.get_rect(midbottom = (300, 590))
        screen.blit(text_begin, text_begin_rect)
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (lamp_rect.collidepoint(event.pos)):
                screen.blit(lampdone, lampdone_rect)
                lampd2= False
            elif computer_rect.collidepoint(event.pos):
                screen.blit(computerdone, computerdone_rect)
                compd2=False
            elif toaster_rect.collidepoint(event.pos):
                screen.blit(toasterdone, toasterdone_rect)
                toasterd2=False

        if (fountd):
            screen.blit(waterfountain, waterfountain_rect)
        if (compd2):
            screen.blit(computer, computer_rect)
        if (lampd2):
            screen.blit(lamp, lamp_rect)
        if(toasterd2):
            screen.blit(toaster, toaster_rect)
        if (not fountd):
            screen.blit(waterfountaindone, waterfountaindone_rect)
        if (not compd2):
            screen.blit(computerdone, computerdone_rect)
        if (not lampd2):
            screen.blit(lampdone, lampdone_rect)
        if (not toasterd2):
            screen.blit(toasterdone, toasterdone_rect)
        if(not compd2 and not lampd2 and not toasterd2):
            inside_mushroom = False
            beginning = True
            player_rect = player.get_rect(midbottom = (300, 500))
            inside = False
            finishmushroom = True

    elif(inside_stone or inside_stump):
        screen.blit(inegghousefull, inegghousefull_rect)
        screen.blit(player, (300, 400))

    if(inside_stone):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (seed_rect.collidepoint(event.pos)):
                screen.blit(inegghousefull, inegghousefull_rect)
                screen.blit(player, (300, 400))
                seedd = False
        if(seedd):
            text_font = pygame.font.Font(None, 30) 
            text_welcome = text_font.render('Click the seed!', True, 'Black')
            text_welcome_rect = text_welcome.get_rect(midbottom = (350, 250))
            screen.blit(text_welcome, text_welcome_rect)
            screen.blit(seed, seed_rect)
        if(not seedd):
            screen.blit(inegghousefull, inegghousefull_rect)
            screen.blit(player, (300, 400))
            text_congrats = text_font.render('You found the seed!', True, 'Black')
            text_congrats_rect = text_congrats.get_rect(midbottom = (340, 250))
            screen.blit(text_congrats, text_congrats_rect)
            text_nextstep = text_font.render('Press SPACE to go outside', True, 'Black')
            text_nextstep_rect = text_nextstep.get_rect(midbottom = (300, 400))
            screen.blit(text_nextstep, text_nextstep_rect)
            text_next = text_font.render('Click on the hole to plant the tree', True, 'Black')
            text_next_rect = text_next.get_rect(midbottom = (300, 575))
            screen.blit(text_next, text_next_rect)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                text_nextstep = text_font.render('hello', True, 'Black')
                text_nextstep_rect = text_nextstep.get_rect(midbottom = (300, 475))
                screen.blit(text_nextstep, text_nextstep_rect)
                inside_stone = False
                beginning = True
                player_rect = player.get_rect(midbottom = (300, 500))
                inside = False
                finishseed = True

    if(inside_stump):
        screen.blit(can, can_rect)
        screen.blit(bottle, bottle_rect)
        screen.blit(paper, paper_rect)
        screen.blit(bin, bin_rect)
        text_font = pygame.font.Font(None, 30) 
        text_tex = text_font.render('Recycle the 3 items by clicking on them!', True, 'Black')
        text_tex_rect = text_tex.get_rect(midbottom = (250, 400))
        screen.blit(text_tex, text_tex_rect)

        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (can_rect.collidepoint(event.pos)):
                canrr = True
                
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (bottle_rect.collidepoint(event.pos)):
                bottler = True
        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (paper_rect.collidepoint(event.pos)):
                paperr = True
        if(canrr and bottler and paperr):
            inside_stump = False
            beginning = True
            player_rect = player.get_rect(midbottom = (300, 500))
            inside = False
            finishstump = True
     
  if beginning == False and instructions == False and inside_egghouse == False and inside_stump == False and inside_mushroom == False and inside_stone == False and sentiment1 == False:
    screen.blit(bg_home, bg_home_rect)
    screen.blit(text_welcome, text_welcome_rect)
    screen.blit(text_begin, text_begin_rect)
    screen.blit(gnome_main, gnome_main_rect)

  if finishegghouse and finishmushroom and finishstone and finishstump:
    endbg = pygame.image.load('endbg.png').convert_alpha()
    endbg = pygame.transform.rotozoom(endbg, 1, 1)
    endbg_rect = endbg.get_rect(topleft = (0,0))
    screen.blit(endbg, endbg_rect)
    screen.blit(endplayer, endplayer_rect)
    text_font = pygame.font.Font(None, 70) 
    text_welcome = text_font.render('Congratulations!', True, 'White')
    text_welcome_rect = text_welcome.get_rect(midbottom = (300, 200))
    screen.blit(text_welcome, text_welcome_rect)
    text_font = pygame.font.Font(None, 40) 

    screen.blit(endplayer, endplayer_rect)

  pygame.display.update() 
  clock.tick(60) 