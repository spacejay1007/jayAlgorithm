function solution(s){
    
    let arrS = [...s]
   let left = 0; // "("을  위한 변수
   if(arrS[0] === ")") return false
   
    
   for(let i = 0; i < arrS.length; i++){
       if(arrS[i]==='('){
           left++; //"("이면 left 1 증가  
       }else if(left >= 1 && arrS[i] === ')'){
           left--; // left가 1 이상이고 arrS[i]가 ')' 이면 left 감소
       }
   }
   
   if(left === 0){
       return true; //left가 0이면 true
   }else{
       return false; // 0이 아니면 false
   }
   
   

}