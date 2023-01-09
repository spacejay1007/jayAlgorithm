const fs = require("fs");
let input = fs
  .readFileSync("./backjun_JS_algorithm/2720_donghuk/donghuk.txt")
  .toString()
  .split("\n");

const repeatCnt = input[0];
input.shift();
// console.log(repeatCnt);

for (let i = 0; i < repeatCnt; i++) {
  const arr = [];
  let number = input[i];

  arr.push(parseInt(number / 25));
  number = parseInt(number % 25);

  arr.push(parseInt(number / 10));
  number = parseInt(number % 10);

  arr.push(parseInt(number / 5));
  number = parseInt(number % 5);

  arr.push(parseInt(number / 1));
  number = parseInt(number % 1);

  console.log(arr.join(","));
}
