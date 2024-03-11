$(document).ready(function () {
    $(document).on('click', '#qty-minus', function (event) {
        event.preventDefault();
        var inputField = $(this).closest('.input-spinner').find('input[type="text"]');
        var currentValue = parseInt(inputField.val());
        if (currentValue > 1) {
            inputField.val(currentValue - 1);
            inputField.trigger('change'); // Вызываем событие change
            inputField.focus();

        }
        var product_id = $(this).closest('.input-spinner').find('.qty-cart').data('product-id');
        updateCartQuantity(currentValue - 1, product_id);
    });
    // Увеличить количество товара
    $(document).on('click', '#qty-plus', function (event) {
        event.preventDefault()
        var inputField = $(this).closest('.input-spinner').find('input[type="text"]');
        var currentValue = parseInt(inputField.val());
        inputField.val(currentValue + 1);
        inputField.trigger('change'); // Вызываем событие change
        inputField.focus();
        var product_id = $(this).closest('.input-spinner').find('.qty-cart').data('product-id');
        updateCartQuantity(currentValue + 1, product_id);
    });
    $(document).on('change', '#qty-cart', function () {
        var currentValue = $(this).val();
        var product_id = $(this).closest('.input-spinner').find('.qty-cart').data('product-id');
        updateCartQuantity(currentValue, product_id);
    });

    function updateCartQuantity(currentValue,product_id) {
        var cartAddUrl = $('#cart-add-url').val();
        var csrfToken = $('#csrf-token').val();

        console.log('Product ID:', product_id);
        console.log('CSRF Token:', csrfToken);
        console.log('cartaddurl', cartAddUrl);
        console.log('Current value:', currentValue);
        $.ajax({
            type: 'POST',
            url: cartAddUrl,
            data: {
                product_id: product_id,
                product_qty: currentValue,
                csrfmiddlewaretoken: csrfToken,
                action: 'post'
            },
            success: function (json) {
                console.log(json);
                console.log('Cart contents');
                console.log(json.quantities);
            },
            error: function (xhr, errmsg, err) {
                // Обработка ошибок
            }
        });
    }
})
