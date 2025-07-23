import pygame
import random
import sys

# เริ่มต้น pygame
pygame.init()

# ขนาดหน้าจอ
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# สี
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 150, 255)
BLACK = (0, 0, 0)

# ผู้เล่น
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 20
player_vel = 7

# บล็อกตก
block_size = 50
block_vel = 5
blocks = []

# เวลา
clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont("Arial", 36)

def draw_window(player_rect, blocks, score):
    win.fill(WHITE)
    pygame.draw.rect(win, BLUE, player_rect)
    for block in blocks:
        pygame.draw.rect(win, RED, block)
    score_text = font.render(f"Score: {score}", True, BLACK)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def main():
    global block_vel
    run = True
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    score = 0
    spawn_timer = 0

    while run:
        clock.tick(FPS)
        spawn_timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        # ควบคุม
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_vel
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_vel

        # สร้างบล็อก
        if spawn_timer > 30:
            block_x = random.randint(0, WIDTH - block_size)
            blocks.append(pygame.Rect(block_x, 0, block_size, block_size))
            spawn_timer = 0
            score += 1
            if score % 10 == 0:
                block_vel += 1  # เพิ่มความเร็วเมื่อคะแนนเพิ่ม

        # เคลื่อนบล็อก
        for block in blocks:
            block.y += block_vel
            if block.colliderect(player_rect):
                print(f"Game Over! Your Score: {score}")
                run = False
            if block.y > HEIGHT:
                blocks.remove(block)

        draw_window(player_rect, blocks, score)

    pygame.quit()

if __name__ == "__main__":
    main()