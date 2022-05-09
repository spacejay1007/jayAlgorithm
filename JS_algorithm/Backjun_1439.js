const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().trim().split('\n');

let setNumber = 0,
  answer_cnt1 = 0,
  answer_cnt2 = 0;

for (let i = 0; i < input.length; i++) {
  if (setNumber !== parseInt(input[i])) {
    if (i === 0) {
      answer_cnt1++;
    } else {
      if (input[i] !== input[i - 1]) {
        answer_cnt1++;
      }
    }
  }
}

setNumber = 1;
for (let i = 0; i < input.length; i++) {
  if (setNumber !== parseInt(input[i])) {
    if (i === 0) {
      answer_cnt2++;
    } else {
      if (input[i] !== input[i - 1]) {
        answer_cnt2++;
      }
    }
  }
}

console.log(Math.min(answer_cnt1, answer_cnt2));
