// JavaScript :- Funtion

// Normal Function Use:-
function oneplus(x,y){
    console.log("Done")
    return 1 + (x+y)/2
}
let a=1, b=2, c=3;
console.log("One Plus",a,"and",b,"is", oneplus(a,b))
console.log("One Plus",b,"and",c,"is", oneplus(b,c))
console.log("One Plus",a,"and",c,"is", oneplus(a,c))

// Arrow Function Use:- (important)
const hello=()=>{
    console.log("Hey how are you?")
    return "hi"
}
let v = hello();
console.log(v)

const sum=(a,b)=>{
    console.log("Hey how are you?")
    return a+b
}
a = 10, b = 20;
console.log(sum(a,b))


