const repeticao = document.querySelector(".ex3");

 (()=>{
    for(let i = 0; i < 3; i++){

        repeticao.innerHTML += "Conexão feita com sucesso! <br>";
    }
})();


// referencia https://developer.mozilla.org/en-US/docs/Glossary/IIFE
//aproveitei o exercicio para aplicar algo que aprendi chamado Immediately Invoked Function Expression (IIFE)
// onde declaramos nossa função anonima dentro de () e para chamar novamente ao final do codigo utilizamos () , assim a função é executada após sua definição.