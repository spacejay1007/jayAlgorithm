function solution(citations) {
    
    const sort = citations.sort((a,b) => b-a)
    
    // console.log(sort)
    let answer = 0 
    for(let i = 0; i < sort.length ; i++) {
        if(i < sort[i] ) answer++
    }
    // for(let i =0; i <citations[0])
    
    return answer;
}