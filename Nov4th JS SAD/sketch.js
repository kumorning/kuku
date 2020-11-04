let r, g, b;

function setup() {
  createCanvas(720, 400);
  // Pick colors randomly
  r = random(255);
  g = random(255);
  b = random(255);
}

function draw() {
  background(0);
  // Draw a circle
  strokeWeight(2);
  stroke(r, g, b);
  fill(r, g, b, 127);
  ellipse(360, 200, 200, 200);
  console.log(r, g, b);
}


function mousePressed() {
 
  let d = dist(mouseX, mouseY, 360, 200);
  if (d < 100) {

    r = random(255);
    g = random(255);
    b = random(255);
  }
}