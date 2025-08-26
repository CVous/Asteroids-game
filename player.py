import pygame
from circleshape import CircleShape
from constants import *

class player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        path = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x + path.x * self.radius, self.position.y + path.y * self.radius, SHOT_RADIUS)
        shot.velocity = path * PLAYER_SHOOT_SPEED

    
        
        

    def update(self, dt):
        
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)



        if keys[pygame.K_SPACE]:
            self.shoot()


    
class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius= SHOT_RADIUS)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)