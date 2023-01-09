const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const A = Number(input[0]);

function () {
if (A <= 90) {
  return A;
} else if (A < 80) {
  return B;
}
}
console.log