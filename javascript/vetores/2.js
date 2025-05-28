// Criando uma lista.
const numeros = [1, 2, 3, 4, 5]

console.log('Exibindo elementos da lista.')
console.log(numeros)

console.log('Multiplicação com elementos da lista.')
const dobrados = numeros.map(n => n * 2)
console.log(dobrados)


console.log('Filtrando elementos da lista.')
const pares  = numeros.filter(n => n %2 === 0 )
console.log(pares)


console.log('Somando todos os elementos da lista.')
const soma = numeros.reduce((soma, atual) => soma + atual, 0)
console.log(soma)


console.log('Subtraindo todos os elementos da lista.')
const total = numeros.reduce((soma, atual) => soma - atual)
console.log(total)

