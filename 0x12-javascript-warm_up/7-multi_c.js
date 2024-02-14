#!/usr/bin/node
const listArg = process.argv;
if (listArg.length === 2 || isNaN(parseInt(listArg[2])) === true) {
  console.log('Missing number of occurrences');
} else {
  const number = parseInt(listArg[2]);
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
