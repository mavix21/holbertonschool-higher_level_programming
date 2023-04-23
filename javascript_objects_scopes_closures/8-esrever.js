#!/usr/bin/node

const esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
};

module.exports.esrever = esrever;
