// let input = require('fs').readFileSync('example.txt').toString();
// // .split('\n');

// // console.log(input);
// var a = parseInt(input[0]);
// var b = parseInt(input[1]);

// console.log(a / b);
// // console.log(a + b);

// // console.log('helloWorld');

// for (let i = 0; i < )
// console.log(input);
let input = Number(require('fs').readFileSync('example.txt').toString());

let print = '';

for (let i = 1; i <= input; i++) {
  print += i + '\n';
}

console.log(print);
