#!/usr/bin/node
var i = 0
const list = require('./100-data.js').list;
let newList = list.map((arg) => {return arg * (i++)});
console.log(list);
console.log(newList);
i = 0;
