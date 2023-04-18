#!/usr/bin/node
const process = require('process');

const argc = process.argv.length;
let output;

if (argc <= 2) {
  output = 'No argument';
} else if (argc === 3) {
  output = 'Argument found';
} else {
  output = 'Arguments found';
}

console.log(output);
