let cartNavbar = document.getElementById('cart-navbar');
async function getCartNavbar(){
    let response  = await fetch('http://localhost:8000/az/api/v1/check-out/ordered-items/',)
    data = await response.json()
    data.forEach(element => {
    cartNavbar.innerHTML += `
    <div id="deleteMain${element.id}" class="cart-navbar shp__single__product" data-id="${element.product.id}">
        <div class="shp__pro__thumb">
            <a href="#">
                <img src="${element.product.image.image}" alt="product images">
            </a>
        </div>
        <div class="shp__pro__details">
            <h2><a href="product-details.html">${element.product.title}</a></h2>
            <span class="quantity">QTY: ${element.quantity}</span>
            <span class="shp__price">£${element.product.set_discount_price}</span>
        </div>
        <div onclick="removeFunction(${element.id})" class="remove__btn">
            <a  href="#" title="Remove this item"><i class="zmdi zmdi-close"></i></a>
        </div>
    </div>
    `
    });
}


addLoadEvent(async() => {
    await getCartNavbar() ;
})



async function removeFunction(order_id){
    let response = await fetch(`http://localhost:8000/az/api/v1/check-out/ordered-items/${order_id}/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('Token')}`
            },
        })
        if (document.getElementById(`removeMain${order_id}`) != null){

            document.getElementById(`removeMain${order_id}`).remove()
        }
        document.getElementById(`deleteMain${order_id}`).remove()
}
