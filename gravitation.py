import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("назва_гри")

player = pygame.Rect(400, 300, 50, 50)

gravity = 0.5
velocity_y = 0
jump_strength = -10
grounded = False
wall_jump = False

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
    move_x = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move_x = -5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move_x = 5
    
    # переміщення по горизонталі з перевіркою колізій
    player.x += move_x
    for wall in walls:
        if player.colliderect(wall):
            if move_x > 0:  # рух вправо
                player.right = wall.left
            elif move_x < 0:  # рух вліво
                player.left = wall.right
    
    # гравітація
    velocity_y += gravity
    player.y += velocity_y
    grounded = False
    
    # перевірка зіткнення із землею
    if player.y + player.height >= 600:
        player.y = 600 - player.height
        velocity_y = 0
        grounded = True
    
    # перевірка колізій з стінами при русі вниз
    for wall in walls:
        if player.colliderect(wall):
            if velocity_y > 0:
                player.bottom = wall.top
                velocity_y = 0
                grounded = True
            elif velocity_y < 0:
                player.top = wall.bottom
                velocity_y = 0
    

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and (grounded or wall_jump):
        velocity_y = jump_strength
        wall_jump = False
    
    for wall in walls:
        if player.colliderect(wall):
            wall_jump = True
    
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)
    
    clock.tick(60)
    pygame.display.update()
