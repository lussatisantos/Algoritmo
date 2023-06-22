let l1 = 4
let l2 = 4
let l3 = 3
let eq = ((l1 == l2) && (l2 == l3))
let es = ((l1 != l2) && (l2 != l3) && (l1 != l3))
var tri = ((l1 < l2 + l3) && (l2 < l1 + l3) && (l3 < l1 + l2))

console.log(`O triangulo equilatero? ${eq}`)
console.log(`O triangulo escaleno? ${es}`)
console.log(`Pode formar um triangulo? ${tri}`)