#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Please, provide a URL and a file path');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }

  fs.writeFile(filePath, body, { encoding: 'utf-8' }, (error) => {
    if (error) {
      console.error(`Error writing file: ${error.message}`);
      process.exit(1);
    }

    // console.log(`File saved to ${filePath}`);
  });
});
