#!/usr/bin/node
const callMeMoby = function (num, theFunction) {
  for (let i = 0; i < num; i++) {
    theFunction();
  }
};

module.exports = { callMeMoby };
