let titulo = document.createElement('h1');
titulo.id = 'titulo';
titulo.textContent = 'Loja de Produtos';


document.body.appendChild(titulo);


let produto = document.createElement('div');
produto.innerHTML = `
    <h2>Nome do Produto: Playstation 5</h2>
    <p>Descrição: Video game playstation, 2 controles e um jogo.</p>
    <p>Preço: R$ 5000,00</p>
`;

document.body.appendChild(produto);