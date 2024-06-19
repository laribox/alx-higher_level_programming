#!/usr/bin/node
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
  return;
}

for (let index = 0; index < x; index++) {
  console.log('C is fun');  
}
