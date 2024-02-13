#!/usr/bin/node
let listSize = 0;
exports.logMe = function (item) {
  console.log(listSize + ': ' + item);
  listSize++;
};
