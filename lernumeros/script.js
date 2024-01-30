let N1 = Number(prompt("Digite um numero: "));
let N2 = Number(prompt("Digite um numero: "));
let N3 = Number(prompt("Digite um numero: "));

if (N1>N2 && N1>N3 && N3>N2){
    window.alert(N1 + " é o maior e "+ N2 + " é o menor" )
}

else if (N1>N2 && N2>N3 && N1>N3){
    window.alert(N1 + ' é o maior e ' + N3 + ' é o menor')
}

else if (N2>N1 && N2>N3 && N3>N1){
    window.alert(N2 + ' é o maior e ' + N1 + ' é o menor')
}

else if (N2>N1 && N2>N3 && N1>N3){
    window.alert(N2 + ' é o maior e ' + N3 + ' é o menor')
}

else if (N3>N2 && N3>N1 && N2>N1){
    window.alert(N3 +'é o maior e ' + N1 + ' é o menor')
}

else if (N3>N2 && N3>N1 && N1>N2){
    window.alert(N3 +'é o maior e ' + N2 + ' é o menor')
}
