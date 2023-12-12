#!/usr/bin/node
const x = Number(process.argv[2]);
function factorial (n) {
  if (!n) {
    return (1);
  }
  return (n * factorial(n - 1));
}
console.log(factorial(x));
