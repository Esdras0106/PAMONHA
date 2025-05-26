const readline = require('readline-sync');

let numero;

do {
    numero = parseInt(readline.question("Digite um numero: "));

    if (numero <= 1) {
        parseInt(readline.question("Digite um numero: ")); 
    }
    else {
        console.log(`Você digitou o numero: ${numero}`);
        break;
    }

} while (true);