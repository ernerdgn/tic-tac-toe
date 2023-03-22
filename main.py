import pygame
import sys
import game

FPS = 60  #SET FPS VARIABLE

WIN = pygame.display.set_mode((game.WIDTH, game.HEIGHT))  # GET WINDOW
pygame.display.set_caption("Tic-Tac-Toe")
WIN.fill(game.BLACK)

#DRAWING BORDERS
pygame.draw.line(WIN, game.WHITE, (0,200), (600,200), 4)
pygame.draw.line(WIN, game.WHITE, (0,400), (600,400), 4)
pygame.draw.line(WIN, game.WHITE, (200,0), (200,600), 4)
pygame.draw.line(WIN, game.WHITE, (400,0), (400,600), 4)


def main():
    run = True
    clock = pygame.time.Clock()  # LOCK FPS

    while run:
        clock.tick(FPS)
        pygame.display.update()  # UPDATE WINDOW
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse click")
                mouse_position = pygame.mouse.get_pos()  # TUPLE DATA (column, row)
                
                if 0 < mouse_position[0] <= 200 and 0 < mouse_position[1] <= 200:  # [0,0]
                    print("0,0")
                    if game.is_empty(0,0):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (15,15), (185, 185))
                            game.x_to_move = False
                            game.MAP[0][0] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (100,100), 85)
                            game.x_to_move = True
                            game.MAP[0][0] = "o"

                elif 201 < mouse_position[0] <= 400 and 0 < mouse_position[1] <= 200:  # [0,1]
                    print("0,1")
                    if game.is_empty(0,1):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (215,15), (385, 185))
                            game.x_to_move = False
                            game.MAP[0][1] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (300,100), 85)
                            game.x_to_move = True
                            game.MAP[0][1] = "o"

                elif 401 < mouse_position[0] <= 600 and 0 < mouse_position[1] <= 200:  # [0,2]
                    print("0,2")
                    if game.is_empty(0,2):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (415,15), (585, 185))
                            game.x_to_move = False
                            game.MAP[0][2] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (500,100), 85)
                            game.x_to_move = True
                            game.MAP[0][2] = "o"

                elif 0 < mouse_position[0] <= 200 and 201 < mouse_position[1] <= 400:  # [1,0]
                    print("1,0")
                    if game.is_empty(1,0):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (15,215), (185, 385))
                            game.x_to_move = False
                            game.MAP[1][0] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (100,300), 85)
                            game.x_to_move = True
                            game.MAP[1][0] = "o"

                elif 201 < mouse_position[0] <= 400 and 201 < mouse_position[1] <= 400:  # [1,1]
                    print("1,1")
                    if game.is_empty(1,1):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (215,215), (385, 385))
                            game.x_to_move = False
                            game.MAP[1][1] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (300,300), 85)
                            game.x_to_move = True
                            game.MAP[1][1] = "o"

                elif 401 < mouse_position[0] <= 600 and 201 < mouse_position[1] <= 400:  # [1,2]
                    print("1,2")
                    if game.is_empty(1,2):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (415,215), (585, 385))
                            game.x_to_move = False
                            game.MAP[1][2] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (500,300), 85)
                            game.x_to_move = True
                            game.MAP[1][2] = "o"

                elif 0 < mouse_position[0] <= 200 and 401 < mouse_position[1] <= 600:  # [2,0]
                    print("2,0")
                    if game.is_empty(2,0):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (15,415), (185, 585))
                            game.x_to_move = False
                            game.MAP[2][0] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (100,500), 85)
                            game.x_to_move = True
                            game.MAP[2][0] = "o"

                elif 201 < mouse_position[0] <= 400 and 401 < mouse_position[1] <= 600:  # [2,1]
                    print("2,1")
                    if game.is_empty(2,1):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (215,415), (385, 585))
                            game.x_to_move = False
                            game.MAP[2][1] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (300,500), 85)
                            game.x_to_move = True
                            game.MAP[2][1] = "o"

                elif 401 < mouse_position[0] <= 600 and 401 < mouse_position[1] <= 600:  # [2,2]
                    print("2,2")
                    if game.is_empty(2,2):
                        if game.x_to_move:
                            game.draw_x(WIN, game.COLOR_X, (415,415), (585, 585))
                            game.x_to_move = False
                            game.MAP[2][2] = "x"
                        else:
                            game.draw_o(WIN, game.COLOR_O, (500,500), 85)
                            game.x_to_move = True
                            game.MAP[2][2] = "o"
                if not game.check_for_winner(game.MAP):
                    print("GAME FINISHED")
                    run = False
                if game.check_draw(game.MAP):
                    print("GAME DRAW!")
                    run = False

    if not run:
        print("game shutting down")
        pygame.quit
        sys.exit(0)

main()
            