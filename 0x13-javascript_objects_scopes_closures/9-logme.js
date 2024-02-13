#!/usr/bin/node
let listSize = 0;
exports.logMe = function (item) {
  listSize++;
  console.log(listSize + ': ' + item);
};
