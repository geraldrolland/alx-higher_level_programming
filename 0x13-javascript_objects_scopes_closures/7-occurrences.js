#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let freq = 0;
  const listSize = list.length;
  for (let i = 0; i <= listSize; i++) {
    if (list[i] === searchElement) {
      freq++;
    }
  }
  return freq;
};
