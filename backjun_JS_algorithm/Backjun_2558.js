let input = require('fs').readFileSync('example.txt').toString().split('\n');

let A = Number(input[0]);
let B = Number(input[1]);

console.log(A + B);
