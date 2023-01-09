const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().trim().split(' ');

// console.log(input);

const min =
  Number(input[0].replace(/6/gi, Number(5))) +
  Number(input[1].replace(/6/gi, Number(5)));
const max =
  Number(input[0].replace(/5/gi, Number(6))) +
  Number(input[1].replace(/5/gi, Number(6)));

console.log(min, max);
