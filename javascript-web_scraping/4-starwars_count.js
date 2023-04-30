#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

if (!url) {
  console.log('Please, provide an url');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  let counter = 0;
  const filmObjects = JSON.parse(body).results; // array of film objects
  for (const filmObj of filmObjects) {
    for (const url of filmObj.characters) {
      if (url.includes(characterId)) counter++;
    }
  }

  console.log(counter);
});
