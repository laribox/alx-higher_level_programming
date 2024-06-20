#!/usr/bin/node

const dict = require('./101-data').dict;
let result = {};

for (let userId in dict) {
  let occurrence = dict[userId];
  
  if (!result[occurrence]) {
    result[occurrence] = [];
  }

  result[occurrence].push(userId);
}

