const fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');

let I = input[0];
let alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='];
// let count = 0;
// for (let i = 0; i < alphabet.length; i++) {
//   let A = alphabet[i];
//   // if()
//   console.log(input.indexOf(A, 0));
// }
// console.log(count);
for (let A of alphabet) {
  I = I.split(A).join('a');
}

console.log(I.length);
