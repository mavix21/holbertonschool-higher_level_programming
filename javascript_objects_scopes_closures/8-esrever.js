#!/usr/bin/node

const esrever = (list) => {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  // Or:
  // list.forEach(element => {
  //   reversedList.unshift(element)
  // });

  return (reversedList);
};

module.exports = { esrever };
