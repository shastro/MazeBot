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
    
   
    if(index(i, j-1) != -1){ //If not on edge
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
    
    /*
    if (neighbors.size() > 0){
      int r = floor(random(0, neighbors.size()));
      return neighbors.get(r);
    } else {
      return null;
    }
    */
    if(neighbors.size() > 0){
      float r = random(0,1);
      int r2 = floor(random(0, neighbors.size()));
      //println(r);
      if (r <= 0.25 && neighbors.size() > 0){
        return neighbors.get(0);
      } else if (r >= 0.25 && r <= 0.5 && neighbors.size() > 1){
        return neighbors.get(1);
      } else if (r >= 0.50 && r <= 0.75 && neighbors.size() > 2){
        return neighbors.get(2);
      } else if (r >= 0.75 && r <= 1 && neighbors.size() > 3){
        return neighbors.get(3);
      } else {
        println("yes");
        println(r);
        println(r2);
        println(neighbors.size());
        return neighbors.get(r2);
      }
    }else{
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
