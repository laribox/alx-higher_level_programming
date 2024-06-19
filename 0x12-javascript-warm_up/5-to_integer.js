#!/usr/bin/node
const number = Number(process.argv[2]);
console.log(isNaN(number) ? 'Not a number' : `My number: ${number}`);
