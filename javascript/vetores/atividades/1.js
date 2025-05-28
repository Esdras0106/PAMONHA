const readlineSync = require ('readline-sync')

let idade;
idade = parseInt(readlineSync.question('Digite sua idade: '))
 
if (idade <16 ) {
   console.log('Você ainda não pode votar.')
}

else if (idade === 16 || idade === 17 ) {
    console.log('Voto opcional.')
}

else if (idade >= 65 ) {
    console.log('Você não é obrigado a votar.')
}

else {
    console.log('Voto obrigatório.')
};