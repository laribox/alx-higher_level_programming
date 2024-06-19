#!/usr/bin/node
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  let result = 1;
  for (let i = n; i > 1; i--) {
    result *= i;
  }
  return result;
}

console.log(factorial(Number(process.argv[2])));
