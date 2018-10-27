// create a function add_date, which appends a current date as string to the list with id="list"
var ul = document.getElementById("list");
var date = new Date();

function add_date(){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(date.toLocaleString()));
    ul.appendChild(li);
}

//setInterval(add_date,1000);