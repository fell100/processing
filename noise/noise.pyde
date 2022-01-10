inc = 0.01
WIDTH = 200
HEIGHT = 200

def setup():
    
    size(WIDTH, HEIGHT)
    global pg
    
    pg = createGraphics(WIDTH, HEIGHT)
    background(0)
    

def draw():
    global pg, WIDTH, HEIGHT, inc
    
    pg.beginDraw()
    # x = 0
    # for x in range(0, WIDTH):
    #     pg.stroke(100, 100, 100)
    #     # #pg.circle(x, random(HEIGHT), 30)
    #     pg.point(x, random(HEIGHT))
    #     x += 1
    # pg.stroke(255)
    
    
    pg.loadPixels()
    
    for x in range(0, WIDTH):
        
        for y in range(0, HEIGHT):
            index = (x + y * WIDTH) * 4
            print(index)
            pg.pixels[index + 0] = color(255,0,0)
            pg.pixels[index + 1] = 0
            pg.pixels[index + 2] = 0
            pg.pixels[index + 3] = 255
    pg.updatePixels()
    pg.endDraw()
    pg.background(0, 10)
    image(pg, 0, 0)
