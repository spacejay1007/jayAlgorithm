function solution(s) {
    const split = s.split(" ")
   const max = Math.max(...split)
   const min = Math.min(...split)
   
   return min+" " + max
}