// create a function add_date, which appends a current date as string to the list with id="list"

function add_date() {
    var ul = document.getElementById("list");
    var li = document.createElement("li");

    var date = new Date();

    var text = date.toLocaleString();

    li.appendChild(document.createTextNode(text));
    ul.appendChild(li);
}
