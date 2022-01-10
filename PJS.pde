static final float A = 10, B = 28, C = 8/3.;
static final float DT = .01;
 
static final boolean IS_PJS = 1/2 == 1/2.;
 
float x = .1, y = .1, z = .1;
boolean paused;
 
void setup() {
  size(800, 600, P3D);
  smooth(4);
  frameRate(60);
 
  background(0);
  stroke(#FF0000);
  strokeWeight(5);
  line(width>>1, height>>1, width, height);
 
  stroke(#FF00FF);
  if (!IS_PJS) strokeWeight(1);
}
 
void draw() {
  final float dx = DT * (A * (y - x));
  final float dy = DT * (x * (B - z) - y);
  final float dz = DT * (x*y - C*z);
 
  translate(width>>1, height>>1);
  scale(5);
  point(x += dx, y += dy, z += dz);
}
 
void mousePressed() {
  if (paused ^= true)  noLoop();
  else                 loop();
}