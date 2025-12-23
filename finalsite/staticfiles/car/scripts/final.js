
//    for car data
    document.addEventListener('DOMContentLoaded', () => {
    const carsContainer = document.getElementById('cars-container');    

    if (!carsContainer) {
        console.error("The main container element with ID 'cars-container' is missing.");
        return; 
    }

    // Fetch car data and i will only display 3 random cars
    function getRandomCars(cars, count = 3) {
    const shuffled = [...cars].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
    }


async function getCars() {
    try {
        const response = await fetch("data/cars.json");
        const data = await response.json();

        // Get 3 random cars
        const randomCars = getRandomCars(data.cars, 3);

        displayCars(randomCars);
    } catch (error) {
        console.error("Error loading car data:", error);
    }
}

    // Display car cards and this is part of my DOM manipulation to inject data into HTML.
    function displayCars(cars) {
        carsContainer.innerHTML = ""; // Clear container

        cars.forEach(car => {
            const card = document.createElement("div");
            card.classList.add("car-container");

            // THIS IS PART OF MY TEMPLATE LITERALS using backticks not single or double quotes.
           card.innerHTML = `
          <img src="${car.image}" alt="${car.make} ${car.model}" width="300" height="200" loading="lazy" decoding="async">

        <div class="car-info">
        <span class="make"><strong>Make:</strong> ${car.make}</span>
        <span class="model"><strong>Model:</strong> ${car.model}</span>
        <span class="year"><strong>Year:</strong> ${car.year}</span>
        <span class="price"><strong>Price:</strong> $${car.price.toLocaleString()}</span>
        
        <div class="more-info" style="display: none;">
            <span class="mileage"><strong>\nMileage:</strong> ${car.mileage.toLocaleString()} miles</span>
            <span class="fuel"><strong>Fuel Type:</strong> ${car.fuel}</span>
            <span class="transmission"><strong>Transmission:</strong> ${car.transmission}</span>
            <span class="color"><strong>Color:</strong> ${car.color}</span>
            <span class="body-type"><strong>Body Type:</strong> ${car.bodyType}</span>
            
        </div>

        <button class="see-more-btn">SEE MORE</button>
    </div>
`;

// Add event listener for the button
const seeMoreBtn = card.querySelector('.see-more-btn');
const moreInfo = card.querySelector('.more-info');

seeMoreBtn.addEventListener('click', () => {
    if (moreInfo.style.display === 'none') {
        moreInfo.style.display = 'block';
        seeMoreBtn.textContent = 'SEE LESS';
    } else {
        moreInfo.style.display = 'none';
        seeMoreBtn.textContent = 'SEE MORE';
    }
});

            carsContainer.appendChild(card);
        });
    }

    // Call getCars to load the data
    getCars();
});
