#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} if (process.argv.length > 2 && parseInt(process.argv[2]) > 0) {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
