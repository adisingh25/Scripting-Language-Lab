var original_string = []
var myLength = []
var length_3_string = []

var myString = document.getElementById('myString')

const getLength = (sen) => {
    myLength.unshift(sen.length)
}

// const check =  (s)  =>  s.length <= 3;

const longWay = (arr1, arr2) => {
    length_3_string=[]
    for(let i=0 ; i<arr2.length; i++){
        if(arr2[i] <=3){
            length_3_string.push(arr1[i])
        }
    }
}


const getValues = (sen,callback) => {
    original_string.unshift(sen)
    callback(sen)

    // length_3_string = original_string.filter(check);
    longWay(original_string, myLength)
  
}



const perform = ()=> {
    var sentence=myString.value 
    if(sentence.trim().length === 0){
        alert('Please fill the values!!')
    }
    else {
        myString.value=''
        getValues(sentence,getLength)

        console.log(original_string)
        console.log(myLength)
        console.log(length_3_string)
    }
}