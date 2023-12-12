#!/usr/bin/node
const sqrt = require('./5-square');
class Square extends sqrt {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let j = 0; j < this.height; j++) {
        for (let i = 0; i < this.width; i++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
}
module.exports = Square;
