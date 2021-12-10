// let input = require('fs').readFileSync('/dev/stdin');
var fs = require('fs');
var input = fs.readFileSync('./example.txt').toString().split('\n');
// console.log(input);

let num = Number(input[0]);
let count = 0;

while (true) {
  if (num % 5 === 0) {
    console.log(parseInt(input / 5) + count);
    break;
  }

  if (0 > num) {
    console.log(-1);
    break;
  }

  count++;
  num -= 3;
}
