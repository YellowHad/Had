
// use your fizzbuzz function

// create an input field and button, and run fizzbuzz when you click the button up until the number which was inputted into the input field

var fizzBuzzList = document.getElementById('fizzBuzzList');

function appendElement(name,list){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(name));
    list.appendChild(li);
}

function fizzbuzz(){
    var i = 0;
    do{
        if(i % 3 == 0 && i % 5 != 0){
            appendElement('fizz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 != 0){
            appendElement('buzz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 == 0){
            appendElement('fizzBuzz',fizzBuzzList);
        }else{
            appendElement(i,fizzBuzzList);
        }
        //console.log(i);
        i++;
    }while(i < 10)

    appendElement('New logic!',fizzBuzzList);

    var i = 0;
    while(true){
         if(i % 3 == 0 && i % 5 != 0){
            appendElement('fizz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 != 0){
            appendElement('buzz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 == 0){
            appendElement('fizzBuzz',fizzBuzzList);
        }else{
            appendElement(i,fizzBuzzList);
        }
        //console.log(i);
        i++;
        if(i == 100){
            break;
        }
    }
}

// Hybernate