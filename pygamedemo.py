import pygame
from random import randint

pygame.init()	#khởi tạo pygame
screen = pygame.display.set_mode((400, 600))	#1 cái màn hình với chiều ngang và dọc
pygame.display.set_caption('Flappy Bird')	#tên của chương trình
running = True	#vòng lặp game
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BlUE = (0, 0, 255)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()	#chạy 60 lần trong 1 giây

font = pygame.font.SysFont('sans', 30)
text = font.render("random", True, BLACK)	#chữ
text_box = text.get_rect()

random_pos = (50,50)
circle_color = RED

while running:
	clock.tick(60)
	screen.fill(WHITE)	#màu nền

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))	#tạo 1 hình chữ nhật bao quanh chữ 
	screen.blit(text, random_pos)

	pygame.draw.circle(screen, circle_color, (200,300), 50)	#vẽ hình tròn
#check hover vào chữ thì nó đổi màu
	if ((mouse_x > random_pos[0]) and (mouse_x < random_pos[0] + text_box[2]) and (mouse_y > random_pos[1]) and (mouse_y < random_pos[1] + text_box[3])):
		text = font.render("random", True, BlUE)
		pygame.draw.line(screen, BlUE, (random_pos[0],random_pos[1] + text_box[3]), (random_pos[0] + text_box[2], random_pos[1] + text_box[3]))	#vẽ một đường gạch chân dưới phần chữ	
	else:
		text = font.render("random", True, BLACK)

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (mouse_x > 50) and ( mouse_x < 200) and (mouse_y > 50) and (mouse_y < 100):	#check con chuột có nằm trong hình chữ nhật hay không
					circle_color = (randint(0,255), randint(0,255), randint(0,255))
					print("Right click on red rectangle")

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()	#để khi refresh lại thì mọi thữ đã vẽ sẽ được thay đổi

pygame.quit()	#tắt