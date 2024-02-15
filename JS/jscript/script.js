let nota1 =( Number (prompt("Digite sua nota: ")));
let nota2 = (Number (prompt("Digite sua nota: ")));

let media = ((nota1 + nota2) / 2);

if (media === 10){
    window.alert('Nota final' + media.toFixed(2) + 'Aprovado com distinção! Parabéns');
}

else if (media<7){
    window.alert('Nota Final' + media.toFixed(2) + 'Reprovado, Melhore!');
}

else if (media >= 7){
    window.alert('Nota Final' + media.toFixed (2) + 'Aprovado Parabéns!');
}