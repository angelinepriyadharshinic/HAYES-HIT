let total = 0;

function addToCart(item, price){

    let cart = document.getElementById("cart");

    let li = document.createElement("li");
    li.innerText = item + " - ₹" + price;

    cart.appendChild(li);

    total += price;

    document.getElementById("total").innerText = total;
}

function checkout(){

    if(total === 0){
        alert("Your cart is empty!");
        return;
    }

    alert(
        "Order Placed Successfully!\n\nTotal Amount: ₹" + total
    );

    document.getElementById("cart").innerHTML = "";

    total = 0;

    document.getElementById("total").innerText = total;
}