let fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n');

let N = Number(input[0]);
let P = input[1].split(' ').map(Number);
const sortTime = P.sort((a, b) => a - b);

const timeArr = [];
let time = 0;
let timeBefore = 0;
for (let i = 0; i < N; i++) {
  //   time = +sortTime[i];
  // time.push(sortTime[i] + sortTime[i + 1]);
  //   console.log(sortTime[i]);
  time += timeBefore + sortTime[i];
  timeBefore += sortTime[i];
}
console.log(time);
// console.log(sortTime);
