var drop= [];
//let video;

function setup() {
  createCanvas(500, 500); 
  for (var i = 0; i < 150; i++)
    drop[i] = new Drop();
}

function draw() {
  background(33);
  for (var i = 0; i < 150; i++) { 
    drop[i].show();
  drop[i].update();
  }
}

function Drop() {
  this.x = random(0,width);
  this.y = random(0,-height);
  
  this.show = function(){
    noStroke();
    fill(255);
    ellipse(this.x, this.y, 2, 10);
  }
  
  this.update = function() {
    this.speed = random(5, 15);
    this.gravity = 1.05;
    this.y = this.y + this.speed*this.gravity;
    
    if(this.y > height){
      this.y = random(0, -height);
      this.gravity = 0;
    }
  }
}

// I am trying to add this part but it is not working. also line2
//function setup() {
  //createCanvas(640, 480);
  //video = createCapture(VIDEO);
  //video.hide();
//}

//function draw() {
  //background(220);
  //image(video, 0, 0);
//}
