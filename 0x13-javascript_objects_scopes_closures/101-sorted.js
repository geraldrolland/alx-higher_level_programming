#!/usr/bin/node
const myDict = require('./101-data.js').dict;

function newDict (dict) {
  const newDict = {};
  let list = [];
  for (const key in dict) {
    for (const myKey in dict) {
      if (dict[key] === dict[myKey]) {
        const elem = '' + myKey;
        list.push(elem);
      }
    }
    const name = dict[key] + '';
    newDict[name] = list;
    list = [];
  }
  console.log(newDict);
}
newDict(myDict);
