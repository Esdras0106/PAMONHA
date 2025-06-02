const readlineSync = require('readline-sync')

const dia = parseInt(readlineSync.question('Escolha um dia entre 1 - 7: '))

switch (dia){
    case 1:
        console.log(`Dia ${dia} é um domingo.`)
        break
    case 2:
        console.log(`Dia ${dia} é uma segunda.`)
        break
    case 3:
        console.log(`Dia ${dia} é uma terça.`)
        break
    case 4:
        console.log(`Dia ${dia} é uma quarta.`)
        break
    case 5:
        console.log(`Dia ${dia} é uma quinta.`)
        break
    case 6:
        console.log(`Dia ${dia} é uma sexta.`)
        break
    case 7:
        console.log(`Dia ${dia} é um sábado.`)
        break
    default:
        console.log('Dia inválido.')
}


