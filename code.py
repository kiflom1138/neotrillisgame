import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()

red = (101,0,255)
blue = (100,0,50)
color = red





while True:
   
    keys = trellis.pressed_keys
   
    if len (keys) > 0:
       
        
        if color == red:
            color = blue
        elif color == blue :
            color = red
        trellis.pixels[keys[0]] = (color)
        time.sleep(.5)
    
    for i in range(8):
        if trellis.pixels[i, 0] != (0, 0, 0) and trellis.pixels[i, 1] == (0, 0,0):
            drop_color= trellis.pixels[i, 0]
            time.sleep(.5)
            trellis.pixels[i, 0] = (0, 0, 0)
            trellis.pixels[i, 1] = (drop_color)
        
        if trellis.pixels[i, 1] != (0, 0, 0) and trellis.pixels[i, 2] == (0, 0,0):
            drop_color= trellis.pixels[i, 1]
            time.sleep(.5)
            trellis.pixels[i, 1] = (0, 0, 0)
            trellis.pixels[i, 2] = (drop_color)
            
            
        if trellis.pixels[i, 2] != (0, 0, 0) and trellis.pixels[i, 3] == (0, 0,0):
            drop_color= trellis.pixels[i, 2]
            time.sleep(.5)
            trellis.pixels[i, 2] = (0, 0, 0)
            trellis.pixels[i, 3] = (drop_color)
    
    
    
    # if trellis.pixels[0, 3] != (0, 0, 0) and trellis.pixels[0, 4] == (0, 0,0):
    #     drop_color= trellis.pixels[0, 3]
    #     time.sleep(.5)
    #     trellis.pixels[0, 3] = (0, 0, 0)
    #     trellis.pixels[0, 4] = (drop_color)
        
        
    
