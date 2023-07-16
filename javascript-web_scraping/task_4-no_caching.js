#!/usr/bin/node

const request = require('request');
const mainUrl = process.argv[2];

// If no URL is provided, log an error message and exit the program
if (!mainUrl) {
  console.log('Please, provide an url');
  process.exit(1);
}

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
request.get(mainUrl, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  // Parse the response body (which should be a JSON object)
  // and extract the array of film objects
  const filmObjects = JSON.parse(body).results;

  // Initialize a counter variable to keep track of the number of Wedge Antilles
  // characters we encounter
  let count = 0;

  // Initialize a cache object (a Map) to store the names of previously fetched characters
  const cache = new Map();

  // Initialize an array to store promises that will eventually resolve to character names
  const characterNamePromises = [];

  // Loop through the array of film objects
  for (const filmObj of filmObjects) {
    // For each film object, loop through the array of character URLs
    for (const url of filmObj.characters) {
      // Call the getCharacterName function to get the name of the character
      // (passing in the cache object so that we can avoid making unnecessary HTTP requests)
      characterNamePromises.push(getCharacterName(url, cache));
    }
  }

  // Wait for all of the promises to resolve (i.e., for all of the character names to be fetched)
  // and store the resulting array of character names in the "characterNames" variable
  const characterNames = await Promise.all(characterNamePromises);

  // Loop through the array of character names and count the number of occurrences of Wedge Antilles
  for (const characterName of characterNames) {
    if (characterName === 'Wedge Antilles') {
      count++;
    }
  }

  // Log the final count of Wedge Antilles characters
  console.log(count);
});
