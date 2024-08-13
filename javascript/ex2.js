const numerosDaSorte = [37, 14, 26, 5, 94, 87];

for (let i = 0; i < numerosDaSorte.length; i++) {
    const num = numerosDaSorte[i];

    if (num < 50 && num % 2 === 0) {
        console.log(`${num} é par e menor que 50`);
    } else if (num < 50) {
        console.log(`${num} é menor que 50`);
    } else if (num > 50) {
        console.log(`${num} é maior que 50`);
    }
}

/*
Acesse o site OneCompiler (Link abaixo), copie e cole o array 'numerosDaSorte', e logo em seguida escreva o código necessário para avaliar cada elemento do array e imprimir uma frase seguindo algum dos seguintes três modelos:

- X é par e menor que 50
- X é menor que 50
- X é maior que 50


numerosDaSorte = [37, 14, 26, 5, 94, 87]  

https://onecompiler.com/javascript/42p3wx7jp

*/