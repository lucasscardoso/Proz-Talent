let num = 4;
let num2 = 5;

function template(num,num2){
  console.log(`
${num} + ${num2} = ${num + num2}
4 - 5 = ${num - num2}
4 x 5 = ${num * num2}
4 / 5 = ${num / num2} `)
};

template(num,num2);


/*
    Acesse o site OneCompiler (link em anexo) e crie uma função que recebe dois números como parâmetros e imprime quatro frases no terminal (a partir de template strings) demonstrando as quatro operações básicas aplicadas a ambos números. Exemplo:

4 + 5 = 9
4 - 5 = -1
4 x 5 = 20
4 / 5 = 0.8 



*/