function solution(absolutes, signs) {
  // var answer = 123456789;
  let stack = [];
  for (let i = 0; i < absolutes.length; i++) {
    if (signs[i] === false) {
      stack.push(absolutes[i] * -1);
    }
    if (signs[i] === true) {
      stack.push(absolutes[i]);
    }
  }

  let count = 0;
  for (let j = 0; j < stack.length; j++) {
    count += Number(stack[j]);
  }
  return count;
  // return answer;
}
