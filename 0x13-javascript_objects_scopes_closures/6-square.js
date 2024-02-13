#!/usr/bin/node
const ParentSquare = require('./5-square.js');
class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = this.height; i >= 1; i--) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
