#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    const char = c || 'X';

    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
