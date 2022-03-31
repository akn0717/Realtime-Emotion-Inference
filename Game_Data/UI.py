import os
import pygame
import numpy as np

class Game_Object:
    def __init__(self, x, y, opacity = 100):
        self.x = x
        self.y = y
        self.opacity = opacity
    
    def update(self):
        pass

class Bubble_Object(Game_Object):
    def __init__(self, img_path, x, y, size, opacity=1):
        super().__init__(x, y, opacity)
        self.ico = pygame.image.load(img_path)
        self.size = (size,size)
        self.velocity = np.array((0,-1))
        self.time = 0
        self.on_screen = True

    def reset(self, img_path, x, y):
        self.ico = self.ico = pygame.image.load(img_path)
        self.x, self.y = x, y
        self.on_screen = True
        
        return
    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if (self.y<-10):
            self.on_screen = False

    def draw(self, screen):
        screen.blit(self.ico, (self.x, self.y))


class Text_Object(Game_Object):
    def __init__(self, x, y, text, size = 56, opacity = 100, font = 'Default'):
        super().__init__(x, y, opacity)
        self.font = font
        self.font = pygame.font.Font(font, size)
        self.color = (0,0,0)
        self.text = text
        self.rendered = pygame.font.Font.render(self.font, self.text, True, self.color)
        self.height = self.rendered.get_height()
        self.width = self.rendered.get_width()
        self.size = size
    def update(self):
        self.rendered = pygame.font.Font.render(self.font, self.text, True, self.color)
        return

    def draw(self, screen):
        screen.blit(self.rendered, (self.x - (self.width/2), self.y- (self.height/2)))

class Button(Game_Object):
    def __init__(self, x, y, height, width, title = None, opacity = 1.0, state = 0):
        super().__init__(x, y, opacity)
        self.height = height
        self.width = width
        self.x -= self.width/2
        self.y -= self.height/2
        self.color = (255,255,255)
        self.text = Text_Object(self.x + width/2, self.y + height/2, text = title, font = 'freesansbold.ttf')
        self.state = state
        self.icons = []
        self.sounds = []
        return

    def mouse_normal(self):
        self.text.color = (0,0,0)
        self.color = (255,255,255)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return

    def mouse_hover(self):
        self.text.color = (255,255,255)
        self.color = (0,0,0)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        return

    def on_hover(self):
        return self.state==1

    def update(self):
        mouse_posx, mouse_posy = pygame.mouse.get_pos()
        last_state = self.state
        if (self.x <= mouse_posx and mouse_posx <= self.x + self.width and self.y <= mouse_posy and mouse_posy <= self.y + self.height):
            self.state = 1
        else:
            self.state = 0

        if self.state != last_state:
            if (self.state == 1):
                self.mouse_hover()
            elif self.state == 0:
                self.mouse_normal()
        self.text.update()
        return
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height))
        self.text.draw(screen)
        return

class Camera():
    def __init__(self, pygame_camera, flip_x, flip_y, rotating_state):
        self.camera = pygame_camera
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.rotating_state = rotating_state

    def rotate(self):
        self.rotating_state = (self.rotating_state + 1) % 4
        return

    def flip_on_x(self):
        self.flip_x = not self.flip_x
        return
    
    def flip_on_y(self):
        self.flip_y = not self.flip_y
        return

    def get_output_transform(self):
        cam_image = pygame.transform.rotate(self.camera.get_image(), angle = (self.rotating_state)*90)
        cam_image = pygame.transform.flip(cam_image, flip_x = self.flip_x, flip_y = self.flip_y)
        (cam_width, cam_height) = cam_image.get_rect()[2], cam_image.get_rect()[3]
        first_cam = pygame.transform.chop(cam_image, (cam_width/2, 0, cam_width/2,0))
        second_cam = pygame.transform.chop(cam_image, (0, 0, cam_width/2,0))
        return first_cam, second_cam

    def draw(self, screen):
        first_cam, second_cam = self.get_output_transform()
        cropped_cam_size = (first_cam.get_width(), first_cam.get_height())
        screen_center = (screen.get_rect()[2]/2,screen.get_rect()[3]/2)
        screen.blit(first_cam, ((screen_center[0]/2) - cropped_cam_size[0]/2,screen_center[1] - cropped_cam_size[1]/2))
        screen.blit(second_cam, ((screen_center[0] + screen_center[0]/2) - cropped_cam_size[0]/2,screen_center[1] - cropped_cam_size[1]/2))

class Animated_Background(Game_Object):
    def __init__(self, screen):
        self.screen = screen
        self.bubble_list = [] 
        self.emojis_files = [f for f in os.listdir("Game_Data/emojis") if os.path.isfile(os.path.join("Game_Data/emojis", f)) and (os.path.splitext(f)[1] == '.png')]
        for i in range(20):
            size = np.random.randint(5,20)
            img_path = os.path.join("Game_Data/emojis", np.random.choice(self.emojis_files))
            bubble = Bubble_Object(img_path, x = np.random.randint(0,self.screen.get_rect()[2]), y = np.random.randint(0,self.screen.get_rect()[3]), size = size)
            self.bubble_list.append(bubble)

    def draw(self):
        self.screen.fill((210,210,210))
        for bubble_idx in range(len(self.bubble_list)):
            if self.bubble_list[bubble_idx].on_screen == False:
                img_path = os.path.join("Game_Data/emojis", np.random.choice(self.emojis_files))
                self.bubble_list[bubble_idx].reset(img_path, x = np.random.randint(0,self.screen.get_rect()[2]), y = np.random.randint(self.screen.get_rect()[3],self.screen.get_rect()[3] + 100))
            self.bubble_list[bubble_idx].update()
            self.bubble_list[bubble_idx].draw(screen = self.screen)
        return

class Main_Menu():
    def __init__(self, screen):
        self.screen = screen
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2
        self.buttons = [Button(x = center_x, y = center_y + 100, height = 60, width = 120, title = "Play"),
                        Button(x = center_x, y = center_y + 200, height = 60, width = 120, title = "Camera Setting"),
                        Button(x = center_x, y = center_y + 300, height = 60, width = 120, title = "Exit")]
        self.bgms = []
        self.logo = pygame.image.load("Game_Data/image/The Expression-logo.png")
        self.logo = pygame.transform.scale(self.logo, (screen.get_rect()[2]/3.85,screen.get_rect()[3]/2.5))
        return
    
    def update(self):
        for button in self.buttons:
            button.update()
        return

    def draw(self, screen):
        self.screen.blit(self.logo, ((self.screen.get_rect()[2]/2)-(self.logo.get_rect()[2]/2),self.screen.get_rect()[3]/2.5 - (self.logo.get_rect()[3]/2)))
        for button in self.buttons:
            button.draw(screen)
        return


class Camera_Menu():
    def __init__(self, camera, screen):
        self.screen = screen
        self.camera = camera
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2
        self.buttons = [Button(x = center_x, y = center_y - 200, height = 60, width = 120, title = "Rotate"),
                        Button(x = center_x, y = center_y - 100, height = 60, width = 120, title = "Flip x axis"),
                        Button(x = center_x, y = center_y, height = 60, width = 120, title = "Flip y axis"),
                        Button(x = center_x, y = center_y + 200, height = 60, width = 120, title = "<< Back")]
        self.bgms = []
        return
    
    
    def update(self):
        for button in self.buttons:
            button.update()
        return

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

        self.camera.draw(screen)
        return

class Play_Menu():
    def __init__(self, camera, screen):
        self.screen = screen
        self.camera = camera
        
        center_x, center_y = screen.get_rect()[2]/2, screen.get_rect()[3]/2
        self.buttons = []
        
        self.bgms = []

    def update(self):
        return

    def draw(self, screen):

        self.camera.draw(screen)
        return