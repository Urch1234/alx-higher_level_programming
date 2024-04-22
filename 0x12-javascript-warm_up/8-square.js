#!/usr/bin/node


const x = parseInt(process.argv[2]);
if (!x) {
  console.log('Missing size');
} else {
  for (let I = 0; I < x; I++) {
    console.log('X'.repeat(x));
  }
}
