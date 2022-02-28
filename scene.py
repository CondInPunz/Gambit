class Scene:
    def __init__(self, screen):
        self.screen = screen

    def set_background(self, image):
        self.screen.blit(image, (0, 0))
