document.addEventListener('DOMContentLoaded', () => {
    const slogans = [
        "Sauvons notre patrimoine !",
        "La lagune Ébrié, notre trésor en péril !",
        "Agissons ensemble contre la pollution !",
        "La nature a besoin de vous !"
    ];

    slogans.forEach((slogan, index) => {
        setTimeout(() => showPopup(slogan), index * 7000);
    });
});

function showPopup(message) {
    const popup = document.createElement('div');
    popup.innerText = message;
    popup.style.position = 'fixed';
    popup.style.top = '20px';
    popup.style.right = '20px';
    popup.style.backgroundColor = '#17252a';
    popup.style.color = '#fff';
    popup.style.padding = '10px 20px';
    popup.style.borderRadius = '5px';
    popup.style.zIndex = '1000';
    document.body.appendChild(popup);

    setTimeout(() => popup.remove(), 5000);
}
