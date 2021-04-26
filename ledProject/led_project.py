'''
import opc

led_colour=[(0,0,0)]

client = opc.Client('localhost:7890') #connecting to simulator
print(enumerate(led_colour))
for count, item in enumerate(led_colour):
    print(count, item)
    if item[0]==5:
        #need to get values out of tuple
        r, g, b = item[1]
        r = 0
        g = 0

        #create changed tuple (uses some values from old and some new)
        new_colour =(r,g,b)
        led_colour[item[0]]= new_colour

client.put_pixels(led_colour) #sends values to led simulator
#need to send it twice if not constantly sending values
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
#print(led_colour)
'''
print("Hello")
