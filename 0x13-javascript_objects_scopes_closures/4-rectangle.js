#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }

  rotate () {
    const rotate = this.width;
    this.width = this.height;
    this.height = rotate;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}
module.exports = Rectangle;
