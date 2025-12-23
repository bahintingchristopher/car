// car/scripts/inventory.js

document.addEventListener('DOMContentLoaded', () => {
    const carsContainer = document.getElementById('cars-container');
    const dialog = document.getElementById('mydialog');

    if (!carsContainer || !dialog) {
        console.error("Required elements missing: carsContainer or mydialog.");
        return;
    }

    const carCards = carsContainer.querySelectorAll('.car-highlight');

    carCards.forEach(card => {
        const advBtn = card.querySelector('.adv-btn');
        
        if (advBtn) {
            advBtn.addEventListener('click', () => {
                
                const car = {
                    make: card.getAttribute('data-make') || 'N/A',
                    model: card.getAttribute('data-model') || 'N/A',
                    year: card.getAttribute('data-year') || 'N/A',
                    price: card.getAttribute('data-price') || '0', 
                    image: card.getAttribute('data-image') || '/static/car/images/no-image.webp',
                    description: card.getAttribute('data-description') || 'No detailed description available.',
                    mileage: card.getAttribute('data-mileage') || 'N/A',
                    fuel: card.getAttribute('data-fuel') || 'N/A',
                    transmission: card.getAttribute('data-transmission') || 'N/A',
                    color: card.getAttribute('data-color') || 'N/A',
                    bodyType: card.getAttribute('data-bodytype') || 'N/A',
                };

                const formatNumber = (value) => {
                    const num = Number(value);
                    return isNaN(num) ? value : num.toLocaleString();
                };

                dialog.innerHTML = `
                    <div class="dialog-header">
                        <h2>UNIQUE FEATURES</h2>
                        <button id="closeDialog">X</button>
                    </div>
                    <img src="${car.image}" alt="${car.make} ${car.model}" width="300" height="200" loading="lazy" decoding="async">
                    <h3>${car.make} ${car.model} (${car.year})</h3>
                    <p><strong>Description:</strong> ${car.description}</p>
                    <hr>
                    <p><strong>Price:</strong> $${formatNumber(car.price)}</p>
                    <p><strong>Mileage:</strong> ${formatNumber(car.mileage)} miles</p>
                    <p><strong>Fuel Type:</strong> ${car.fuel}</p>
                    <p><strong>Transmission:</strong> ${car.transmission}</p>
                    <p><strong>Color:</strong> ${car.color}</p>
                    <p><strong>Body Type:</strong> ${car.bodyType}</p>
                `;
                
                dialog.showModal();

                dialog.querySelector("#closeDialog").addEventListener("click", () => {
                    dialog.close();
                });
            });
        }
    });
});