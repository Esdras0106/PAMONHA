const readlineSync = require ('readline-sync')

function media(a,b){    
    return (a + b ) / 2 
}

const a = (parseFloat(readlineSync.question('Digite um numero: ')))
const b = (parseFloat(readlineSync.question('Digite um outro numero: ')))
let mediar = media(a,b);

console.log(`Média: ${mediar}`)