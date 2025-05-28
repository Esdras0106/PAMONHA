const readlineSync = require('readline-sync')

let valor1 = parseInt(readlineSync.question('Digite o primeiro valor: '))
let b = parseInt(readlineSync.question('Digite o segundo valor: '))

let soma;

if (valor1 === b) {
    soma = valor1 + b;
} else {
    soma = valor1 * b;
}

console.log(`Resultado: ${soma}`)
