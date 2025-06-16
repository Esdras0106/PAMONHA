function calcularMedia() {
        
        let n1 = Number(document.getElementById("nota1").value);
        let n2 = Number(document.getElementById("nota2").value);
        let n3 = Number(document.getElementById("nota3").value);
        let n4 = Number(document.getElementById("nota4").value);
      
        if (n1 === 0 || n1 <0){
                alert(`A nota ${n1} é inválida.`)
        }
    
        else if (n2 === 0 || n2 <0){
                alert(`A nota ${n1} é inválida.`)
        }
    
        else if (n2 === 0 || n2 <0){
                alert(`A nota ${n1} é inválida.`)
        }
    
        else if (n2 === 0 || n2 <0){
                alert(`A nota ${n1} é inválida.`)
        }

        let media = (n1 + n2 + n3 + n4) / 4;
        
        if (media >= 7){
                alert(`\nSITUAÇÂO: APROVADO`)
        }
        
        else if (media <4){
                alert(`\nSITUAÇÂO: REPROVADO`)
        }
        else{
                alert(`\nSITUAÇÂO: RECUPERAÇÂO`)
         
        document.getElementById("resultadoMedia").textContent = "Média: " + media.toFixed(2);
    }      
}
