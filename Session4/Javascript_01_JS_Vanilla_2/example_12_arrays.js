var fruits = ["Banana", "Orange", "Apple", "Mango"];

document.getElementById("fruits1").innerHTML = fruits.toString();

document.getElementById("fruits2").innerHTML = fruits.join(" * ");


function appender(li_text) {
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(li_text));
    ul.appendChild(li);
}

function start_appender(){
    fruits.forEach(function(fruit) {
        appender(fruit);
    });
}
