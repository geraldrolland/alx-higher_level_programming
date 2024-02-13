#!/usr/bin/node
let i = 0;
const list = require('./100-data.js').list;
const newList = list.map((arg) => { return arg * (i++); });
console.log(list);
console.log(newList);
i = 0;
