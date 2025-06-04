const numeros = [1, 2, 3, 4, 5, 6]
console.log('Pares: ')
pares = numeros.filter(n => n %2 === 0)
quantidade_p = pares.length
console.log(`Possuem ${quantidade_p} pares.`)

console.log('\nImpares: ')
impares = numeros.filter(n => n %2 != 0)
quantidade_i = impares.length
console.log(`Possuem ${quantidade_i} impares.`)