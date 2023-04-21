#!/usr/bin/node

const { argv, exit } = require('process');

if (argv.length <= 3) {
  console.log(0);
  exit();
}

const arrayOfNumbers = [...argv.slice(2)].map(Number);
let largest = -Infinity;
let secondLargest = -Infinity;

for (const num of arrayOfNumbers) {
  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest) {
    secondLargest = num;
  }
}

console.log(secondLargest);
