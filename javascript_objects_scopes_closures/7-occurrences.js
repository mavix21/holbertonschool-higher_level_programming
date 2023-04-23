#!/usr/bin/node

const nbOccurences = function (list, searchElement) {
  let numberOfOcurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numberOfOcurrences++;
    }
  }

  return (numberOfOcurrences);
};

module.exports.nbOccurences = nbOccurences;
