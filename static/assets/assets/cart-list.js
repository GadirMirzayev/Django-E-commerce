let cartList = document.getElementById('cart-list');
async function getCartItems(){
    let response  = await fetch('http://localhost:8000/az/api/v1/check-out/ordered-items/',)
    
    data = await response.json()
    data.forEach(element => {
        let price = element.product.set_discount_price
        let total = price * element.quantity
        cartList.innerHTML += `
        <tr id="removeMain${element.id}">
            <td class="product-thumbnail"><a href="#"><img
                        src="${element.product.image.image}"
                        alt="product img" /></a></td>
            <td class="product-name"><a href="#">${element.product.title}</a></td>
            <td class="product-price"><span class="amount">£${price}</span></td>
            <td class="product-quantity"><input type="number" data-id="${element.id}" value="${element.quantity}" class="countProduct" /></td>
            <td class="product-subtotal">£${total}</td>
            <td onclick="deleteFunction(${element.id})" class="product-remove"><button class="delete" data-id="${element.id}" class="deleteProduct">X</button></td>
        </tr>
        `
    });
}


$(document).click(function(event) {
    let target = $(event.target);
    if($(target).hasClass('countProduct')){
        target.on('input', async function(event){
            console.log("SALAM");
            let basketId = this.dataset.id
            let input = this.value
            let data = {
                'quantity': input
            }
            let response2 = await fetch(`http://localhost:8000/az/api/v1/check-out/ordered-items/${basketId}/`, {
                method: "PUT",
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${localStorage.getItem('Token')}`
                },
                body: JSON.stringify(data)
            })
            let resData = await response2.json()
            let newTotal = resData.product_details.set_discount_price * resData.quantity
            this.parentElement.nextElementSibling.innerHTML = `<td class="product-subtotal">£${newTotal}</td>`
        })
    }
});


addLoadEvent(async() => {
    await getCartItems() ;
})



async function deleteFunction(order_id){
    let response = await fetch(`http://localhost:8000/az/api/v1/check-out/ordered-items/${order_id}/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('Token')}`
            },
        })
        document.getElementById(`removeMain${order_id}`).remove()
        document.getElementById(`deleteMain${order_id}`).remove()
}