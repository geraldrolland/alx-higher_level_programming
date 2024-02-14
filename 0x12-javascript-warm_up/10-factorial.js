#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] === undefined || isNaN(parseInt(listArg[2])) === true) {
  console.log(1);
} else {
  console.log(factorial(parseInt(listArg[2])));
}
function factorial (num) {
  if (num === 1) {
    return 1;
  }
  num *= factorial(num - 1);
  return num;
}
