function vowelsAndConsonants(s) {
    let vowel = ['a','e','i','o','u'];
    let ans = [];
    
    for (let x of s){
        if (vowel.includes(x)){
            ans.push(x)
        }
    }
    
    for (let x of ans){
        console.log(x)
    }
    
    for (let x of s){
        if (!vowel.includes(x)){
            console.log(x)
        }
    }
    
}
