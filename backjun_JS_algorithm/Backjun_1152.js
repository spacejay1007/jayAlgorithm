const fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');

// let count = 0;
// for (let i = 0; i < input.length; i++) {
//   if (input[i] === '') {
//     return 0;
//   }
//   count += 1;
// }

// console.log(count);
// if(input)
// console.log(input.length);

// let count = input.length;

// if (input === '') count -= 1;
// if (input[input.length - 1] === '') count -= 1;

// // console.log(input);
// console.log(count);

// let input = fs.readFileSync(filePath).toString().split("\n");

input = input[0].split(' ');
let result = input.length;

if (input[0] === '') result -= 1;
if (input[input.length - 1] === '') result -= 1;

console.log(result);
