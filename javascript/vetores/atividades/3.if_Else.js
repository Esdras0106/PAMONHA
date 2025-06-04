const numeros = [1, 2, 3, 4, 5, 6]

let quantidade_p = 0;
let quantidade_i = 0;

for (let i = 0; i < numeros.length; i++ )
if (numeros[i] %2 === 0){
    quantidade_p ++;
}
else{
    quantidade_i ++;
}

console.log(`Pares: ${quantidade_p}`)
console.log(`Impares: ${quantidade_i}`)




