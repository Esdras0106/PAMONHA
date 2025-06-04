const readline = require('readline-sync');

const lista_notas = []

for( let i = 1; i <= 3; i++){
    let nota = readline.questionFloat(`Digite a ${i}ª nota: `)
    lista_notas.push(nota)
}

console.log('\nSoma das Notas: ')
soma = lista_notas.reduce((soma, total) => soma + total, 0)
console.log(soma)

console.log('\nQuantidade de notas: ')
quantidadeDeNotas = lista_notas.length
console.log(quantidadeDeNotas)

console.log('\nMedia:')
media = soma / quantidadeDeNotas
console.log(media)

console.log('\nExibindo todas as notas: ')
lista_notas.forEach((nota, index) => console.log(`${++index}ª nota: ${nota}`))