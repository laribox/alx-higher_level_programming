#!/usr/bin/node
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < x; index++) {
    for (let index = 0; index < x; index++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
