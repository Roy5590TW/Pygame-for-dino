import pygame
import sys
import random

# 視窗大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# 地面高度
GROUND_HEIGHT = 350

# 跳躍相關參數
JUMP_HEIGHT = 140
JUMP_SPEED = 7
GRAVITY = 2.7

# 障礙物相關參數
OBSTACLE_WIDTH = 30
OBSTACLE_HEIGHTS = [50, 53, 55, 57, 60]
OBSTACLE_GAP = 200
OBSTACLE_SPEED = [5, 5.1, 5.2]

# 分數初始設定
score = 0

# 初始化Pygame
pygame.init()
pygame.mixer.init()

# 設定視窗大小
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('小恐龍遊戲')
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
score_sound = pygame.mixer.Sound('score.wav')
score_sound.set_volume(0.8)

# 加載小恐龍圖片並縮小
dinosaur_image = pygame.image.load('dinosaur.png')
dinosaur_image = pygame.transform.scale(
  dinosaur_image,
  (dinosaur_image.get_width() // 7, dinosaur_image.get_height() // 7))
dinosaur_rect = dinosaur_image.get_rect()
dinosaur_rect.bottom = GROUND_HEIGHT

# 障礙物列表
obstacles = []

# 設定地面和背景顏色
ground_color = (150, 150, 150)
background_color = (255, 255, 255)

# 設定小恐龍狀態
is_jumping = False
jump_count = 0

# 設定遊戲時鐘
clock = pygame.time.Clock()


# 生成障礙物
def generate_obstacle():
  obstacle_height = random.choice(OBSTACLE_HEIGHTS)
  obstacle_rect = pygame.Rect(WINDOW_WIDTH, GROUND_HEIGHT - obstacle_height,
                              OBSTACLE_WIDTH, obstacle_height)
  obstacles.append(obstacle_rect)


# 檢測碰撞
def check_collision():
  for obstacle in obstacles:
    if dinosaur_rect.colliderect(obstacle):
      return True
  return False


# 繪製分數
def draw_score():
  global score
  font = pygame.font.Font(None, 36)
  score_text = font.render("score: {}".format(score), True, (0, 0, 0))
  score_rect = score_text.get_rect(topright=(WINDOW_WIDTH - 10, 10))
  window_surface.blit(score_text, score_rect)


# 遊戲主迴圈
running = True
game_over = False
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and not is_jumping and not game_over:
        is_jumping = True
        jump_count = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
      mouse_pos = pygame.mouse.get_pos()
      if restart_rect.collidepoint(mouse_pos):
        # 重新開始遊戲
        obstacles.clear()
        dinosaur_rect.bottom = GROUND_HEIGHT
        is_jumping = False
        game_over = False
        # 重設分數
        score = 0
        pygame.mixer.music.play(-1)

  if not game_over:
    # 更新小恐龍位置
    if is_jumping:
      if jump_count < JUMP_HEIGHT:
        # 上升
        dinosaur_rect.y -= JUMP_SPEED
        jump_count += JUMP_SPEED
      else:
        # 下降
        dinosaur_rect.y += JUMP_SPEED
        jump_count += JUMP_SPEED
        if jump_count >= 2 * JUMP_HEIGHT:
          # 回到初始位置，結束跳躍
          dinosaur_rect.bottom = GROUND_HEIGHT
          is_jumping = False
          #+point
    # 更新障礙物位置
    for obstacle in obstacles:
      obstacle.x -= random.choice(OBSTACLE_SPEED)
      score += 100
      score_sound.play()


    # 移除離開螢幕的障礙物
    obstacles = [obstacle for obstacle in obstacles if obstacle.right > 0]

    # 生成新的障礙物
    if len(
        obstacles) == 0 or obstacles[-1].right < WINDOW_WIDTH - OBSTACLE_GAP:
      generate_obstacle()

    # 檢測碰撞
    if check_collision():
      game_over = True
      pygame.mixer.music.stop()

  # 繪製視窗背景
  window_surface.fill(background_color)
  pygame.draw.rect(
    window_surface, ground_color,
    pygame.Rect(0, GROUND_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - GROUND_HEIGHT))

  # 繪製障礙物
  for obstacle in obstacles:
    pygame.draw.rect(window_surface, (0, 0, 0), obstacle)

  # 繪製小恐龍
  window_surface.blit(dinosaur_image, dinosaur_rect)

  if game_over:
    # 顯示最終 Score 文字
    font = pygame.font.Font(None, 36)
    game_over_score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    game_over_score_rect = game_over_score_text.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
    window_surface.blit(game_over_score_text, game_over_score_rect)

    # 顯示 Game Over 文字
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(
        center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 90))
    window_surface.blit(game_over_text, game_over_rect)

    # 顯示重來圖片
    restart_image = pygame.image.load('retry.jpg')
    restart_image = pygame.transform.scale(restart_image, (100, 100))  # 自訂尺寸
    restart_rect = restart_image.get_rect(center=(WINDOW_WIDTH // 2,
                                                  WINDOW_HEIGHT // 2 + 50))
    window_surface.blit(restart_image, restart_rect)

  # 更新分數
  if not game_over:
    draw_score()

  # 更新視窗畫面
  pygame.display.flip()

  # 控製遊戲時鐘
  clock.tick(60)

# 關閉視窗
pygame.quit()
sys.exit()
