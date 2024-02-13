#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
      if ((h > 0) && (w > 0)) {
        this.width = w;
        this.height = h;
    }
  }
    print() {
      for (; this.height >= 1; this.height--) {
        let x = 'X';
        console.log(x.repeat(this.width));
    }
  }
    rotate() {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
  }
    double() {
      this.width = 2 * this.width;
      this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
