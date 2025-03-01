import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("назва_гри")

player = pygame.Rect(400, 300, 50, 50)
walls = [
    pygame.Rect(200, 530, 100, 100),  
    pygame.Rect(500, 530, 100, 150)   
]

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    move_x, move_y = 0, 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_x = -5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_x = 5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        move_y = -5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        move_y = 5
    
    # перевірка колізії по X
    player.x += move_x
    for wall in walls:
        if player.colliderect(wall):
            if move_x > 0: 
                player.right = wall.left
            if move_x < 0:  
                player.left = wall.right
    
    # перевірка колізії по Y
    player.y += move_y
    for wall in walls:
        if player.colliderect(wall):
            if move_y > 0:  
                player.bottom = wall.top
            if move_y < 0:  
                player.top = wall.bottom
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)
    
    clock.tick(60)
    pygame.display.update()
