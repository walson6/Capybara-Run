#TODO
#-randomize enemy spawns and speed BUT ALSO BALANCE IT!
import pygame
import random
pygame.init()

###Score (ms since pygame.init())
def display_score():
  current_time = int(pygame.time.get_ticks() / 1000) - start_time
  score_surf = font.render(f'Score: {current_time}', False, 'Black')
  score_rect = score_surf.get_rect(center = (500, 83))
  screen.blit(score_surf, score_rect)

###Game set up
screen = pygame.display.set_mode((1000, 542))
clock = pygame.time.Clock()
font = pygame.font.Font('Minecraft.ttf', 30)
lostFont = pygame.font.Font('Minecraft.ttf', 50)
game_active = True
start_time = 0
instructions_surf = font.render("Avoid the capybaras and oranges!", False, 'Black')
instructions_rect = instructions_surf.get_rect(center=(500, 40))

###Background model and position
background_surf = pygame.image.load('background1.png').convert_alpha()
background_surf = pygame.transform.rotozoom(background_surf,0, 0.5)

background_surf_rect1 = background_surf.get_rect(midbottom = (384,766))
background_surf_rect2 = background_surf.get_rect(midbottom = (1152,766))
background_surf_rect3 = background_surf.get_rect(midbottom = (1920,766))
background_surf_rect4 = background_surf.get_rect(midbottom = (2688,766))

###Ground model and position
#450 is width of floors
ground_surface = pygame.image.load('floor2.png').convert_alpha()
ground_surface = pygame.transform.rotozoom(ground_surface,0, 0.1)

ground_surface_rect1 = ground_surface.get_rect(midbottom = (0, 542))
ground_surface_rect2 = ground_surface.get_rect(midbottom = (400, 542))
ground_surface_rect3 = ground_surface.get_rect(midbottom = (800, 542))
ground_surface_rect4 = ground_surface.get_rect(midbottom = (1200, 542))

###Jump sound effect
jump_noise = pygame.mixer.Sound('JumpEffect.wav')
music = pygame.mixer.Sound('CuteCircus.wav')
music.set_volume(0.1)
music.play()

###Enemey model and position
enemy = pygame.image.load('capyhole.png').convert_alpha()
enemy = pygame.transform.rotozoom(enemy,0, 0.035)
enemy_rect = enemy.get_rect(bottomleft = (1200, 403))

oranges = ["orange1.png","orange2.png","orange3.png"]
enemy1 = pygame.image.load(random.choice(oranges)).convert_alpha()
enemy1 = pygame.transform.rotozoom(enemy1,0, 0.065)
enemy_rect1 = enemy1.get_rect(bottomleft = (1100, 200))

###Player model and position
player = pygame.image.load('capybara1.png').convert_alpha()
player = pygame.transform.rotozoom(player,0, 0.1)
player_rect = player.get_rect(midbottom = (85,385))
player1 = pygame.image.load('capybara2.png').convert_alpha()
player1 = pygame.transform.rotozoom(player1,0, 0.1)
player_rect1 = player1.get_rect(midbottom = (85,385))

player_gravity = 0
randomSpeed = random.randint(13,17)

###Game loop
while True:
  ###Update screen to remove "echos"
  screen.fill((	135, 206, 235))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    ###Press space to jump (player jump action and height)
    if game_active == True:
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE and player_rect.bottom >= 385:
            player_gravity = -17 #increase for jump height
            jump_noise.play()
    ###Press space to restart
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_active = True
        enemy_rect.left = 1000
        enemy_rect1.left = 1000
        start_time = int(pygame.time.get_ticks() / 1000)

  ###Active game
  if game_active:
    background_surf_rect1.x -= 9
    if background_surf_rect1.right <= 0:
      background_surf_rect1.left = 1000
    screen.blit(background_surf, background_surf_rect1)
    background_surf_rect2.x -= 9
    if background_surf_rect2.right <= 0:
      background_surf_rect2.left = 1000
    screen.blit(background_surf, background_surf_rect2)
    background_surf_rect3.x -= 9
    if background_surf_rect3.right <= 0:
      background_surf_rect3.left = 1000
    screen.blit(background_surf, background_surf_rect3)
    background_surf_rect4.x -= 9
    if background_surf_rect4.right <= 0:
      background_surf_rect4.left = 1000
    screen.blit(background_surf, background_surf_rect4)

    ground_surface_rect1.x -= 9
    if ground_surface_rect1.right <= 0:
      ground_surface_rect1.left = 1000
    screen.blit(ground_surface, ground_surface_rect1)
    ground_surface_rect2.x -= 9
    if ground_surface_rect2.right <= 0:
      ground_surface_rect2.left = 1000
    screen.blit(ground_surface, ground_surface_rect2)
    ground_surface_rect3.x -= 9
    if ground_surface_rect3.right <= 0:
      ground_surface_rect3.left = 1000
    screen.blit(ground_surface, ground_surface_rect3)
    ground_surface_rect4.x -= 9
    if ground_surface_rect4.right <= 0:
      ground_surface_rect4.left = 1000
    screen.blit(ground_surface, ground_surface_rect4)

    ###Enemy movement and display
    enemy_rect.x -= 9
    if enemy_rect.right <= 0:
      enemy_rect.left = 1700
    screen.blit(enemy, enemy_rect)

    enemy_rect1.x -= randomSpeed
    if enemy_rect1.right <= -100:
      enemy1 = pygame.image.load(random.choice(oranges)).convert_alpha()
      enemy1 = pygame.transform.rotozoom(enemy1, 0, 0.065)
      enemy_rect1.left = 1300
      randomSpeed = random.randint(13, 17)
    screen.blit(enemy1, enemy_rect1)

    ###Player movement, display, and gravity
    player_gravity += 0.7 #increase for more gravity
    player_rect.y += player_gravity
    if player_rect.bottom >= 385:
      player_rect.bottom = 385

    player_rect1.y += player_gravity
    if player_rect1.bottom >= 385:
      player_rect1.bottom = 385
    screen.blit(player1, player_rect1)

    ###Player animation
    if ((pygame.time.get_ticks() - start_time)) % 2 == 1 and player_rect1.bottom >= 385:
      screen.blit(player, player_rect)
    elif ((pygame.time.get_ticks() - start_time)) % 2 == 2:
      screen.blit(player1, player_rect1)

    ###Collision
    if enemy_rect.colliderect(player_rect) or enemy_rect.colliderect(player_rect1) or enemy_rect1.colliderect(player_rect) or enemy_rect1.colliderect(player_rect1):
      game_active = False
    if enemy_rect1.colliderect(player_rect) or enemy_rect1.colliderect(player_rect1):
      game_active = False

    screen.blit(instructions_surf, instructions_rect)
    display_score()
    pygame.display.update()
    lastScore = int(pygame.time.get_ticks() / 1000) - start_time

  ###Lost screen
  else:
    screen.fill((135, 206, 235))
    screen.blit(background_surf, background_surf_rect1)
    screen.blit(background_surf, background_surf_rect2)
    screen.blit(background_surf, background_surf_rect3)
    screen.blit(background_surf, background_surf_rect4)
    screen.blit(ground_surface, ground_surface_rect1)
    screen.blit(ground_surface, ground_surface_rect2)
    screen.blit(ground_surface, ground_surface_rect3)
    screen.blit(ground_surface, ground_surface_rect4)

    endMessage_surf = lostFont.render("You lost!", False, 'Black')
    endMessage_rect = endMessage_surf.get_rect(center=(500, 170))
    endMessage_surf1 = lostFont.render("Press space to try again", False, 'Black')
    endMessage_rect1 = endMessage_surf1.get_rect(center=(500, 230))
    scoreMessage_surf = lostFont.render(f"Your score: {lastScore}", False, 'Black')
    scoreMessage_rect = scoreMessage_surf.get_rect(center=(500, 295))

    screen.blit(enemy, enemy_rect)
    screen.blit(enemy1, enemy_rect1)
    screen.blit(player, player_rect)
    screen.blit(endMessage_surf, endMessage_rect)
    screen.blit(endMessage_surf1, endMessage_rect1)
    screen.blit(scoreMessage_surf, scoreMessage_rect)
    pygame.display.update()

  clock.tick(60)