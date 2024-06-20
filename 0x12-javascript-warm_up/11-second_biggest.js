#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
