function solution(array, commands) {
  const answer = [];

  for (let i = 0; i < commands.length; i++) {
    let command = array.slice(commands[i][0] - 1, commands[i][1]);
    const K = commands[i][2] - 1;
    command.sort((a, b) => a - b);
    answer.push(command[K]);
  }

  return answer;
}
