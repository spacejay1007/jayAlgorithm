const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

const A = Number(input[0]);
const arr = new Array(A + 1);

for (let i = 1; i - 1 < A; i++) {
  //   console.log(input[i]);
  arr[i] = input[i].split(' ').map(Number);
}

arr.sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]));

let cur = arr[0][1];
let ans = 1;
for (let i = 1; i < A; i++) {
  if (arr[i][0] >= cur) {
    cur = arr[i][1];
    ans++;
  }
}
console.log(ans);
// console.log(cur);
