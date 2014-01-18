#!/usr/bin/env python

import math
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import random
import sys

time_to_wait = random.randint( 1500, 3000 )
time = time_to_wait


screen_width = 640
screen_height = 480
screen_size = screen_width, screen_height
press_events = press_events = pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN

screen = None

wait_time = 2000 #Wait for 2 seconds


def write_text( screen, text, color, big ):
    if big:
        height= screen.get_height() / 9
        up = screen.get_height() / 2
    else:
        height = screen.get_height() / 12
        up = screen.get_height() - ( screen.get_height() /24 )
    font = pygame.font.Font( None, height )
    rend = font.render( text, 1, color )
    textpos = rend.get_rect(
        centerx = screen.get_width() / 2,
        centery = up
    )
    screen.blit( rend, textpos )

def timed_wait( time_to_wait, event_types_that_cancel ):
    """
    Wait for time_to_wait, but cancel if a relevant event happens.
    Return True if cancelled, or False if we waited the full time.
    """

    start_time = pygame.time.get_ticks()

    finished_waiting_event_id = pygame.USEREVENT + 1
    pygame.time.set_timer( finished_waiting_event_id, time_to_wait )

    try:

        pygame.event.clear()

        pressed = False
        waiting = True
        time = time_to_wait
        while waiting:
            evt = pygame.event.wait()
            if is_quit( evt ):
                quit()
            elif evt.type in event_types_that_cancel:
                waiting = False
                pressed = True
                time = pygame.time.get_ticks()-start_time
            elif evt.type == finished_waiting_event_id:
                waiting = False
    finally:
        pygame.time.set_timer( finished_waiting_event_id, 0 )

    return pressed, time



def start():
    global screen
    pygame.init()
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )

def quit():
    pygame.quit()
    sys.exit()

def ready_screen():
    screen.fill( pygame.Color( "black" ) )
    white = pygame.Color("white")
    write_text( screen, "Welcome to the Pyg Latin Translator!", white, True )

    white = pygame.Color("white")
    write_text( screen, "Press any key to get started.", white, False )

    pygame.display.flip()

    timed_wait( 0, press_events )

def wait():
    time_to_wait = 2000 # 2 seconds
    timed_wait( time_to_wait, () )

def is_quit( evt ):
    return ( 
        evt.type == pygame.QUIT or
        (
            evt.type == pygame.KEYDOWN and
            evt.key == pygame.K_ESCAPE
        )
    )


def get_key():
    while 1:
      event = pygame.event.poll()
      if event.type == KEYDOWN:
        return event.key
      else:
        pass

def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    fontobject = pygame.font.Font(None,50)

    if len(message) != 0:
      screen.blit(fontobject.render(message, 1, (255,255,255)),
                  ((screen.get_width() / 2) - 200, (screen.get_height() / 2) - 10))
    
    pygame.display.flip()



def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    original = []
    display_box(screen, question + ": " + string.join(original,""))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
              original = original[0:-1]
        elif inkey == K_RETURN:
              break
        elif inkey == K_MINUS:
              original.append("_")
        elif inkey <= 127:
              original.append(chr(inkey))
        display_box(screen, question + ": " + string.join(original,""))
    return string.join(original,"")

    pygame.display.flip()

    timed_wait( 0, press_events )

def check(translate_this):
   pyg = "ay"

   if len(translate_this) > 0 and translate_this.isalpha():
       word = translate_this.lower()
       first = translate_this[0]

       if first =="a" or first == "e" or first =="i" or first == "o" or first == "u" or first == "y":
           new_word = word + pyg
           return new_word
           print new_word
        
       else:
          s = word
          second = s[1]
          if second =="a" or second == "e" or second =="i" or second == "o" or second == "u" or second == "y":
              new_word = s[1:]+s[0]+pyg
          else:
              new_word = s[2:]+s[0:2]+pyg
          print new_word
          return new_word
   else:
       print "Hey! That's not a word!"
       return "Hey! That's not a word!"
       pygame.display.flip()
       timed_wait( 1000, press_events )
       
       question_2(again)

       again = raw_input("Give me another word")

       if again.isalpha() == False:
           print "You're not playing by the rules...come back when you want to play nice"
           return "You're not playing by the rules...come back when you want to play nice"



def question_1():
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    input1 = ask(screen, "Word to Translate")
    pygame.display.flip()


    ##This bit prints the word to translate to the screen

    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    white = pygame.Color("white")
    write_text( screen, "Translating : " + input1, white, True )
    pygame.display.flip()
    timed_wait( 1000, press_events )

    ##This bit prints the word to translate and result to console

    print input1

    ##This bit prints the result to the screen
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    white = pygame.Color("white")
    write_text( screen, "The translation is : " +check(input1), white, True )
    pygame.display.flip()
    timed_wait( 2000, press_events )



def question_2():
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    input2 = ask(screen, "Give me another word ")
    pygame.display.flip()


    ##This bit prints the word to translate to the screen

    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    white = pygame.Color("white")
    write_text( screen, "Translating : " + input1, white, True )
    pygame.display.flip()
    timed_wait( 1000, press_events )

    ##This bit prints the word to translate and result to console

    print input2

    ##This bit prints the result to the screen
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    white = pygame.Color("white")
    write_text( screen, check(input1), white, True )
    pygame.display.flip()
    timed_wait( 2000, press_events )


def end():
    screen = pygame.display.set_mode( screen_size, pygame.FULLSCREEN )
    screen.fill( pygame.Color( "black" ))
    white = pygame.Color( "white" )
    write_text( screen, "Anksthay orfay ayingplay!", white, True)

    white = pygame.Color( "white" )
    write_text( screen, "Press any key to exit", white, False)
    
    pygame.display.flip()
    timed_wait( 2000, press_events )

# We start from here

start()

ready_screen()

question_1()
    
end()
