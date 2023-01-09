const input = require('fs').readFileSync('example.txt').toString().split('\n');

// console.log(input);
const A = input[0].split(' ').map(Number);

const list = [];
list.sort((a, b) => a - b);

for (let i = 1; i - 1 < A; i++) {
  list.push(Number(input[i]));
}

const count = 0;
const countList = 0;
for (let j = 0; j < list.length; j++) {
  count = countList + list[j];
}
