#!/usr/bin/node

const { argv } = require('process');
const arg1 = +argv[2];
const arg2 = +argv[3];

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(arg1, arg2);
