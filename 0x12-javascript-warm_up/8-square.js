#!/usr/bin/node
const x = Number(process.argv[2]);
if (!x) {
  console.log('Missing size');
} else {
  for (let j = 0; j < x; j++) {
    for (let i = 0; i < x; i++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}
