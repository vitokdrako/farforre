document.getElementById('variant-selector').addEventListener('change', function() {
    const selectedOption = this.options[this.selectedIndex];
    const price = selectedOption.getAttribute('data-price');
    const availability = selectedOption.getAttribute('data-availability');
    const weight = selectedOption.getAttribute('data-weight');
    const damages = selectedOption.getAttribute('data-damages');
    const height = selectedOption.getAttribute('data-height');
    const length = selectedOption.getAttribute('data-length');
    const width = selectedOption.getAttribute('data-width');
    const diameter = selectedOption.getAttribute('data-diameter');
    
    // Оновіть дані на сторінці з отриманими значеннями
    document.querySelector('.product-availability').textContent = `Наявність: ${availability}`;
    document.querySelector('.product-weight').textContent = `Вага: ${weight} кг`;
    document.querySelector('.product-damages').textContent = `Збитки: ${damages}`;
    document.querySelector('.product-length').textContent = `Довжина: ${length}`;
    document.querySelector('.product-width').textContent = `Ширина: ${width}`;
    document.querySelector('.product-diameter').textContent = `Діаметр: ${diameter}`;
    document.querySelector('.product-height').textContent = `Висота: ${height}`;

    // Оновіть ціну з урахуванням отриманого значення
    document.getElementById('product-price-display').textContent = `₴ ${price}`;
});
