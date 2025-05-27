const readlineSync = require('readline-sync')

let numero =  parseInt(readlineSync.question('Digite um numero: '))

if (numero % 2 !=0){
    console.log(`O numero ${numero} e impar.`)
}
else {
    console.log(`O número ${numero}e par.`)
}