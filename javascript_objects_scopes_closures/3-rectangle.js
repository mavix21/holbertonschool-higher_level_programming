#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const repr = [];
    for (let i = 0; i < this.height; i++) {
      repr.push('X'.repeat(this.width));
    }

    console.log(repr.join('\n'));
  }
}

module.exports = Rectangle;
