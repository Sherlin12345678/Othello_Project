import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption("Othello")
icon = pygame.image.load('C:/Users/vasus/Downloads/logo1.png')
pygame.display.set_icon(icon)
textfont = pygame.font.SysFont("Ariel", 50)

width, height = 800, 600
window = pygame.display.set_mode((width, height))
bg_img = pygame.image.load('C:/Users/vasus/Downloads/logo12.png')
bg_img = pygame.transform.scale(bg_img, (125, 125))

runing = True
while runing:
    window.fill((255, 255, 255))
    textTBD = textfont.render("OTHELLO...", 15, (0, 0, 0))
    window.blit(bg_img, (340, 200))
    window.blit(textTBD, (320, 350))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    pygame.display.update()

pygame.quit()