function solution(brown, yellow) {
    let sum = (brown / 2) + 2;  // 가로, 세로의 합
   
    for (let i = sum-1; i >= sum/2; i--) {
      let row = i;
      let column = sum-i;
      if (yellow === (row - 2)*(column - 2)) return [row, column];
    }
  }


  function solution(brown, red) {
    // let answer = [];
    for (let i = 3; i <= (brown+red)/i; i++) {
        /** Math.floor === 무조건 내림  */
        let x = Math.floor((brown+red)/i);
        if( (x-2)*(i-2)=== red) {
            break;
        }
    }
 
    return [x,i];  // 가로 x, 세로 i
}