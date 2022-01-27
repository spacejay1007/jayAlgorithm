const fs = require('fs');
let input = fs.readFileSync('example.txt').toString().split('\n').map(Number);

const T = input[0];
input.shift();
let k; // 층수
let n; // 호수
let arr = [];

for (let i = 0; i < T * 2; i = i + 2) {
  k = Number(input[i]);
  n = Number(input[i + 1]);
  arr.push([k, n]);
}

const sum = [];
let people;

for (let i = 0; i < T; i++) {
  if (arr[i][0] >= 2) {
    people = arr[i][1] * (arr[i][0] + 1) + arr[i][0];
  } else {
    people = arr[i][1] * (arr[i][0] + 1);
  }

  sum.push(people);
}

console.log(sum);

for (let j = 0; j < arr[i][1]; j++) {}
