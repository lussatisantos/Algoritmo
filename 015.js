//Sequencia de fibonacci

let n1 = 0
let n2 = 1
let n3 = 0

console.log (n1)
console.log(n2)
for (let i = 0; i < 14; i++) {
    n3 = n1 + n2
    console.log(n3)
    n1 += n2
    n2 += n3
}