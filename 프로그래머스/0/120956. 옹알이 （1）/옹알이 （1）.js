function solution(babbling) {
    let answer = 0
    const possible = ["aya", "ye", "woo", "ma"]
    
    for (const word of babbling) {
        let currentword = word
        for (const sound of possible) {
            currentword = currentword.replace(sound," ")
        }
        if (currentword.trim() === "") {
            answer++
        }
    }
    
    return answer
}