var cakes = document.getElementById('cakes')
var cookies = document.getElementById('cookies')
var breads = document.getElementById('breads')
var bill = document.getElementById('bill')

const generateBill = () => {
    
    if (cakes.value == '' || cookies.value == '' || breads.value == '' || cakes.value < 0 || cookies.value < 0 || breads.value < 0  ) {
        alert('Please fill all the details properly!!')
    }
    else {
        var totalBill = cakes.value * 220 + cookies.value * 250 + breads.value * 50
        bill.value = totalBill
    }

}

const payNow = () => {

    if (bill.value=='' || bill.value <=0) {
        alert('Please fill all the details and the generate the bill!!')
    }
    else {
        alert('Thank you for your purchase! Have a nice day!!')
        cakes.value = ''
        cookies.value = ''
        breads.value = ''
        bill.value = ''
    }
    
}
