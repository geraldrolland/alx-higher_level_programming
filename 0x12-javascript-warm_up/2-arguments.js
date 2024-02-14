#!/usr/bin/node
const listArg = process.argv;
if (listArg.length === 2) {
  console.log('No argument');
} else if (listArg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
