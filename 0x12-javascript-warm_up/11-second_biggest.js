#!/usr/bin/node
const listArg = process.argv;
if (listArg[2] === undefined || listArg.length === 3) {
  console.log(0);
} else {
  const myList = listArg.slice(2);
  for (let i = 0; i < myList.length; i++) {
    myList[i] = parseInt(myList[i]);
  }
  const newList = myList.sort();
  const size = newList.length;
  const max = newList[size - 1];
  for (let j = newList.length - 1; j >= 0; j--) {
    if (newList[j] !== max || j === 0) {
      console.log(newList[j]);
      break;
    }
  }
}
