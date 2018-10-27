
var is_blue = true;
function set_time(){
    is_blue = !is_blue
    document.getElementById("time").innerHTML = (new Date()).toLocaleString();
    document.getElementById("seconds").innerHTML = (new Date()).getSeconds();
    document.getElementById("seconds").style.color = is_blue ? "blue":"red";
}
setInterval(set_time, 1000);
