#!/usr/bin/node
// const myVar = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
