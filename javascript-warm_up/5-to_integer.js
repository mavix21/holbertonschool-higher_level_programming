#!/usr/bin/node
const process = require('process');

const { argv } = process;

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
