import pygame
import button
import othello

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('C:/Users/Sherlin/Downloads/startbutton(othello).png').convert_alpha()
exit_img = pygame.image.load('C:/Users/Sherlin/Downloads/exitbutton(othello).png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
exit_button = button.Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

    run = True
    while run:


        screen.fill((202, 228, 241))

        if start_button.draw(screen):
            def main():
                game = othello.Othello()
                game.draw_board()
                game.initialize_board()

                game.run()


            main()
        if exit_button.draw(screen):
            print('EXIT')

    #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

pygame.quit()