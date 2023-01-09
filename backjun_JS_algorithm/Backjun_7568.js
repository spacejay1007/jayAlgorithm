const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const N = Number(input[0]);
input.shift();

let stack = [];
for (let i = 0; i < N; i++) {
  let body = input[i].split(' ').map(Number);
  stack.push(body);
}

let result = [];
for (let j = 0; j < N; j++) {
  let count = 0;
  for (let k = 0; k < N; k++) {
    if (stack[j][0] < stack[k][0] && stack[j][1] < stack[k][1]) {
      count++;
    }
  }
  result.push(count + 1);
}

console.log(result.join(' '));
