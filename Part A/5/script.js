
const changeString = () => {


    var originalString = document.getElementById('myString')
    var output1 = document.getElementById('ans1')
    var output2 = document.getElementById('ans2')


    if(originalString.value==''){
        alert('Please fill the box with a sentence')
    }
    else {

        var originalsen = originalString.value;
        var s=originalsen.replace(/ /g, '')
        var newString = ''

        for(let i=0; i<s.length ; i++){
            if(s[i] == 'z') {
                newString += 'a'
            }
            else {
                var char = String.fromCharCode(s.charCodeAt(i) + 1)
                newString +=char
            }
        }
        
        output1.value=newString
    
        const vowels = ['a', 'e', 'i', 'o', 'u']
    
        var finalString = ''
    
        for(let j=0; j<newString.length; j++){
    
            if(vowels.indexOf(newString[j]) >= 0){
                    finalString+=newString[j].toUpperCase()
            }
            else {
                finalString+=newString[j]
            }
        }
    
        output2.value=finalString
        originalString.value=''
    }


}


