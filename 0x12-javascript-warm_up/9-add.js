#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] === undefined || listArg[3] === undefined) {
  console.log('NaN');
} else if (isNaN(parseInt(listArg[2])) === true || isNaN(parseInt(listArg[3])) === true) {
  console.log('NaN');
} else {
  console.log(parseInt(listArg[2]) + parseInt(listArg[3]));
}
