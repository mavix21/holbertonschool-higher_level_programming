#!/usr/bin/node

const request = require('request');
const mainUrl = process.argv[2];

if (!mainUrl) {
  console.log('Please, provide an url');
  process.exit(1);
}

async function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        console.log(error);
        reject(error);
        return;
      }

      const characterName = JSON.parse(body).name;
      resolve(characterName);
    });
  });
}

request.get(mainUrl, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const filmObjects = JSON.parse(body).results; // array of film objects
  let count = 0;
  const characterNamePromises = [];

  for (const filmObj of filmObjects) {
    for (const url of filmObj.characters) {
      characterNamePromises.push(getCharacterName(url));
    }
  }

  const characterNames = await Promise.all(characterNamePromises);

  for (const characterName of characterNames) {
    if (characterName === 'Wedge Antilles') {
      count++;
    }
  }

  console.log(count);
});
