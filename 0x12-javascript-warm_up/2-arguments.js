#!/usr/bin/node
if (process.argv.length - 1 === 1) {
  console.log('No argument');
}
if (process.argv.length - 1 === 2) {
  console.log('Argument found');
}
if (process.argv.length - 1 > 2) {
  console.log('Arguments found');
}
