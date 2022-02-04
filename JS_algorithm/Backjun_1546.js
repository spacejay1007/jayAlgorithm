const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const M = Number(input[0]);
const score = input[1].split(' ').map(Number);

const Max = score.sort((a, b) => a - b)[M - 1];

let sum = 0;

for (let i = 0; i < M; i++) {
  const newNum = (score[i] / Max) * 100;
  sum += newNum;
}

console.log(sum / M);
