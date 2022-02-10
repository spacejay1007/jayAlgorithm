const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const N = Number(input[0]);
let km = input[1].split(' ').map(Number);
let liter = input[2].split(' ').map(Number);

let count = 0;
let L = liter[0];

for (let i = 0; i < km.length; i++) {
  if (L >= liter[i]) {
    L = liter[i];
  }
  count += L * km[i];
}
console.log(count);
