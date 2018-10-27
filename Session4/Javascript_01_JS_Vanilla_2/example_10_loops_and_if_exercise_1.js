
// write a function which fill the list with the fizzbuzz numbers

// for die zahlen 1 bis 100:
// teilbar durch 3 -> fizz
// teilbar durch 5 -> buzz
// teilbar durch 3 und 5 -> fizzbuzz
// sonst soll die zahl

var fizzBuzzList = document.getElementById('fizzBuzzList');

function appendElement(name,list){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(name));
    list.appendChild(li);
}

function fizzbuzz(){
    for(var i=0; i < 100; i++){
        if(i % 3 == 0 && i % 5 != 0){
            appendElement('fizz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 != 0){
            appendElement('buzz',fizzBuzzList);
        }else if(i % 5 == 0 && i % 3 == 0){
            appendElement('fizzBuzz',fizzBuzzList);
        }else{
            appendElement(i,fizzBuzzList);
        }
        console.log(i);
    }
}
