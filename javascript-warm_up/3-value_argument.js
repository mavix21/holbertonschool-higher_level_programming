#!/usr/bin/node
const process = require('process');

const { argv } = process;

if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
