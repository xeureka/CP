


function main() {
    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
    }
}


function getMaxLessThanK(n,k){
    let maximValue = 0;

    for (let i = 1; i<n;i++){
        for (let j = i + 1;j <= n;j++){
            let andValue = i & j;
            if (andValue < k && maximValue <andValue){
                maximValue = andValue
            }
        }
    }

    return maximValue;
}
