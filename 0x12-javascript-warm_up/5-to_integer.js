#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Not a number');
} else {
  if (isNaN(parseInt(process.argv[2]))) {
    console.log('Not a number');
  } else {
    console.log(parseInt(process.argv[2]));
  }
}
