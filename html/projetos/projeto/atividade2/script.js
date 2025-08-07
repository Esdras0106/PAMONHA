document.addEventListener('DOMContentLoaded', function () {
    const botao = document.getElementById('gerarBotao');

    botao.addEventListener('click', function () {
        const idadeInput = document.getElementById('IdadeInput');
        const resultadoDiv = document.getElementById('resultado');
        const idade = parseInt(idadeInput.value);


        if (isNaN(idade) || idade < 0 || idade > 130) {
            resultadoDiv.innerHTML = "<p style='color:red;'>Por favor, insira uma idade válida entre 0 e 130.</p>";
            return;
        }

        let situacaoVoto = "";

        if (idade >= 18 && idade < 65) {
            situacaoVoto = "Voto obrigatório.";
        } else if (idade >= 16 && idade < 18) {
            situacaoVoto = "Voto opcional.";
        } else {
            situacaoVoto = "Voto não obrigatório.";
        }

        resultadoDiv.innerHTML = `<p><strong>${situacaoVoto}</strong></p>`;
    });
});
