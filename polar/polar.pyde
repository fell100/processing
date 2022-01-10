angle = 0
r = 150
WIDTH = 1000
LENGTH = 1000
Rcolor = 0
Gcolor = 0
Bcolor = 0
direction = 1

def setup():
    size(WIDTH,LENGTH)
    global pg
    
    pg = createGraphics(WIDTH, LENGTH)
    background(0)


def changeColor():
    global Rcolor,Gcolor,Bcolor
    if Rcolor == 0:
        if Gcolor == 0:
            Bcolor+= 32
            if Bcolor == 256:
                Gcolor += 32
                Bcolor = 0
        else:
            Bcolor+=32
            if Bcolor == 256:
                Gcolor+=32
                Bcolor = 0
                if Gcolor == 256:
                    Rcolor += 32
                    Gcolor = 0
                    Bcolor = 0
    else:
        if Gcolor != 256:
            Bcolor+=32
            if Bcolor == 256:
                Bcolor = 0
                Gcolor+=32
        else:
          Gcolor = 0
          Bcolor = 0
          Rcolor += 32
        if Rcolor == 256:
            Rcolor = 0
            Gcolor = 0
            Bcolor = 0        



def draw():
    global angle, r, pg, Rcolor,Gcolor,Bcolor, numRGB
    pg.beginDraw()
     
    # Rcolor += random(-5,5)
    # Gcolor += random(-5,5)
    # Bcolor += random(-10,10)



    def createBall():

        global angle, r, pg, Rcolor, Gcolor, Bcolor, direction
        
        pg.stroke(Rcolor,Gcolor,Bcolor)
        pg.strokeWeight(20)
        pg.noFill()
        pg.translate(500,500)
        x = r * cos(angle)
        y = r * sin(angle)
        r += 2 * direction
        angle += 0.018
        if r == 252:
            direction *= -1
        if r == 0:
            direction *= -1
        pg.point(x,y)
        pg.strokeWeight(10)
        pg.circle(0, 0, 530)
        pg.noFill()
        pg.stroke(255, 10)
        
        pg.strokeWeight(10)
        pg.point(0,0)
        pg.stroke(255, 10)
        changeColor()
        
        
    pg.background(0, 10)
    
    createBall()
    pg.endDraw()
    image(pg, 0, 0)
    
     
