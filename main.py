import pygame
import sys


def move_paddle(y_paddle, paddle_height, move, height):
    if move < 0:
        if y_paddle + move < 0:
            return 0
        else:
            return y_paddle + move
    elif move > 0:
        if y_paddle + paddle_height + move > height:
            return height - paddle_height
        else:
            return y_paddle + move
    else:
        return y_paddle


def main():
    pygame.init()

    width = 800
    height = 600

    white = (255, 255, 255)
    black = (0, 0, 0)

    paddle_width = 20
    paddle_height = 90

    ball_side = 20

    x_player = 0
    y_player = height // 2 - 50

    x_pc = width - 20
    y_pc = height // 2 - 50

    x_ball = width // 2 - ball_side
    y_ball = height // 2 - ball_side

    distance = 30

    move_player = 0
    move_pc = 0

    move_ball_x = -distance
    move_ball_y = 0

    collide_player = True
    collide_pc = False

    screen = pygame.display.set_mode((width, height))
    frames = pygame.time.Clock()
    pygame.display.set_caption('Pong 2D')

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_player = -distance
                elif event.key == pygame.K_s:
                    move_player = distance

                if event.key == pygame.K_UP:
                    move_pc = -distance
                elif event.key == pygame.K_DOWN:
                    move_pc = distance

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    move_player = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    move_pc = 0

        y_player = move_paddle(y_player, paddle_height, move_player, height)
        y_pc = move_paddle(y_pc, paddle_height, move_pc, height)

        screen.fill(black)

        pygame.draw.rect(screen, white, (x_player, y_player, paddle_width, paddle_height))
        pygame.draw.rect(screen, white, (x_pc, y_pc, paddle_width, paddle_height))
        pygame.draw.rect(screen, white, (x_ball, y_ball, ball_side, ball_side))

        if collide_player and x_player <= x_ball + ball_side <= x_player + paddle_width and y_player <= y_ball + ball_side <= y_player + paddle_height:
            move_ball_x = distance

            if y_player + 0 <= y_ball < y_player + paddle_height // 3:
                move_ball_y = -(y_player + paddle_height // 3 - y_ball)
            elif y_player + paddle_height // 3 <= y_ball < y_player + 2 * paddle_height // 3:
                move_ball_y = 0
            else:
                move_ball_y = (y_player + paddle_height - y_ball)

            collide_player = False
            collide_pc = True

        if collide_pc and x_pc <= x_ball + ball_side <= x_pc + paddle_width and y_pc <= y_ball + ball_side <= y_pc + paddle_height:
            move_ball_x = -distance

            if y_pc + 0 <= y_ball < y_pc + paddle_height // 3:
                move_ball_y = -(y_pc + paddle_height // 3 - y_ball)
            elif y_pc + paddle_height // 3 <= y_ball < y_pc + 2 * paddle_height // 3:
                move_ball_y = 0
            else:
                move_ball_y = (y_pc + paddle_height - y_ball)

            collide_player = True
            collide_pc = False

        if y_ball < 0 or y_ball > height:
            move_ball_y *= -1

        # if x_ball < 0 or x_ball > width:
        #    x_ball = width // 2 - ball_side
        #    y_ball = height // 2 - ball_side
        #    move_ball_x = -distance
        #    move_ball_y = 0

        x_ball += move_ball_x
        y_ball += move_ball_y

        pygame.display.update()
        frames.tick(20)


if __name__ == '__main__':
    main()
