#!/usr/bin/node
const dict = require('./101-data').dict;

const occurrences = {};

Object.keys(dict).forEach((key) => {
  const occurrence = dict[key];
  if (occurrences[occurrence]) {
    occurrences[occurrence].push(key);
  } else {
    occurrences[occurrence] = [key];
  }
});
for (const occ in occurrences) {
  occurrences[occ].sort((a, b) => a - b);
}
console.log(occurrences);
