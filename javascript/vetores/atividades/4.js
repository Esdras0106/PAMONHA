const readline = require('readline-sync')

const list_numeros = []
let quantidade_negativos = 0;
let quantidade_positivos = 0;
let soma = 0;

for (let i = 1; i < 5; i++){
    const numeros = readline.questionFloat(`Digite o ${i}º numero: `)
    list_numeros.push(numeros)
    
    if (numeros < 0){
        quantidade_negativos ++
    }
    else if (numeros >0){
        quantidade_positivos++
        soma += numeros
    }
}

console.log(`\nQuantidade de Negativos: ${quantidade_negativos}`)
console.log(`Soma dos Positivos: ${soma}`)
