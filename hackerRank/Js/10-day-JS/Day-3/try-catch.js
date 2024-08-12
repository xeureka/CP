function reverseString(s) {
    try{
        let revS = s.split('').reverse().join('');
        
        console.log(revS);
    }catch(err){
        console.log(err.message);
        console.log(s);
    }
    
}