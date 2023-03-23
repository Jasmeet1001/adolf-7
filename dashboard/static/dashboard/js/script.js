function updateTime() {
    var element = document.getElementById("date-time");
    var now = new Date();
    var dateTime = now.toLocaleString();
    element.innerHTML = dateTime;
}
  
setInterval(updateTime, 1000);
  

const billDownload = ()=> {
    
    var invoice = document.getElementById("invoice");

    if(descriptions.length == 0){
        window.alert("No items added")
        return;
    }
    
    
    invoice.style.display = "block"
}
 


var descriptions = [];
var cart = [];
function addItem(button){

    // { id, vehical_tp, color, product_nm, item_desc, uom, mrp_incl_gst_pu }
    const product_info = button.dataset

    var productId = product_info.id;
    var vehical_tp = product_info.vehical_type;
    var color = product_info.color;
    var product_nm = product_info.product_name;
    var itemDesc = product_info.item_desc;
    var uom = product_info.uom;
    var mrpInclGstPu = product_info.mrp_incl_gst_pu;

    var productQuantityInp = document.getElementsByClassName("quantiy-Input")
    
    for(var i = 0; i < productQuantityInp.length; i++){
        if(productQuantityInp[i].classList.contains(productId)){
           var quantityInputValue = productQuantityInp[i].value
        }
    }

    if(!descriptionExists(vehical_tp, product_nm) && quantityInputValue > 0) {
        var counterBill = billStatement.getElementsByTagName("tr").length;
        var counterCart = cartStatement.getElementsByTagName("tr").length;
        var newRowBill = '<tr><td style="text-align: center; border-right: 1px solid black;">'+ (counterBill+1) +'</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ vehical_tp +'</td><td style="border-right: 1px solid black;" colspan="3">'+ color + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ product_nm + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ itemDesc + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ uom  + '</td><td style="width: 10px; border-right: 1px solid black;">' + quantityInputValue + '</td><td style="width: 10px; border-right: 1px solid black;">'+ (quantityInputValue*mrpInclGstPu) +'</tr>';
        var counterCartBill = '<tr><td>' + (counterCart+1) + '</td><td>' + vehical_tp + '</td><td>'+ product_nm + '</td><td>' + quantityInputValue + '</td><td>'+ (quantityInputValue*mrpInclGstPu) + '</td></tr>'
        billStatement.innerHTML += newRowBill; 
        cartStatement.innerHTML += counterCartBill;
        descriptions.push(product_info);
        cart.push(product_info);
    }
    else {
        window.alert("Can't add item with 0 quantity.")
    }

    
    
}

function descriptionExists(vehical_tp, product_nm) {
    for (var i = 0; i < descriptions.length; i++) {
        if (descriptions[i]["vehical_type"] === vehical_tp && descriptions[i]["product_name"] === product_nm) {
            window.alert("Already Added");
            return true;
        }
    }
    return false;
}


function removeItem(descriptions, cart){
    var billStatement = document.getElementById("billStatement");
    var rowsBill = billStatement.getElementsByTagName("tr");

    var cartStatement = document.getElementById("cartStatement");
    var rowsCart = cartStatement.getElementsByTagName("tr");

    
    if (descriptions.length > 0) {
        descriptions.pop();
        cart.pop();
        billStatement.deleteRow(rowsBill.length - 1);
        cartStatement.deleteRow(rowsCart.length - 1);

        for (var i = 1; i < rowsBill.length; i++) {
            rowsBill[i-1].cells[0].innerHTML = i.toString();
            rowsCart[i-1].cells[0].innerHTML = i.toString();
        }
    }
}

function reset() {
    descriptions = [];
    cart = [];

    cartStatement.innerHTML = "";
    billStatement.innerHTML = "";
  }
