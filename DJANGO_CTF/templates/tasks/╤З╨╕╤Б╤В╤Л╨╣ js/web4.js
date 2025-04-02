let Barny = 0;
let btn = document.getElementById("btn");
let count = document.getElementById("count");
let text = document.getElementById("text_of_task");
btn.onclick = popka;
function popka() {
    Barny ++;
    if (Barny === 20000) {
        text.innerHTML = 'OFR{Iqn_U5_Qm5k_:)}'
    }
    count.innerHTML = Barny;
};