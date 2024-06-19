import requests
import pygame
import io
from direct_information_subsystem import *

pygame.init()

class weatherpygame:
    def __init__(self):
        self.inputcheck = ["Location", True]
    
    def textintoimage(text, fontsize, underline=False, light=False):
        if underline == True:
            font = pygame.font.SysFont("Segoe UI Variable", fontsize)
            pygame.font.Font.set_underline(font, 1)
        elif light:
            font = pygame.font.SysFont("segoeuisemilight", fontsize)
        else:
            font = pygame.font.SysFont("Segoe UI Variable", fontsize)
        image = font.render(str(text),1,"#000000")
        
        return image
    
    def button(screen, dimensions, distance, Height, text, colour=[222,222,222], fontsize=20, fontcolour="Black", colourighlight=20): #Buttons like hell man
        a,b = pygame.mouse.get_pos()
        buttonfont = pygame.font.SysFont('Segoe UI Variable',fontsize)
        Text = buttonfont.render(str(text), True, fontcolour)
        A = int(pygame.Surface.get_width(Text)) * 1.1
        button = pygame.Rect(dimensions[0] / 2 - A / 2 + distance, dimensions[1] / 2 - fontsize *1.1 + Height, A, pygame.Surface.get_height(Text) * 1.4)
        if button.x <= a <= button.x + A and button.y <= b <= button.y + fontsize * 1.1:  
            pygame.draw.rect(screen,(colour[0] + colourighlight,colour[1] + colourighlight, colour[2] + colourighlight), button, border_radius=4)
        else:
            pygame.draw.rect(screen,(colour), button, border_radius= 4)
        screen.blit(Text,(dimensions[0] / 2 - int(pygame.Surface.get_width(Text)) / 2 + distance, button.y + fontsize * 1.1 - fontsize))
        return button

    def textboxsetup(self, textboxsetup):
        self.inputcheck = [textboxsetup, True]
        
    def textbox(self, events, inputbox):
        if inputbox == True:
            if events.key == pygame.K_BACKSPACE:
                self.inputcheck[0] = str(self.inputcheck[0])[:-1]
            if events.key != pygame.K_RETURN:
                self.inputcheck[0] += events.unicode
            if events.key == pygame.K_RETURN:
                self.inputcheck[1] = False
            if events.key == pygame.K_BACKSPACE:
                self.inputcheck[0] = str(self.inputcheck[0])[:-1]

    def background():
        UIbackground = pygame.image.load("assets/weatherapibackground.png")
        UIbackground = pygame.transform.scale(UIbackground, (526,526))
        return UIbackground
    
    def weatherimage(iconurl):
        img = io.BytesIO(requests.get(str(f"https:{iconurl}")).content)
        weathericon = pygame.image.load(img)
        weathericon = pygame.transform.scale(weathericon, (180,180))
        return weathericon