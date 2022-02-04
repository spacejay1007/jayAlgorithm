const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

// const N = Number(input);

// const X = [];
// for (let i = 1; i < N + 1; i++) {
//   if (N === 0) {
//     return 1;
//   }

//   X.push(i);
// }
// const XX = X.reduce((a, b) => a * b);

// console.log(XX);

const N = Number(input[0]);

function f(n) {
  if (n === 0) {
    return 1;
  }
  return n * f(n - 1);
}
console.log(f(N));
