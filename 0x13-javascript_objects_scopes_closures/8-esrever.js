#!/usr/bin/node
exports.esrever = function (list) {
  let listSize = list.length;
  const myList = [];
  listSize--;
  for (let i = listSize; i >= 0; i--) {
    myList.push(list[i]);
  }
  return myList;
};
