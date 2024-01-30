let salario = parseFloat(prompt('Informe seu salário'));
let reajuste; 
let aumento;


if (salario <= 280.00){
    aumento = (salario *0.20);
    reajuste = (salario + (salario *0.20));
    window.alert('Seu novo salário é de: ' + reajuste + ',\n seu salario antigo era de: '
    + salario.toFixed(2) + ', \nhouve um aumento de 20% e o valor do seu aumento foi de ' + aumento 
    )
}
else if (salario > 280.00 && salario <=700.00 ){
    aumento = (salario *0.15);
    reajuste = (salario + (salario *0.15));
    window.alert('Seu novo salário é de: ' + reajuste + ',\n seu salario antigo era de: '
    + salario.toFixed(2) + ', \nhouve um aumento de 20% e o valor do seu aumento foi de ' + aumento 
    )
}
else if (salario > 700.00 && salario <=1500.00 ){
    aumento = (salario *0.10);
    reajuste = (salario + (salario *0.10));
    window.alert('Seu novo salário é de: ' + reajuste + ',\n seu salario antigo era de: '
    + salario.toFixed(2) + ', \nhouve um aumento de 20% e o valor do seu aumento foi de ' + aumento 
    )
}
else if (salario > 1500.00){
    aumento = (salario *0.05);
    reajuste = (salario + (salario *0.05));
    window.alert('Seu novo salário é de: ' + reajuste + ',\n seu salario antigo era de: '
    + salario.toFixed(2) + ', \nhouve um aumento de 20% e o valor do seu aumento foi de ' + aumento 
    )
}