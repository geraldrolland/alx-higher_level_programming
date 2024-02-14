#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] === undefined || isNaN(parseInt(listArg[2])) === true) {
  console.log('Missing size');
} else {
  const size = parseInt(listArg[2]);
  const myVar = 'X';
  for (let i = 0; i < size; i++) {
    console.log(myVar.repeat(size));
  }
}
