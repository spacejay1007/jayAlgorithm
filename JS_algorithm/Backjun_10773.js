const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

// console.log(input);
const K = Number(input[0]); // 정수 K 횟수
const M = [];

for (let i = 1; i < K + 1; i++) {
  if (Number(input[i]) !== 0) {
    M.push(Number(input[i]));
  } else {
    M.pop();
  }
}
// const sum = M.reduce((a, b) => a + b);
let sum = 0;
for (let j = 0; j < M.length; j++) {
  sum += M[j];
}
console.log(sum);
