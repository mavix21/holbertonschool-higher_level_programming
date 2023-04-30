#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please, provide a movie Id');
  process.exit(1);
}

const baseUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

// Define a function to get the name of a character given their URL
// The function takes a second argument, a cache (a Map object), that will store
// the names of previously fetched characters, so that if a character has already
// been fetched, we can avoid making another HTTP request
async function getCharacterName (url, cache) {
  // If we already have the name of this character in the cache, return it
  if (cache.has(url)) {
    return cache.get(url);
  }

  // Otherwise, make an HTTP request to get the character's name
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        console.log(error);
        reject(error);
        return;
      }

      // Parse the response body (which should be a JSON object)
      // and extract the name of the character
      const characterName = JSON.parse(body).name;

      // Store the name in the cache for future use
      cache.set(url, characterName);

      // Resolve the promise with the character's name
      resolve(characterName);
    });
  });
}

// Make an HTTP request to get the main Star Wars API endpoint
// We use the "async" keyword here to be able to use "await" later in the function
request.get(baseUrl, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body (which should be a JSON object)
  // and extract the array of urls
  const characterUrls = JSON.parse(body).characters;

  // Initialize a cache object (a Map) to store the names of previously fetched characters
  const cache = new Map();

  // Initialize an array to store promises that will eventually resolve to character names
  const characterNamePromises = [];

  // Loop through the array of character URLs
  for (const url of characterUrls) {
    // Call the getCharacterName function to get the name of the character
    // (passing in the cache object so that we can avoid making unnecessary HTTP requests)
    characterNamePromises.push(getCharacterName(url, cache));
  }

  // Wait for all of the promises to resolve (i.e., for all of the character names to be fetched)
  // and store the resulting array of character names in the "characterNames" variable
  const characterNames = await Promise.all(characterNamePromises);
  for (const name of characterNames) {
    console.log(name);
  }
});
