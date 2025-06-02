const readlineSync = require('readline-sync')

let a = parseInt(readlineSync.question('Digite o valor de A: '))
let b = parseInt(readlineSync.question('Digite o valor de B: '))
let c = parseInt(readlineSync.question('Digite o valor de C: '))

let soma = (a + b)

if (soma > c) {
    console.log(`O número ${soma} é maior que C.`)
}
else if (soma === c) {
    console.log(`O número ${soma} é igual a C.`)
}
else {
    console.log(`O número ${soma} é menor que C.`)
}
