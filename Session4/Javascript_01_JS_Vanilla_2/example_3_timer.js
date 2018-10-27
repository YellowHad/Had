function set_time(){
    var myDate = new Date();
    document.getElementById("time").innerHTML = myDate.toLocaleString();
    document.getElementById("seconds").innerHTML = myDate.getSeconds();
    document.getElementById("millisecs").innerHTML = myDate.getMilliseconds();
    console.log(myDate.toISOString());
}
setInterval(set_time, 10);
