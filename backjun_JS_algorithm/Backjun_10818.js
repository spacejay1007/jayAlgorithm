let input = require('fs').readFileSync('example.txt').toString().split('\n');

const A = input[0].split(' ').map(Number);
const B = input[1].split(' ').map(Number);

// const minMax = [];
// for (i = 0; i < A; i++) {
//   //   console.log(B[i]);
//   console.log(Math.max.apply(null, B[i]));
// }

// console.log(B.sort());

// var max = B.reduce(function (previous, current) {
//   return previous > current ? previous : current;
// });
// var min = B.reduce(function (previous, current) {
//   return previous < current ? previous : current;
// });
// // console.log(min);
// // console.log(max);

// console.log(min, max);

B.sort((a, b) => a - b);

console.log(B[0], B[A - 1]);
