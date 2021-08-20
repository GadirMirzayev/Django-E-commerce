let shopList = document.getElementById('shop-list');

async function getShopItems(){
    let response  = await fetch(`http://localhost:8000/az/api/products/`,)
   
    data = await response.json()
    data.forEach(element => {
        shopList.innerHTML += `
        <div class="col-md-3 single__pro col-lg-3 cat--1 col-sm-4 col-xs-12">
            <div class="product foo">
                <div class="product__inner">
                    <div class="pro__thumb">
                        <a href="${element.get_absolute_url}">
                            <img src="${element.image.image}" alt="product images">
                        </a>
                    </div>
                    <div class="product__hover__info">
                        <ul class="product__action">
                            <li><a data-toggle="modal" data-target="#productModal" title="Quick View" class="quick-view modal-view detail-link" href="#"><span class="ti-plus"></span></a></li>
                            <li><button onclick="AddToCart(${element.id})" class="ti-shopping-cart add-to-cart"></button></li>
                            <li><a title="Wishlist" href="wishlist.html"><span class="ti-heart"></span></a></li>
                        </ul>
                    </div>
                </div>
                <div class="product__details">
                    <h2><a href="${element.get_absolute_url}">${element.title}</a></h2>
                    <ul class="product__price">
                        <li class="old__price">$${element.price}</li>
                        <li class="new__price">$${element.set_discount_price}</li>
                    </ul>
                </div>
            </div>
        </div>
        `
    });
}


addLoadEvent(async() => {
    await getShopItems() ;
})
    



















 