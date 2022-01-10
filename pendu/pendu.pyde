angle = 0
angleV = 0.03
Rcolor = 100
Gcolor = 200
Bcolor = 50
rotation = 1

def setup():
    size(1000,1000)
    global pg
    
    pg = createGraphics(1000, 1000)
    background(0)
    
def draw():
    global angle, angleV, Rcolor, Gcolor, Bcolor, rotation
    incX = map(cos(angle),-1,1,50,50)
    incY = map(sin(angle),-1,1,-150,150) 
    
    
    
    pg.beginDraw()
    
    Rcolor += random(-5,5)
    Gcolor += random(-5,5)
    Bcolor += random(-5,5)
    
    rotation += 0.05
    
    pg.background(0,10)
    pg.translate(500,500)
    pg.fill(Rcolor, Gcolor, Bcolor)
    # r = map(sin(angle),-1,1,0,200)
    y = map(sin(rotation)*sin(angle + HALF_PI),-1,1,-400,400)
    x = map(cos(rotation)*cos(angle/2),-1,1,-500,500)
    # rotateX(angle*0,01)
    pg.stroke(Rcolor, Gcolor, Bcolor)
    pg.line(0,0,x,y)
    pg.circle(x,y,32)
    #increment = TWO_PI / 60
    angle += angleV
    
    # rotation = range(0, TWO_PI)
    # rotate(rotation, x, y, 0)
    pg.endDraw()
    image(pg, 0, 0)
