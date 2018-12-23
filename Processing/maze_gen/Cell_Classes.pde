class Cell
{
  int i;
  int j;
  Boolean[] walls;
  Boolean visited;
  color col;

  
  Cell(int i, int j){
    this.i = i;
    this.j = j;
    walls = new Boolean[]{true,true,true,true};
    this.visited = false;
    this.col = color(0,255,255,0);
  }

  /* Checks neighbors and returns next cell */
  Cell checkNeighbors(){
    ArrayList<Cell> neighbors = new ArrayList<Cell>();
    
   
    if(index(i, j-1) != -1){
      Cell top = grid.get(index(i, j-1));
      if(!top.visited){
        neighbors.add(top);
      }
    }
    if(index(i, j+1) != -1){
      Cell bottom = grid.get(index(i, j+1));
      if(!bottom.visited){
        neighbors.add(bottom);
      }
    }
    if(index(i - 1, j) != -1){
      Cell left = grid.get(index(i - 1, j));
      if(!left.visited){
        neighbors.add(left);
      }
    }
    if(index(i + 1, j) != -1){
      Cell right = grid.get(index(i + 1, j));
      if(!right.visited){
        neighbors.add(right);
      }
    }
    
    
    if (neighbors.size() > 0){
      int r = floor(random(0, neighbors.size()));
      return neighbors.get(r);
    } else {
      return null;
    }
    
  
}
  void highlight(){
    int x = this.i*w;
    int y = this.j*w;
    noStroke();
    fill(bgcol);
    rect(x,y,w,w);
  }
  void show(){
    int x = this.i * w;
    int y = this.j * w;
    stroke(255);
    if(w > 10){
      strokeWeight(w/10);
    }else{
      strokeWeight(1);
    }
    
     
    if(walls[0]){
    line(x,y,x+w,y);
    }
    if(walls[1]){
    line(x+w,y,x+w,y+w);
    }
    if(walls[2]){
    line(x+w,y+w,x,y+w);
    }
    if(walls[3]){
    line(x,y+w,x,y);
    }
    if(this.visited){
      fill(this.col);
      noStroke();
      rect(x,y,w,w);
    }
    
  }

}
