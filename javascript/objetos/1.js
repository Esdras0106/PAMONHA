const usuarios = [
    {nome: 'Ana', idade: 25},
    {nome: 'Marta', idade: 32},
    {nome: 'Maria', idade: 45}
]

console.log('\tExibindo todos os elementos do vetor.')
usuarios.forEach(usuario => {
    console.log(`\n${usuario.nome} tem ${usuario.idade} anos de idade.`)
})

console.log('\nFiltrando usuários.')
const menor_que_trinta = usuarios.filter(usuario => usuario.idade < 30)
menor_que_trinta.forEach(usuario => console.log(`${usuario.nome} tem menos de 30 anos.`))

console.log('\nExibindo apenas um nome dos usuários.')
const nomes = usuarios.map(usuario => usuario.nome)
nomes.forEach( nome => {
    console.log(`Nome ${nome}`)
})

console.log('\nExibindo o nome dos funcionários com numeração')
nomes.forEach( (nome, index) =>{
    console.log(`${++index}: ${nome}`)
})

console.log('\nEncontrar um usuario na lista.')
const usuario_encontrado = usuarios.find(usuario => usuario.nome === 'Marta')
console.log(`Nome ${usuario_encontrado.nome}, idade: ${usuario_encontrado.idade}`)



console.log('\nMostrar a soma de todas as idades')
const somalidades = usuarios.reduce ((total,usuario) => total + usuario.idade, 0)
console.log(`Total> ${somalidades}`)