const check = (s) => {

    flag=false

    if(s[0]!='+' || s[s.length-1]!='+'){
        return false
    }

    for(let i=1 ; i<s.length; i++){

        if(s[i]== '+') {
            if(s[i-1]=='+' || s[i+1]=='+'){
                return false
            }
        }
        if(s[i] >= 'a' && s[i] <= 'z'){
            if(s[i-1] == '+' && s[i+1] == '+'){
                flag=true
            }
            else {
                flag=false;
                break;
            }
        }
    }

    return flag
}


const perform = () => {

    var originalString = document.getElementById('myString')
    var output1 = document.getElementById('ans1')
    if(originalString.value==''){
        alert('please enter the sequence and then proceed!')
    }
    else {
        var s = originalString.value;
        if(check(s)){
            output1.value='The sequence matches the given constraints.'
        }
        else {
            output1.value='The sequence does not matches the given constraints.'
        }
    }
}


