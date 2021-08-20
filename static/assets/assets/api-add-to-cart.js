async function AddToCart(productId){
    let basketData = {
        'product': parseInt(productId)
    }
    let response = await fetch('http://localhost:8000/az/api/v1/check-out/ordered-items/', {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
            'Authorization': `Token ${localStorage.getItem('Token')}`
        },
        body: JSON.stringify(basketData) 
    })
    data = await response.json()
    
    let response2 = await fetch(`http://localhost:8000/az/api/products/${data['product']}`,{
        method: "GET",
        headers:{
            "Content-Type":"application/json",
            Authorization:`Token ${localStorage.getItem("Token")}`,
        }
    })
    data2 = await response2.json()
    
    let cartList2 = document.getElementById('cart-navbar');
    let cartList3 = document.getElementsByClassName('cart-navbar');
    let price2 = data2["set_discount_price"]
    let total2 = price2 * data["quantity"]

    for (var i = 0 ; i < cartList3.length ; i++){
    varmi = cartList3[i].getAttribute("data-id")
        if (varmi == productId){
            data["quantity"] += 1
            return
        }
    }
    
    cartList2.innerHTML+=`
    <div id="deleteMain${data["id"]}" class="cart-navbar shp__single__product" data-id="${data2["id"]}" >
        <div class="shp__pro__thumb">
            <a href="#">
                <img src="${data2["image"]["image"]}" alt="product images">
            </a>
        </div>
        <div class="shp__pro__details">
            <h2><a href="product-details.html">${data2["title"]}</a></h2>
            <span class="quantity">QTY: ${data["quantity"]}</span>
            <span class="shp__price">£${price2}</span>
        </div>
        <div onclick="removeFunction(${data["id"]})" class="remove__btn">
            <a href="#" title="Remove this item"><i class="zmdi zmdi-close"></i></a>
        </div>
    </div>
    `
}; 