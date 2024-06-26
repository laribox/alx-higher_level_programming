#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (character) {
    if (character === undefined) {
      character = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += character;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
