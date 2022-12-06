var item = document.getElementById('itemname')
var quantity = document.getElementById('itemquantity')
var price = document.getElementById('itemprice')
var amount = document.getElementById('amount')
var billArea = document.getElementById('billArea')

const generateBill = () => {

    if (item.value == '' || quantity.value == 0 || price.value == 0) {
        alert('Please fill all the details!!')
    }
    else {
        billArea.removeAttribute("hidden")
        var totalBill = quantity.value * price.value
        amount.value = totalBill


    }
}

const payNow = () => {

    if (item.value == '' || quantity.value == 0 || price.value == 0) {
        alert('Please fill all the details and the generate the bill!!')
    }
    else {
        alert('Thank you for your purchase! Have a nice day!!')
        item.value = ''
        quantity.value = 0
        price.value = 0.0
        amount.value = 0.0
    }
}
