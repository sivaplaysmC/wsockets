import pygame

win = pygame.display.set_mode((800,800))

run = True

## game_states :
## menu 
## pause screen 
## command_console
## game

def main(win) :
    while True :
        win.fill("blue")
        pygame.display.flip()
        for event in pygame.event.get() :
            if event.type == pygame.KEYDOWN :
                return


main(win)

gamestate = "main_menu"
gamestate_stack = list()
gamestate_stack.append(gamestate)

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            quit()
    win.fill('white')
    pygame.display.flip()

