// Criando um Vetor.
const listaDenumeros = [1, 2, 3, 4]

console.log('Listando todos os numeros da lista.')
console.log(listaDenumeros)

console.log('\nMultipicando vetores por 2: ')
const dobrados = listaDenumeros.map(n => n * 2)
console.log(dobrados)

console.log('\nSomando todos os numeros da lista: ')
const pares = listaDenumeros.filter(n => n % 2 ===0)
console.log(pares)

console.log('\nSomando todos os numeros da lista: ')
const soma = listaDenumeros.reduce((soma , total) => soma + total , 0)
console.log(soma)

