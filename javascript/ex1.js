let usuario = {
    nome: 'lucas',
    idade: 28,
    email: 'lucas@lucas.com',
    id: 123
}

if(usuario.nome != 'lucas' || usuario.email != 'lucas@lucas.com'){
    console.log('usuario nao localizado');
}if(usuario.nome == 'lucas' || usuario.email == 'lucas@lucas.com'){
    console.log('usuario  localizado');
}