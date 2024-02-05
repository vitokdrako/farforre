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
function openCartPage() {
    window.location.href = '/cart/';
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function addProductToCart(variantId, quantity) {
    fetch('/add-to-cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Використовуйте csrftoken, отриманий з кукі
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            variant_id: variantId,
            quantity: quantity
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        // Логіка обробки відповіді сервера
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}