const fs = require('fs');
const input = fs.readFileSync('example.txt').toString().split('\n');

// console.log(input);
// [A, B] = input;
// console.log(A, B);
[N, ...numbers] = input;
N = Number(N);
numbers = numbers.map((i) => Number(i));
// console.log(N, numbers);

let m = new Array(90).fill(0);
m = [1, 1, 2, 2, 3, 4, 5, 7, 9, ...m];

const f = (n) => {
  if (m[n]) return m[n];
  else {
    return (m[n] = f(n - 1) + f(n - 5));
  }
};

for (let j = 0; j < N; j++) {
  console.log(f(numbers[j]));
}
