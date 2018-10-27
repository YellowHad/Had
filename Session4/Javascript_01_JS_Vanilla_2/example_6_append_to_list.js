function get_random_number(low, high) {
    return low + Math.floor(Math.random() * (high-low));
}

function appender() {
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(get_random_number(1,100)));
    ul.appendChild(li);
}

setInterval(appender, 1000);
