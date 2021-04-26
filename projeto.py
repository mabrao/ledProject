#!/usr/bin/env python

import opc
import time

led_colour=[(0,0,0)]*360

#declaring positions for letters to spell out brazil
B = [63,64,65,66,123,126,183,184,185,186,243,246,303,304,305,306] #values for letter B
R = [130,132,133,190,191,250,310] #values for letter r
A = [138,197,199,256,257,258,259,260,315,321] #values for letter a
S = [156,157,158,159,216,276,277,278,279,336,337,338,339]
I = [163,164,165,224,284,343,344,345]
L = [169,229,289,349,350,351]


white = (255,255,255)
purple = (175,0,164)
yellow = (255,255,0)
blue = (59,0,255)
red = (233,0,0)
green = (81,186,52)


client = opc.Client('localhost:7890') #connecting to simulator


def brazil():
    for count, item in enumerate(led_colour):

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

        #changed tuple for half of brazil flag:
        if (count==29) or (count>87 and count<91) or (count>146 and count<152) or (count>205 and count<213) or (count>264 and count<274) or (count>323 and count<335):
            led_colour[count]= yellow
            if (count > 147 and count < 151) or (count > 206 and count < 212) or (count > 265 and count < 273) or (count > 324 and count < 334):
                led_colour[count] = blue
                if(count == 149 or count == 209 or count == 269 or count == 329):
                    led_colour[count] = white

def italy():
    for count, item in enumerate(led_colour):
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
    for count, item in enumerate(led_colour):
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
    for count, item in enumerate(led_colour):
        #black part of flag:
        if count % 360 <= 120:
            led_colour[count] = red
        #red part of flag:
        if (count % 360 >= 120) and (count % 360 < 240):
            led_colour[count] = white
        #yellow part of flag:
        if (count % 360 >= 240) and (count % 360 < 360):
            led_colour[count] = blue

#create fade function



while 1:
    #create menu here
    #time.sleep(10) #delay for 10 seconds
    netherlands()
    client.put_pixels(led_colour) #sends values to led simulator
    #need to send it twice if not constantly sending values
    #due to interpolation setting on fadecandy
    client.put_pixels(led_colour)
    break
