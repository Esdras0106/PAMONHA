const readlineSync = require('readline-sync')

let numero =  parseInt(readlineSync.question('Digite um numero: '))

if (numero %2 !=0){
    console.log(`O número ${numero} é ímpar.`)
}
else {
    console.log(`O número ${numero} é par`)
}
