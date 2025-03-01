import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("назва_гри")


player = pygame.Rect(400, 300, 50, 50)

running = True
while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)

    pygame.time.Clock().tick(60)
    pygame.display.update()
