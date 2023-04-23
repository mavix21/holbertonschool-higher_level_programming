#!/usr/bin/node

const nbOccurences = (list, searchElement) => {
  let numberOfOcurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numberOfOcurrences++;
    }
  }

  return (numberOfOcurrences);
};

// Another way:
// const nbOccurences = (list, searchElement) => list.filter((element) => {
//   searchElement === element).length
// };

module.exports = { nbOccurences };
