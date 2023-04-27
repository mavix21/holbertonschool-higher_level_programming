#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const fileContent = process.argv[3] || '';

if (!filePath) {
  console.log('Please specify a file path');
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
