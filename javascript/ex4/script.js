const titulo = document.getElementById('titulo');
const link = document.getElementById('link-proz');
const listaOrdenada = document.getElementById('lista-ordenada');
const listaNaoOrdenada = document.querySelector('ul');

if (titulo) {
    titulo.innerText = 'Olá, seja bem-vindo';
} else {
    console.error('Elemento <h1> não encontrado!');
}


if (link) {
    link.innerText = 'Bem-vindo, clique no link e visite nosso site';
} else {
    console.error('Elemento <a> não encontrado!');
}


if (listaOrdenada) {
    listaOrdenada.innerHTML = `
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    `;
} else {
    console.error('Elemento <ol> não encontrado!');
}


if (listaNaoOrdenada) {
    listaNaoOrdenada.innerHTML = `
        <li>Item A</li>
        <li>Item B</li>
        <li>Item C</li>
    `;
} else {
    console.error('Elemento <ul> não encontrado!');
}