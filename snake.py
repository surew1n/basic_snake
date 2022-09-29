import pygame, random
 
pygame.init()

pygame.display.set_caption('Snake')
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 
width = 420
height = 420
screen = pygame.display.set_mode((width, height))
 
game_over = False
berry_spawned = False
berry_ate = False
moved = False

points = 0

block_size = 20

head_x = 200
head_y = 200

body_list = [pygame.Rect(head_x, head_y, block_size, block_size)]

vel = 20

clock = pygame.time.Clock()
 
while not game_over:
  for x in range(1, len(body_list)):
    if (body_list[0].left == body_list[x].left) and (body_list[0].top == body_list[x].top):
      game_over = True

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          if dir != "right" and moved == False:
            dir = "left"
            moved = True
        elif event.key == pygame.K_RIGHT:
          if dir != "left" and moved == False:
            dir = "right"
            moved = True
        elif event.key == pygame.K_UP:
          if dir != "down" and moved == False:
            dir = "up"
            moved = True            
        elif event.key == pygame.K_DOWN:
          if dir != "up" and moved == False:
            dir = "down"
            moved = True

  berry_ate = False

  if body_list[0].left > 400:
    body_list[0].left = 0
  elif body_list[0].left < 0:
    body_list[0].left = 400
  elif body_list[0].top < 0:
    body_list[0].top = 400  
  elif body_list[0].top > 400:
    body_list[0].top = 0

  screen.fill(black)

  if berry_spawned == False:
    berry_x = random.randint(0, 20) * block_size
    berry_y = random.randint(0, 20) * block_size
    while True:
      if berry_x == body_list[0].left and berry_y == body_list[0].top:
        berry_x = random.randint(0, 20) * block_size
        berry_y = random.randint(0, 20) * block_size
      else:
        berry_spawned = True
        break

  if body_list[0].left == berry_x and body_list[0].top == berry_y:
    berry_spawned = False
    berry_ate = True
    points += 1
    print(points)

  def snake_move():
    if dir == "up":
      body_list.insert(0, pygame.Rect(body_list[0].left, body_list[0].top - 20, block_size, block_size))
      if berry_ate == False:
        body_list.pop()
    elif dir == "down":
      body_list.insert(0, pygame.Rect(body_list[0].left, body_list[0].top + 20, block_size, block_size))
      if berry_ate == False:
        body_list.pop()
    if dir == "left":
      body_list.insert(0, pygame.Rect(body_list[0].left - 20, body_list[0].top, block_size, block_size))
      if berry_ate == False:
        body_list.pop()
    if dir == "right":
      body_list.insert(0, pygame.Rect(body_list[0].left + 20, body_list[0].top, block_size, block_size))
      if berry_ate == False:
        body_list.pop()

  for x in range(0, width, block_size):
    for y in range(0, height, block_size):
      grid_rect = pygame.Rect(x, y, block_size, block_size)
      pygame.draw.rect(screen, white, grid_rect, 1) 

  pygame.draw.rect(screen, blue, [berry_x, berry_y, block_size, block_size])
  pygame.draw.rect(screen, white, [berry_x,  berry_y, block_size, block_size], 1)

  for x in body_list:
    pygame.draw.rect(screen, red, x)
    pygame.draw.rect(screen, white, x, 1)

  snake_move()
  pygame.display.update()

  clock.tick(15)
  moved = False
 
pygame.quit()