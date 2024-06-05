import pygame

WIDTH, HEIGHT = 800, 700
FPS = 30


def main():
	pygame.init()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Simple Game with Enemies!")
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == "__main__":
	main()
