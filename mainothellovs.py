import pygame
from button import Button


pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arial black", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load('C:/Users/Sherlin/Downloads/resumebutton(othello).png').convert_alpha()
options_img = pygame.image.load('C:/Users/Sherlin/Downloads/optionsbutton(othello).png').convert_alpha()
quit_img = pygame.image.load('C:/Users/Sherlin/Downloads/quitbutton(othello).png').convert_alpha
audio_img = pygame.image.load('C:/Users/Sherlin/Downloads/audiobutton(othello).png').convert_alpha()
help_img = pygame.image.load('C:/Users/Sherlin/Downloads/helpbutton(othello).png').convert_alpha()
back_img = pygame.image.load('C:/Users/Sherlin/Downloads/backbutton(othello).png').convert_alpha()

#create button instances

resume_button = Button(304, 125, resume_img, 1)
options_button = Button(297, 250, options_img, 1)
quit_button = Button(336, 375, quit_img, 1)
audio_button = Button(225, 200, audio_img, 1)
help_button = Button(246, 325, help_img, 1)
back_button = Button(332, 450, back_img, 1)
def draw_text(font, text, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.fill((52, 78, 91))

  if game_paused == True:
    #check menu state
    if menu_state == "main":
      #draw pause screen buttons
      if resume_button.draw(screen):
        game_paused = False
      if options_button.draw(screen):
        menu_state = "options"
      if quit_button.draw(screen):
        run = False
    #check if the options menu is open
    if menu_state == "options":
      #draw the different options buttons
      if audio_button.draw(screen):
        print("Audio Settings")
      if help_button.draw(screen):
        print("Change Key Bindings")
      if back_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()