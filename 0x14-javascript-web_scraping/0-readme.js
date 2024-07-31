#!/usr/bin/node
const filename = process.argv[2];
const fs = require('fs');
fs.readFile(filename, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
