const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().trim().split('\n');

// const N = Number(input[0]);
input.shift(input[0]);
const arr = input.sort((a, b) => a.length - b.length || a.localeCompare(b));
const R = new Set(arr);

console.log([...R].join('\n'));

// console.log(arr.join('\n'));

// for (let i = 1; i <= N; i++) {
//   //   console.log(i);
//   //   stack.push(input[i]);
//   let A = input[i].length;

//   //   console.log(input[i].length);

//   console.log(A);
// }
// console.log(input[1]);
// console.log(stack.length);
