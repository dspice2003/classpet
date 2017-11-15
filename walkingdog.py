from sense_hat import SenseHat import time s = SenseHat() s.low_light = 
True green = (0, 255, 0) yellow = (255, 255, 0) blue = (0, 0, 255) red = 
(255, 0, 0) white = (255,255,255) nothing = (0,0,0) pink = (255,105, 
180) white = (255,255,255) def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    P = pink
    W = white
    logo = [
    O, O, O, O, O, O, O, O,
    P, O, O, O, O, O, O, O,
    O, P, O, O, P, O, P, O,
    O, P, G, G, P, Y, Y, O,
    O, G, G, G, Y, W, Y, G,
    O, G, G, G, G, Y, Y, O,
    O, G, O, G, O, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo def raspi_logo():
    G = green
    R = red
    O = nothing
    Y = yellow
    P = pink
    W = white
    logo = [
    O, O, O, O, O, O, O, O,
    P, O, O, O, O, O, O, O,
    O, P, O, O, P, O, P, O,
    O, P, G, G, P, Y, Y, O,
    O, G, G, G, Y, W, Y, G,
    O, G, G, G, G, Y, Y, O,
    O, O, G, O, G, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo images = [trinket_logo, trinket_logo, raspi_logo, 
raspi_logo,] count = 0 while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
