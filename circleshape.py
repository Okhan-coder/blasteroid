import pygame

class CircleShape(pygame.sprite.Sprite):
     def __init__(self,x,y,radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

     def draw(self,screen):
        #Draw on Screen
        pass
     def update(self,dt):
        #Update Screen
        pass
     def collide(self,circle):
         distance = self.position.distance_to(circle.position)
         r_distance = self.radius + circle.radius
         if distance > r_distance:
             return True
         return False
