const ano = new Date ()
const ano_actual = ano.getFullYear()
let ano_nasc = 2000

let idade = ano_actual - ano_nasc

if (idade < 12) {
    console.log('Voce seras uma crianca')
} else if (idade > 12 && idade < 17 ) {
    console.log ('Voce seras um adolescente')
} else if (idade > 17 && idade < 35) {
    console.log('Voce seras jovem')
} else if (idade > 35 && idade < 60){
    console.log('Voce seras adulto')
} else if (idade > 60) {
    console.log('Voce seras idoso')
}