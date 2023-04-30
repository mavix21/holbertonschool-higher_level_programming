#!/usr/bin/node
const axios = require('axios').default;

const url = process.argv[2];
if (!url) {
  console.log('Please, provide an url');
  process.exit(1);
}

axios.get(url)
  .then(({ data: { results } }) => {
    let count = 0;
    results.forEach(({ characters }) => {
      characters.forEach((url) => {
        if (url.includes('18')) count++;
      });
    });
    console.log(count);
  })
  .catch(err => console.error(err));
