#!/usr/bin/env python

import opc #this is for connecting to simulator and sending pixels
import time #this is for delay functions

led_colour=[(0,0,0)]*360 #main list with 360 tuples

#declaring positions for letters to spell out brazil
B = [63,64,65,66,123,126,183,184,185,186,243,246,303,304,305,306] #values for letter B
R = [130,132,133,190,191,250,310] #values for letter r
A = [138,197,199,256,257,258,259,260,315,321] #values for letter a
S = [156,157,158,159,216,276,277,278,279,336,337,338,339]
I = [163,164,165,224,284,343,344,345]
L = [169,229,289,349,350,351]

#values for colours I will be using
black = (0,0,0)
white = (255,255,255)
purple = (175,0,164)
yellow = (255,255,0)
blue = (59,0,255)
baby_blue = (66,245,239)
red = (233,0,0)
green = (81,186,52)

#this is for a user input check:
acceptable_colours = ['r', 'g', 'b', 'R', 'G', 'B']

client = opc.Client('localhost:7890') #connecting to simulator/lights

#declaring functions that will create the flags:
def brazil():
    for count, item in enumerate(led_colour):#iterate through 360 LEDs
        #if count inside position of letters, pixel will be green:
        if count in B:
            led_colour[count] = green
        if count in R:
            led_colour[count] = green
        if count in A:
            led_colour[count] = green
        if count in S:
            led_colour[count] = green
        if count in I:
            led_colour[count] = green
        if count in L:
            led_colour[count] = green

        #changed tuple for half of brazil flag: (I am doing half because the full flag would not work)
        if (count==29) or (count>87 and count<91) or (count>146 and count<152) or (count>205 and count<213) or (count>264 and count<274) or (count>323 and count<335):
            led_colour[count]= yellow
            if (count > 147 and count < 151) or (count > 206 and count < 212) or (count > 265 and count < 273) or (count > 324 and count < 334):
                led_colour[count] = blue
                if(count == 149 or count == 209 or count == 269 or count == 329):
                    led_colour[count] = white

def italy():
    for count, item in enumerate(led_colour):#iterate through 360 LEDs (with an index (count))
        #green part of flag:
        if count % 60 <= 20:
            led_colour[count] = green
        #white part of flag:
        if (count % 60 <= 40) and (count % 60 >= 20):
            led_colour[count] = white
        #red part of flag:
        if (count % 60 >= 40) and (count % 60 <= 80):
            led_colour[count] = red

def france():
    for count, item in enumerate(led_colour):#iterate through 360 lEDs (with an index (count))
        #blue part of flag:
        if count % 60 <= 20:
            led_colour[count] = blue
        #white part of flag:
        if (count % 60 <= 40) and (count % 60 >= 20):
            led_colour[count] = white
        #red part of flag:
        if (count % 60 >= 40) and (count % 60 <= 80):
            led_colour[count] = red

def netherlands():
    for count, item in enumerate(led_colour):#iterate through 360 LEDs (with an index (count))
        #black part of flag:
        if count % 360 <= 120:
            led_colour[count] = red
        #red part of flag:
        if (count % 360 >= 120) and (count % 360 < 240):
            led_colour[count] = white
        #yellow part of flag:
        if (count % 360 >= 240) and (count % 360 < 360):
            led_colour[count] = blue

x = 0

def menu(): #this is the main menu for selecting the flags
    #this will be displayed on the screen
    print('\nPlease choose a flag to be displayed:')
    print('\n1. Brazil\n2. Italy\n3. France\n4. Netherlands\n')
    x = int(input()) #user input is assigned to variable x
    #check if user input is within the acceptable values:
    while(x not in (1,2,3,4)):
        print('\nPlease enter a valid input!\n')
        x = int(input()) #user input is assigned to variable x
    #depending on the user input return a different flag:
    if x == 1:
        return brazil()
    elif x == 2:
        return italy()
    elif x == 3:
        return france()
    elif x == 4:
        return netherlands()


def menu_flashing(): #this menu asks for user input in order to flash the flag
    print("\nHow many times do you want to flash the selected flag? (value must be between 1 and 10)")
    y = int(input())
    while (y < 1) or (y>10): #this checks for user input between 1 and 10
        print("\nPlease enter a valid input:\t")
        y = int(input())
    flash(y) #calls function that flashes the flag

def menu_weather(): #this will print 1 message for the rain function and one message for the sun and rain function
    print("\nWe are in london, so we might as well make it rain!\n")
    rain() #calls rain function
    print("\nOk, now let's have a some sun in between the rain\n")
    sun_and_rain() #calls sun and rain function
    print("\n\n")


#fade function:
def fade(colour): #this function requires an input from the user to be executed
    fade_amount = 1
    r,g,b = (0,0,0)
    if colour == 'r' or colour == 'R': #if input is r
        while (r < 255): #fade the red pixel from 0 to 255
            r += fade_amount
            fade_colour = [(r,g,b)]*360
            time.sleep(0.01)
            client.put_pixels(fade_colour)
        while (r > 0): #fade the red pixel from 255 to 0
            r -= fade_amount
            fade_colour = [(r,g,b)]*360
            time.sleep(0.01)
            client.put_pixels(fade_colour)
    elif colour == 'g' or colour == 'G': #if input is g
        while (g < 255): #fade the green pixel from 0 to 255
            g += fade_amount
            fade_colour = [(r,g,b)]*360
            time.sleep(0.01)
            client.put_pixels(fade_colour)
        while (g > 0): #fade the green pixel from 255 to 0
            g -= fade_amount
            fade_colour = [(r,g,b)]*360
            time.sleep(0.01)
            client.put_pixels(fade_colour)
    elif colour == 'b' or colour == 'B': #if input is b
            while (b < 255): #fade the blue pixel from 0 to 255
                b += fade_amount
                fade_colour = [(r,g,b)]*360
                time.sleep(0.01)
                client.put_pixels(fade_colour)
            while (b > 0): #fade the green pixel from 255 to 0
                b -= fade_amount
                fade_colour = [(r,g,b)]*360
                time.sleep(0.01)
                client.put_pixels(fade_colour)



def flash(num_times): #this will flash the flag with the input from the user
    i = 0
    while (i < num_times): #iterate through the user input
        #make screen all black:
        blackout = [black]*360
        client.put_pixels(blackout)
        time.sleep(0.5) #delay
        #display selected flag on screen (stored on list led_colour)
        client.put_pixels(led_colour)
        time.sleep(0.5)#delay
        i += 1 #update iteration variable

def sun_and_rain():
    i = 0 #iteration variable
    rained = [black]*360
    client.put_pixels(rained) #make screen all black
    for i in range(0,360): #iterate through all LEDs
        if i%2 == 0: #even numbers will be baby blue
            rained[i] = baby_blue
            time.sleep(0.03)
            client.put_pixels(rained)
        if i%2 != 0: #odd numbers will be yellow
            rained[i] = yellow
            time.sleep(0.03)
            client.put_pixels(rained)


def rain(): #this will fill every other pixel with the baby blue colour
    blackout = [black]*360
    client.put_pixels(blackout) #this makes the screen all black
    for i in range(0,360): #iterate inside all pixels
        if i%2 ==0:
            blackout[i] = baby_blue
            time.sleep(0.03)
            client.put_pixels(blackout)


while 1:
    menu()
    client.put_pixels(led_colour) #sends values to led simulator
    #need to send it twice if not constantly sending values
    #due to interpolation setting on fadecandy
    client.put_pixels(led_colour)
    time.sleep(3) #adds a delay
    menu_flashing() #asks for user input and then flashes selected flag
    #this is the menu for fading one of three colors:
    print("\nchoose a colour to fade: enter r for red, g for green or b for blue:\t")
    z = input() #asks for user input and assign to a var z
    while z not in acceptable_colours: #user gets stuck in this loop if he does not enter an acceptable input
        print("\nPlease enter a valid input!")
        print("\nchoose a colour to fade: enter r for red, g for green or b for blue:\t")
        z = input()
    fade(z) #call the fade function
    menu_weather() #make it rain and make it sunny
