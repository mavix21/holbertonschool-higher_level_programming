#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

if (!id) {
  console.log('Please specify an id');
  process.exit(1);
}

const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const title = JSON.parse(body).title;
  console.log(title);
});
