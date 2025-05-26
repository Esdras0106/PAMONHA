// npm install readline-sync

const readline = require('readline-sync')

soma = 0 
let nota = 0 

for (let i=1; i <= 2; i++) {
    do { 
        nota = readline.questionFloat('Digite uma nota: ')
    }while( nota < 0 || nota > 10)
        soma += nota
    }
    
media = soma / 2 
console.log (`Média: ${media}`)
// print(f"Média: {media}")  P Y T H O N
// console.log(f"Média: ${media}") J A V A - S C R I P T
// System.out.printin("Média: " + media ) J A V A 