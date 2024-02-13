#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((arg) => { return list.indexOf(arg) * arg; });
console.log(list);
console.log(newList);
