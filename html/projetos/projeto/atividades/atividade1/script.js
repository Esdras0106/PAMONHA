function calcularMedia() {
        let n1 = Number(document.getElementById("nota1").value);
        let n2 = Number(document.getElementById("nota2").value);
        let n3 = Number(document.getElementById("nota3").value);
        let n4 = Number(document.getElementById("nota4").value);
      
        // Validação
        if (n1 <= 0 || n2 <= 0 || n3 <= 0 || n4 <= 0) {
          document.getElementById("resultadoMedia").textContent = "Média: --";
          document.getElementById("situacaoAluno").textContent = "Preencha todas as notas corretamente!";
          document.getElementById("situacaoAluno").className = "situacao reprovado";
          document.getElementById("resultadoDetalhes").open = true;
          return;
        }
      
        let media = (n1 + n2 + n3 + n4) / 4;
      
        // Mostrar resultado
        document.getElementById("resultadoMedia").textContent = "Média: " + media.toFixed(2);
        document.getElementById("resultadoDetalhes").open = true;
      
        const situacaoDiv = document.getElementById("situacaoAluno");
      
        if (media >= 7) {
          situacaoDiv.textContent = "Situação: Aprovado ✅";
          situacaoDiv.className = "situacao aprovado";
        } else if (media < 4) {
          situacaoDiv.textContent = "Situação: Reprovado ❌";
          situacaoDiv.className = "situacao reprovado";
        } else {
          situacaoDiv.textContent = "Situação: Recuperação ⚠️";
          situacaoDiv.className = "situacao recuperacao";
        }
      }
      