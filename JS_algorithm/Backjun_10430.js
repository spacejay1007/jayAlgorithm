let input = require('fs').readFileSync('example.txt').toString().split(' ');

let A = Number(input[0]);
let B = Number(input[1]);
let C = Number(input[2]);

console.log((A + B) % C);
console.log(((A % C) + (B % C)) % C);
console.log((A * B) % C);
console.log(((A % C) * (B % C)) % C);
