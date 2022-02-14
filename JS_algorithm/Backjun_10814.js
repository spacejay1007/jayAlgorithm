const fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');

// input.shift();
// input.sort((a, b) => a.split(' ')[0] - b.split(' ')[0]);

// console.log(input.join('\n'));

const N = +input.shift();
const arr = [];

for (let i = 0; i < N; i++) {
  arr.push(input[i].trim().split(' '));
}

arr.sort((a, b) => a[0] - b[0]);

for (result of arr) {
  console.log(result.join(' '));
}
