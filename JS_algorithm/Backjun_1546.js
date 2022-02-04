const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const M = Number(input[0]);
const score = input[1].split(' ').map(Number);
// score.sort();
const Max = score.sort((a, b) => a - b)[M - 1];

let sum = 0;
// const newScore = [];
for (let i = 0; i < M; i++) {
  //   newScore.push((score[i] / score[score.length - 1]) * 100);
  const newNum = (score[i] / Max) * 100;
  console.log(newNum);
  sum += newNum;
}

// const sum = newScore.reduce((a, b) => a + b);

console.log(sum / M);

// const N = +input[0];
// const num = input[1].split(' ').map(Number);
// const numMax = num.sort((a, b) => a - b)[N - 1];
// let sum = 0;

// for (let i = 0; i < N; i++) {
//   const newNum = (num[i] / numMax) * 100;
//   sum += newNum;
// }

// console.log(sum / N);
