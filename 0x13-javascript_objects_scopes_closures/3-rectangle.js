#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (; this.height >= 1; this.height--) {
      let x = 'X';
      console.log(x.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
