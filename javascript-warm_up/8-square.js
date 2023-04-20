#!/usr/bin/node

const { argv, exit } = require('process');
const size = parseInt(argv[2], 10);

if (isNaN(size)) {
  console.log('Missing size');
  exit(1);
}

let square = '';
for (let i = 0; i < size; i++) {
  square += 'X'.repeat(size);
  if (i !== size - 1) {
    square += '\n';
  }
}

console.log(square);
