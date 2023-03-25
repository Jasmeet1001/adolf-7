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
    
    let pdfWindow=window.open('','PRINT','height=650,width=900,top=100,left=150');
    pdfWindow.document.write(`<html><head><title>Invoice</title>`);
    pdfWindow.document.write('</head><body >');
    pdfWindow.document.write(invoice.innerHTML);
    pdfWindow.document.write('</body></html>');

    pdfWindow.document.close(); // necessary for IE >= 10
    pdfWindow.focus(); // necessary for IE >= 10*/
    pdfWindow.print();
    
    pdfWindow.close();
    invoice.style.display = "none"
}
 


var descriptions = [];
var cart = [];
var amount = [];
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

        var amountPerProduct = quantityInputValue*mrpInclGstPu

        var counterBill = billStatement.getElementsByTagName("tr").length;
        var counterCart = cartStatement.getElementsByTagName("tr").length;
        var newRowBill = '<tr><td style="text-align: center; border-right: 1px solid black;">'+ (counterBill+1) +'</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ vehical_tp +'</td><td style="border-right: 1px solid black;" colspan="3">'+ color + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ product_nm + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ itemDesc + '</td><td style="width: 10px; border-right: 1px solid black;" colspan="3">'+ uom  + '</td><td style="width: 10px; border-right: 1px solid black;">' + quantityInputValue + '</td><td style="width: 10px; border-right: 1px solid black;">'+ amountPerProduct +'</tr>';
        var counterCartBill = '<tr><td>' + (counterCart+1) + '</td><td>' + vehical_tp + '</td><td>'+ product_nm + '</td><td>' + quantityInputValue + '</td><td>'+ amountPerProduct + '</td></tr>'
        billStatement.innerHTML += newRowBill; 
        cartStatement.innerHTML += counterCartBill;
        descriptions.push(product_info);
        cart.push(product_info);
        amount.push(amountPerProduct)

        var totalAmount = amount.reduce((acc, val) => acc + val, 0)

        var billStatementAmount = document.getElementById("billStatementAmount")
        billStatementAmount.innerHTML = '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">Total Amount</td><td colspan="5" style="text-align: center;">' + totalAmount + '</td></tr>' + '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">GST</td><td colspan="5" style="text-align: center;">Unknown</td></tr>' + '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">Final Amount</td><td colspan="5" style="text-align: center;">' +  + '</td></tr>'
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


function removeItem(){
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
        
        amount.pop();
        var totalAmount = amount.reduce((acc, val) => acc + val, 0)
        var billStatementAmount = document.getElementById("billStatementAmount")
        billStatementAmount.innerHTML = '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">Total Amount</td><td colspan="5" style="text-align: center;">' + totalAmount + '</td></tr>' + '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">GST</td><td colspan="5" style="text-align: center;">Unknown</td></tr>' + '<tr style="background: rgba(217,225,242,1.0); border-bottom: 1px solid black;"><td colspan="13" style="border-right: 1px solid black;">Final Amount</td><td colspan="5" style="text-align: center;">' +  + '</td></tr>'

    }
}

function reset() {
    descriptions = [];
    cart = [];
    amount = [];

    cartStatement.innerHTML = "";
    billStatement.innerHTML = "";
    billStatementAmount.innerHTML = "";
}
