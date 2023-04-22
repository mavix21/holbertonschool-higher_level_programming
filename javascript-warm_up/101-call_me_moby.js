#!/usr/bin/node

module.exports.callMeMoby = function (x, theFunction) {
  // No need to execute if x is 0 or negative
  if (x <= 0) {
    return;
  }

  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
