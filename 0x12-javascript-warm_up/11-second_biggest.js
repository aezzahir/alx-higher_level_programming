#!/usr/bin/node
let big1 = 0; let big2 = 0;
let i = 0;
while (i < process.argv.length - 1) {
  if (process.argv[i + 1] > process.argv[i]) {
    big2 = big1;
    big1 = Number(process.argv[i + 1]);
  } else {
    big2 = big1;
    big1 = Number(process.argv[i]);
  }
  i++;
}
console.log(big2);
