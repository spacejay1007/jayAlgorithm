let input = require('fs').readFileSync('example.txt').toString();

let A = Number(input);
for (i = 1; i <= 9; i++) {
  console.log(`${A} * ${i} = ${A * i}`);
}

// console.log(A * 1);
// console.log(A * 2);
// console.log(A * 3);
// console.log(A * 4);
// console.log(A * 5);
// console.log(A * 6);
// console.log(A * 7);
// console.log(A * 8);
// console.log(A * 9);
