var button = document.getElementById('btn');
var is_read = false;

function changeColor(){
    //ternary operator
    button.style.backgroundColor= is_read? "red":"green";
    button.style.color = is_read? "yellow" : "blue";
    is_read = !is_read;
    console.log("Button clicked")
}
//Visual Studio Code