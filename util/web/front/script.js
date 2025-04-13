let allData = [];
let chartInstance = null;
let variante = null;
let difficulte = null;
let taux = true;

let btnToutesDifficultes = document.getElementById('toutes-difficultes');
let btnDifficulte1 = document.getElementById('difficulte-1');
let btnDifficulte2 = document.getElementById('difficulte-2');
let btnVarianteAll = document.getElementById('variante-all');
let btnVarianteEN = document.getElementById('variante-en');
let btnVarianteFR = document.getElementById('variante-fr');
let btnVarianteShort = document.getElementById('variante-short');
let btnTaux = document.getElementById('taux');
let btnNombre = document.getElementById('nombre');

async function loadData() {
    const response = await fetch('data/benchmark_results.json');
    allData = await response.json();
    afficher();
}

btnTaux.addEventListener('click', () => {
    btnTaux.classList.add('primary');
    btnNombre.classList.remove('primary');
    taux = true;
    afficher();
});

btnNombre.addEventListener('click', () => {
    btnNombre.classList.add('primary');
    btnTaux.classList.remove('primary');
    taux = false;
    afficher();
});

btnToutesDifficultes.addEventListener('click', () => {
    btnToutesDifficultes.classList.add('primary');
    btnDifficulte1.classList.remove('primary');
    btnDifficulte2.classList.remove('primary');
    difficulte = null;
    afficher();
});

btnDifficulte1.addEventListener('click', () => {
    btnDifficulte1.classList.add('primary');
    btnToutesDifficultes.classList.remove('primary');
    btnDifficulte2.classList.remove('primary');
    difficulte = "1";
    afficher();
});

btnDifficulte2.addEventListener('click', () => {
    btnDifficulte2.classList.add('primary');
    btnToutesDifficultes.classList.remove('primary');
    btnDifficulte1.classList.remove('primary');
    difficulte = "2";
    afficher();
});

btnVarianteAll.addEventListener('click', () => {
    btnVarianteAll.classList.add('primary');
    btnVarianteEN.classList.remove('primary');
    btnVarianteFR.classList.remove('primary');
    btnVarianteShort.classList.remove('primary');
    variante = null;
    afficher();
});

btnVarianteEN.addEventListener('click', () => {
    btnVarianteEN.classList.add('primary');
    btnVarianteAll.classList.remove('primary');
    btnVarianteFR.classList.remove('primary');
    btnVarianteShort.classList.remove('primary');
    variante = "en";
    afficher();
});

btnVarianteFR.addEventListener('click', () => {
    btnVarianteFR.classList.add('primary');
    btnVarianteAll.classList.remove('primary');
    btnVarianteEN.classList.remove('primary');
    btnVarianteShort.classList.remove('primary');
    variante = "fr";
    afficher();
});

btnVarianteShort.addEventListener('click', () => {
    btnVarianteShort.classList.add('primary');
    btnVarianteAll.classList.remove('primary');
    btnVarianteEN.classList.remove('primary');
    btnVarianteFR.classList.remove('primary');
    variante = "short";
    afficher();
});

function afficher() {
    const llms = [...new Set(allData.map(d => d.llm))];

    console.log(allData);

    let filteredData = variante === null ? allData : allData.filter(d => d.variant === variante);

    filteredData = difficulte === null ? filteredData : filteredData.filter(d => d.difficulty === difficulte);

    let nb = 0;

    const tauxDeReussite = llms.map(llm => {
        const items = filteredData.filter(d => d.llm === llm);
        const correct = items.filter(d => d.correct).length;
        nb = items.length;
        return taux ? (correct / items.length) * 100 : correct;
    });

    const ctx = document.getElementById('resultats').getContext('2d');

    if (chartInstance) {
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: llms,
            datasets: [{
                label: taux ? 'Taux de réussite (%)' : 'Nombre de réponses correctes',
                data: tauxDeReussite,
                backgroundColor: ['#1976d2'] 
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: taux ? 100 : nb,
                    title: {
                        display: true,
                        text: taux ? 'Taux de réussite (%)' : 'Nombre de réponses correctes'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'LLMs'
                    }
                }
            }
        }
    });
}

loadData();