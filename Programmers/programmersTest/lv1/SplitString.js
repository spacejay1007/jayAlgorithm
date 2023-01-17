// programmers > 문자열 나누기

const t = "banana";
const x = "abracadabra";
const y = "aaabbaccccabba";

const SplitSting = (t) => {
  // let same = 0;
  // let def = 0;
  // const arr = [];
  // let firstText = t[0];

  // [...t].map((item, idx) => {
  //   // console.log(item);

  //   if (firstText === item) same++;
  //   else {
  //     def++;
  //   }

  //   if (same === def) {
  //     console.log(item);
  //     t.substr();
  //   }
  // });

  // console.log(same, def);
  let arr = [];
  let x = 0;
  let y = 0;

  while (t.length > 0) {
    let count = 0;
    for (let i = 0; i < t.length; i++) {
      t[0] === t[i] ? (x += 1) : (y += 1);
      if (x === y) {
        count = i + 1;
        break;
      }
    }
    console.log(t.slice(0, count));
    arr.push(t.slice(0, count));
    t = t.slice(count);
    if (count === 0) break;
  }
  console.log(arr);

  //
  // let isX = [t[0], 0];
  // let isNotX = "";
  // const result = [];
  // for (let i = 0; i < t.length; i++) {
  //   if (isX[0] === t[i]) isX[1]++;
  //   // console.log(isX[1]++);
  //   else isNotX += t[i];
  //   console.log(t[i], isNotX, isX[1], isNotX.length);
  //   // console.log(isX[1]++);
  //   if (isX[1] === isNotX.length) {
  //     result.push(isX[0] + isNotX);
  //     isX = [t[i + 1], 0];
  //     isNotX = "";
  //   }
  // }
  // if (isX[0]) result.push(isX[0]);
  //
  // console.log(result);
};

SplitSting(t);
// SplitSting(x);
// SplitSting(y);
