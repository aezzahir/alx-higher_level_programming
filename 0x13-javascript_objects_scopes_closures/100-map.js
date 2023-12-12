#!/usr/bin/node
const list = require('./100-data').list;
const maped = list.map((x) => x * (x - 1));
console.log(list);
console.log(maped);
