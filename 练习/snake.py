# 设计贪吃蛇小游戏

# 导入库
import pygame
import time
import random

snake_speed = 15

# 窗口大小
window_x = 720
window_y = 480

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# 初始化pygame
pygame.init()

# 初始化游戏窗口
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS（每秒帧数）控制器
fps = pygame.time.Clock()

# 定义蛇默认位置
snake_position = [100, 50]

# 定义蛇体的前 4 个块
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# 水果位置
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# 设置默认的蛇方向向右
direction = 'RIGHT'
change_to = direction

# 初始分数
score = 0


# 显示评分功能
def show_score(choice, color, font, size):

    # 创建字体对象 score_font
    score_font = pygame.font.SysFont(font, size)

    # 创建显示表面对象 core_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # 为文本表面对象创建一个矩形对象
    score_rect = score_surface.get_rect()

    # 显示文字
    game_window.blit(score_surface, score_rect)


# 游戏结束功能
def game_over():
    # 创建字体对象 my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # 创建将在其上绘制文本的文本表面
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)

    # 为文本表面对象创建一个矩形对象
    game_over_rect = game_over_surface.get_rect()

    # 设置文本位置
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit 将在屏幕上绘制文本
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # 2 秒后我们将退出程序
    time.sleep(2)

    # 停用 pygame 库
    pygame.quit()

    # 退出程序
    quit()


# Main Function
while True:

    # 处理关键事件
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # 如果同时按下两个键
    # 我们不想让蛇同时向两个方向移动
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # 移动蛇
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # 蛇体生长机制
    # 如果水果和蛇发生碰撞，那么分数将增加 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # 游戏结束条件
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # 触碰蛇身
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # 连续显示分数
    show_score(1, white, 'times new roman', 20)

    # 刷新游戏画面
    pygame.display.update()

    # 每秒帧数/刷新率
    fps.tick(snake_speed)


