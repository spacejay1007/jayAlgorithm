let input = require("fs").readFileSync("example.txt").toString().split("\n");

const A = input[0].split(" ").map(Number);
const B = input[1].split(" ").map(Number);
// console.log(A[1]);
// console.log(B);
const C = [];
for (let i = 0; i < A[0]; i++) {
  if (A[1] > B[i]) {
    C.push(B[i]);
  }
}
console.log(C.join(" "));
// console.log(A);
// for (i = 0; i <= input.length; i++) {}
