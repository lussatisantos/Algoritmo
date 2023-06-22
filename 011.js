let fact = 5
let f = 1
let i = fact

do {
    f = f * i
    i--
} while (i > 1)

console.log(`O valor do factorial de ${fact} e igual a ${f}`)