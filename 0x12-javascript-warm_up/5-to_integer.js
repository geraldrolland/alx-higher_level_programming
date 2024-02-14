#!/usr/bin/node
const listArg = process.argv;
if (listArg.length === 2) {
  console.log('Not a number');
} else {
  for (let i = 2; i < listArg.length; i++) {
    const number = parseInt(listArg[i]);
    if (isNaN(number)) {
      console.log('Not a number');
    } else {
      console.log('My number: ' + number);
    }
  }
}
