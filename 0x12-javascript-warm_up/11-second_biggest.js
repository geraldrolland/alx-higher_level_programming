#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] === undefined || listArg.length === 3) {
  console.log(0);
} else {
  const myList = listArg.slice(2);
  for (let i = 0; i < myList.length; i++) {
    myList[i] = parseInt(myList[i]);
  }
  const newList = myList.sort((a, b) => a - b);
  const max = newList[newList.length - 1];
  for (let j = newList.length - 1; j >= 0; j--) {
    if (newList[j] !== max) {
      console.log(newList[j]);
      break;
    }
    if (j === 0) {
      console.log(newList[j]);
    }
  }
}
