const readlineSync = require ('readline-sync')

function somar(a, b){
    if (a === b){
        return a + b
    }
    else {
        return a * b
    }
}

let a = parseInt(readlineSync.question("Digite um numero: "))
let b = parseInt(readlineSync.question("Digite um numero: "))

const c = somar(a,b)
console.log(`Resultado: ${c}`)