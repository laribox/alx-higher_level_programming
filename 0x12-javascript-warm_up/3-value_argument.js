#!/usr/bin/node
const firstAgr = process.argv[2];

if (firstAgr === undefined) {
  console.log('No argument');
} else {
  console.log(firstAgr);
}
