#!/usr/bin/node
let big1 = -Infinity;
let big2 = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const num = Number(process.argv[i]);

  if (num > big1) {
    big2 = big1;
    big1 = num;
  } else if (num > big2 && num !== big1) {
    big2 = num;
  }
}

if (big2 === -Infinity) {
  console.log(0);
} else {
  console.log(big2);
}
