const fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');

const N = Number(input);
let answer = '';

const dfs = (n) => {
  if (n === 0) {
    return;
  } else {
    dfs(parseInt(n / 2));
    answer += String(n % 2);
  }
};

dfs(N);
console.log(answer);
// console.log(parseInt(1 / 2));
// console.log(1 % 2);
