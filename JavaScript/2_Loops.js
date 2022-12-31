// JavaScript :- If else condition, Tunary operators, Loops.

let a = 'harry'
let b = 6
console.log(a + b)          // harry6
console.log(typeof (a+b))   // string

const c = {
    'harry':true,
    'adarsh':false,
    'lovish':67,
    'rohan':undefined 
}
c['friend'] = 'subham'
c['harry'] = 45
console.log(c)              // { all boject  }
console.log(c['harry'])     // 45
console.log(c.rohan)        // undefined

// Use Google Chrome console

// If else condtions:
a = prompt("hey how are you?");
a = Number.parseFloat(a) // converting the string to a number
console.log(a)
if(a<0){
    alert("This is note a age");
}
else if(a<=9){
    alert('hey are you kids')
}
else if(a>9 || a<60){
    alert('hey are you kids')
}
else {
    alert('This is invalid age !')
}

// Tunary Operators:
console.log('You can', a<18? "not drive": "Drive")


// Intreduces Loops:-
// for Loops:-
let sum = 0;
let n = prompt("Enter the value of n");
n = Number.parseInt(n)
for(let i=0; i<n; i++){
    sum +=(i+1) 
}
console.log("Sun of first "+n+" Natureal Number is "+sum)

let item = {
    'harry':true,
    'adarsh':false,
    'lovish':67,
    'rohan':undefined
}
// for in loop:-
for (let a in item){
    console.log("items "+a+" are "+item[a])
}
// for of loop;-
for (let b of "harry"){
    console.log("harry "+b)
}

// while loops:-
n = prompt("Enter the value of n");
n = Number.parseInt(n)
let i=0
while (n>i) {
    console.log("Sun of first "+i+" Natural Number is "+n)
    i++;
}

// Do while loops:- ( at least one time run condition fail)
n = prompt("Enter the value of n");
n = Number.parseInt(n)
i=5
do{
    console.log("Sun of first "+i+" Natural Number is "+n)
    i++;
}while (n>i)



