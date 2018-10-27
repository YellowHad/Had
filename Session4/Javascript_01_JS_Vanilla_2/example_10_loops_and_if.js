function appender(number, list_id) {
  var ul = document.getElementById(list_id);
  var li = document.createElement("li");
  li.appendChild(document.createTextNode(number));
  ul.appendChild(li);
}

// for loop

for(var i=0; i<100; i++){
    if(i%2==0){
        appender(i, "list");
    }
    else if (i % 3 === 0){
        appender(i + "  is divisor of 3", "list");
    }
    else {
        appender("Not Right", "list");
    }
}

// do while

var k = 0;
do{
    appender((new Date()).toLocaleString(), "timeslist");
    k++;
}while(k < 10)

// while

var l = 0;
while(true){
    l++;
    console.log(l)
    if(l === 10){ break; }
}
