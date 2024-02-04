document.addEventListener('DOMContentLoaded', function() {
    updateProductDetails(); // Викликати функцію при завантаженні сторінки
});

document.getElementById('variant-selector').addEventListener('change', function() {
    updateProductDetails(); // Викликати функцію при зміні варіанту
});

function updateProductDetails() {
    const selectedOption = document.getElementById('variant-selector').options[document.getElementById('variant-selector').selectedIndex];
    const price = selectedOption.getAttribute('data-price');
    const availability = selectedOption.getAttribute('data-availability');
    const weight = selectedOption.getAttribute('data-weight');
    const damages = selectedOption.getAttribute('data-damages');
    const height = selectedOption.getAttribute('data-height');
    const length = selectedOption.getAttribute('data-length');
    const width = selectedOption.getAttribute('data-width');
    const diameter = selectedOption.getAttribute('data-diameter');
    
    document.querySelector('.product-availability').textContent = `Наявність: ${availability}`;
    document.querySelector('.product-weight').textContent = `Вага: ${weight} кг`;
    document.querySelector('.product-damages').textContent = `Збитки: ${damages}`;
    document.querySelector('.product-length').textContent = `Довжина: ${length}`;
    document.querySelector('.product-width').textContent = `Ширина: ${width}`;
    document.querySelector('.product-diameter').textContent = `Діаметр: ${diameter}`;
    document.querySelector('.product-height').textContent = `Висота: ${height}`;

    document.getElementById('product-price-display').textContent = `₴ ${price}`;
}