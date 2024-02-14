#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] !== undefined) {
  console.log(listArg[2]);
} else {
  console.log('No argument');
}
