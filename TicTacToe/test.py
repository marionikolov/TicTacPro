#! /usr/bin/env python
import pygame
import time
import os, sys
print ('Splash load...')
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((200,200),pygame.NOFRAME)
pygame.Surface([640,480], pygame.SRCALPHA, 32)
splash=pygame.image.load("images\misc\splash.png")
screen.blit(splash,(-50,-60))
pygame.display.flip()
time.sleep(5)
