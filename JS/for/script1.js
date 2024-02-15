// Número de candidatos
const numCandidatos = 3;

// Inicializar contadores de votos para cada candidato
const votos = Array(numCandidatos).fill(0);

// Pedir o número total de eleitores
const numEleitores = prompt("Informe o número total de eleitores:");

// Loop para coletar votos de cada eleitor
for (let i = 1; i <= numEleitores; i++) {
    // Pedir ao eleitor para votar (1, 2 ou 3 para os candidatos)
    const voto = prompt(`Eleitor ${i}, vote (1, 2 ou 3 para os candidatos):`);
    
    // Validar o voto e incrementar o contador apropriado
    if (voto >= 1 && voto <= numCandidatos) {
        votos[voto - 1]++;
    } else {
        console.log(`Voto inválido do Eleitor ${i}.`);
    }
}

// Mostrar o número de votos de cada candidato
for (let j = 0; j < numCandidatos; j++) {
    console.log(`Candidato ${j + 1}: ${votos[j]} votos`);
}

