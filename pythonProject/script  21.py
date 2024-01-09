# Player de musíca
import pygame
pygame.init()
pygame.mixer.music.load('m01.mp3') #carregar a música
pygame.mixer.music.play() #play música
input()
pygame.event.wait()
