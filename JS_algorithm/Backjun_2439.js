let input = require('fs').readFileSync('example.txt').toString();

for (let i = 1; i < Number(input) + 1; i++) {
  //   console.log(i);
  console.log(' ' * (n - i) + '*' * i);
}
