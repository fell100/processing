r = 450
total = 0
in_circle = 0

def setup():
    
    
    size(1000, 1000)
    background(0)
    translate(width/2, height/2)
    stroke(255)
    noFill()
    ellipse(0,0,r * 2,r * 2)
    rectMode(CENTER)
    rect(0,0,r * 2,r * 2)
    
    

def draw():
    global total, in_circle, r
    translate(width/2, height/2)
    pi = 0
    
    for i in range(0, 10000):
        x = random(-r, r)
        y = random(-r, r)
        total += 1
        #d = sqrt(x * x + y * y)
        d = (x * x + y * y)
        #if(d < r):
        if(d < r * r):   
            in_circle += 1
            stroke(66, 239, 245, 75)
        else:
            stroke(0, 139, 181, 75)
        
        pi = 4 * (float(in_circle) / float(total)) 
        
        point(x,y)
            
    print(pi)
