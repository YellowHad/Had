function fizzbuzz_easy(){
    for (var i=1; i <= 20; i++)
    {
        if (i % 15 == 0)
            console.log("FizzBuzz");
        else if (i % 3 == 0)
            console.log("Fizz");
        else if (i % 5 == 0)
            console.log("Buzz");
        else
            console.log(i);
    }
}

function fizzbuzz_medium(){
    for (var i = 1; i <= 100; i++) {
      var f = i % 3 === 0;
      var b = i % 5 === 0;
      console.log(f ? b ? "FizzBuzz" : "Fizz" : b ? "Buzz" : i);
    }
}

function fizzbuzz_expert(){
    for(var i=0;i<100;)console.log((++i%3?'':'Fizz')+(i%5?'':'Buzz')||i)
}
