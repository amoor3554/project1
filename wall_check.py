import pygame

# تهيئة pygame
pygame.init()

# إعداد الشاشة
screen = pygame.display.set_mode((800, 600))

# إعداد اللاعب
player = pygame.Rect(50, 50, 50, 50)
player_speed = 1

# إعداد الجدار
wall = pygame.Rect(300, 300, 100, 100)

# الحلقة الرئيسية للعبة
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # التحكم في حركة اللاعب
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # التحقق من التصادم
    if player.colliderect(wall):
        # إذا حدث تصادم، أعد اللاعب إلى موضعه السابق
        if keys[pygame.K_LEFT]:
            player.x += player_speed
        if keys[pygame.K_RIGHT]:
            player.x -= player_speed
        if keys[pygame.K_UP]:
            player.y += player_speed
        if keys[pygame.K_DOWN]:
            player.y -= player_speed

    # رسم الكائنات
    screen.fill((0, 0, 0))  # خلفية سوداء
    pygame.draw.rect(screen, (255, 0, 0), player)  # اللاعب باللون الأحمر
    pygame.draw.rect(screen, (0, 255, 0), wall)    # الجدار باللون الأخضر

    # تحديث الشاشة
    pygame.display.flip()

pygame.quit()
