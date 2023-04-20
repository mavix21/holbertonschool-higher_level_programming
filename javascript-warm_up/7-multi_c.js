#!/usr/bin/node

const { argv, exit } = require('process');
const numberOfOccurrences = argv[2];

if (isNaN(numberOfOccurrences)) {
  console.log('Missing number of occurrences');
  exit(1);
}

for (let i = 0; i < +numberOfOccurrences; i++) {
  console.log('C is fun');
}
