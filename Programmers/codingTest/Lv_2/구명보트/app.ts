function solution(people, limit) {
    let answer = 0
    const sortPeople = people.sort((a,b)=> b-a)

    
        for(var i=0, j=people.length-1 ; i<=j; i++) {
            
            
        if(people[i]+people[j] > limit) { answer += 1
            
        }else{
            j -= 1
            answer += 1
        }
        }
            
    return answer