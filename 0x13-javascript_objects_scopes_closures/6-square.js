#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i >= 1; i--) {
      const x = 'X';
      console.log(x.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = this.size; i >= 1; i--) {
        console.log(c.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
