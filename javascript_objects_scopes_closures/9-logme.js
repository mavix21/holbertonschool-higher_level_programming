#!/usr/bin/node

let printCounter = 0;
const logMe = (item) => {
  console.log(`${printCounter}: ${item}`);
  printCounter++;
};

module.exports = { logMe };
