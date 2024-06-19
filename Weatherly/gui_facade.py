import pygame
import requests
import io
import direct_information_subsystem
import pygame_subsystem
import json

SCREENHEIGHT = 620
SCREENWIDTH = 900
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.init()

titlefavicon = pygame.image.load('assets/favicon.png')
pygame.display.set_icon(titlefavicon)
pygame.display.set_caption('Weatherly')

class finalfacade:
    def locdata(location):
        global necessarydata
        necessarydata = direct_information_subsystem.DirectInfo.get_weather_information_from_location(location)
        return necessarydata
    
    def ipdata():
        global necessarydata
        necessarydata = direct_information_subsystem.DirectInfo.get_weather_information_from_ip()
        return necessarydata
    
    def textboxallowance():
        weatherguy = pygame_subsystem.weatherpygame
        return weatherguy

    def areaplacement():
        global necessarydata
        fontsize = 40
        UVwords = necessarydata["uv"]
        Forecast = necessarydata["forecast"]
        AstronomyA = necessarydata["sunrise_sunset"]['sunrise']
        AstronomyB = necessarydata["sunrise_sunset"]['sunset']
        Humidity = necessarydata["humidity"]
        wind = necessarydata["wind"]
        pressure = necessarydata["pressure"]
        visibility = necessarydata["visibility"]
        UVwordstext = pygame_subsystem.weatherpygame.textintoimage(UVwords,fontsize-8)
        astronomyatext = pygame_subsystem.weatherpygame.textintoimage(AstronomyA,fontsize-8)
        astronomybtext = pygame_subsystem.weatherpygame.textintoimage(AstronomyB,fontsize-8)
        humiditytext = pygame_subsystem.weatherpygame.textintoimage(Humidity,fontsize-9)
        windtext = pygame_subsystem.weatherpygame.textintoimage(wind,fontsize-8)
        pressuretext = pygame_subsystem.weatherpygame.textintoimage(pressure,fontsize-8)
        visibilitytext = pygame_subsystem.weatherpygame.textintoimage(visibility,fontsize-8)
        screen.blit(UVwordstext, (399-pygame.Surface.get_width(UVwordstext)/2,52+79-24))
        screen.blit(astronomyatext,(415-pygame.Surface.get_width(astronomyatext)/2,246+78-30))
        screen.blit(astronomybtext,(570-pygame.Surface.get_width(astronomybtext)/2,246+78-30))
        screen.blit(humiditytext, (320+368+79-pygame.Surface.get_width(humiditytext)/2,246+50))
        screen.blit(windtext, (400-pygame.Surface.get_width(windtext)/2,478))
        screen.blit(pressuretext, (320+184+79-pygame.Surface.get_width(pressuretext)/2,478))

        screen.blit(visibilitytext, (320+368+79-pygame.Surface.get_width(visibilitytext)/2,478))
        for iteration, time in enumerate(Forecast):
            temptext = pygame_subsystem.weatherpygame.textintoimage(str(Forecast[time])+"°", 20)
            screen.blit(temptext, (550+(43*iteration)-pygame.Surface.get_width(temptext)/2, 115))
            
        
        
    def standardscreen(otheroption):
        global necessarydata
        fontsize = 40
        thisscreen = True
        outputs = [True, otheroption]
        background = pygame_subsystem.weatherpygame.background()
        weathericon = pygame.image.load(necessarydata['fluenticon'])
        while thisscreen:
            screen.fill(("#F3F3F3"))
            #Getting Data
            location1 = pygame_subsystem.weatherpygame.textintoimage((f"{necessarydata["location"]["name"]},"), 14)
            location2 = pygame_subsystem.weatherpygame.textintoimage(necessarydata['location']["region"], 14)
            locationchange = pygame_subsystem.weatherpygame.textintoimage("Change Location", 14, True)
            locationchangehitbox = pygame.Rect(70,561, pygame.Surface.get_width(locationchange), pygame.Surface.get_height(locationchange))
            temperature = pygame_subsystem.weatherpygame.textintoimage(str(int(necessarydata["current_temp"])), 96)
            condition = pygame_subsystem.weatherpygame.textintoimage(necessarydata['condition'], 20)

            #Placing on Screen
            screen.blit(background, (320,52))
            screen.blit(weathericon, (65, 120))
            screen.blit(location1, (70,510))
            screen.blit(location2, (70, 530)) 
            pygame.draw.rect(screen, "#F3F3F3", locationchangehitbox)
            screen.blit(locationchange, (69, 561))
            screen.blit(temperature,(70,290))
            screen.blit(condition,(70,420))
            screen.blit(pygame_subsystem.weatherpygame.textintoimage("°C", 96, light=True), (70+temperature.get_width(), 290))
            finalfacade.areaplacement()
            
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if locationchangehitbox.collidepoint(events.pos):
                        thisscreen = False
                        outputs = [True, True]
                    
            pygame.display.update()
        return outputs
    def locationchangescreen(dimensions):
        oogleyboogley = pygame_subsystem.weatherpygame()
        oogleyboogley.textboxsetup("Enter Location")
        inputbox = False
        locchangescr = True
        while locchangescr:
            screen.fill(("#F3F3F3"))
            locbox = pygame_subsystem.weatherpygame.button(screen, dimensions, 2,0, (f" {oogleyboogley.inputcheck[0]} "))
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if locbox.collidepoint(events.pos):
                        inputbox = True
                        if oogleyboogley.inputcheck[0] == "Enter Location":
                            oogleyboogley.inputcheck[0] = ""
                if events.type == pygame.KEYDOWN:
                    oogleyboogley.textbox(events, inputbox)
            
            locchangescr = oogleyboogley.inputcheck[1]
            if locchangescr == False:
                return [oogleyboogley.inputcheck[0],True, True]
            pygame.display.update()
        



                        