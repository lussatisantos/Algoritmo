console.log ('---------------------')
console.log('Crianca esperanca')
 console.log('---------------------')

 console.log('Obrigado por ajudar')

 console.log ('[1] para doar $10')
 console.log('[2] para doar $25')
 console.log('[3] para doar $50')
console.log('[4] para doar outros valores')
console.log('[5] para cancelar')

let valores = ''

switch (valores) {
    case 0:
        valores = 10
        break
    case 1:
        valores = 25
        break
    case 2:
        valores = 50
        break
    case 3:
        valores = prompt('digite um valor: ')
        break
    case 4:
        valores = 'Doacao cancelada'
        break
}

console.log(`A sua doacao foi de ${valores}$`)
console.log('MUITO Obrigado')