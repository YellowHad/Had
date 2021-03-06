var car = {brand:"fiat", color:"white", km:10000};
document.getElementById("car").innerHTML = car;

var cars = [
    {brand:"fiat", color:"white", km:10000},
    {brand:"vw", color:"polo", km:20000},
    {brand:"bmw", color:"i3", km:30000},
    {brand:"tesla", color:"model s", km:40000}
];


function car_to_table_appender(car_object) {
    var table_body_element = document.getElementById("cars_table_body");
    var new_table_row = table_body_element.insertRow(0);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var brand_cell = new_table_row.insertCell(0);
    var km_cell = new_table_row.insertCell(1);

    brand_cell.innerHTML = car_object.brand;
    km_cell.innerHTML = car_object.km;
}

cars.forEach(function(car) {
    car_to_table_appender(car)
});
