const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().trim().split('\n');

const N = Number(input[0]);
input.shift();
const R = input.map((item) => item);

function n(N, R) {
  const sort = R.sort((a, b) => a - b);
  const arr = [];

  for (let i = 0; i < N; i + 1) {
    arr.push(sort[i] * (N - i));
  }
  console.log(Math.max(...arr));
}

n(N, R);
