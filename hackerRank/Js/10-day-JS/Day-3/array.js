function getSecondLargest(nums) {
    // Complete the function
    let firstMax = Math.max(...nums);
let sortNums = nums.sort((a,b) => a - b)

let another = [];

 

for (let x of sortNums){
    if (x != undefined && x != firstMax){
        another.push(x)
    }
}



return Math.max(...another);
}