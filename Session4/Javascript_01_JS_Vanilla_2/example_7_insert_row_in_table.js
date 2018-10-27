function get_random_number(low, high) {
    return low + Math.floor(Math.random() * (high-low));
}

function table_appender() {
    var table_body_element = document.getElementById("tbody_id");
    var new_table_row = table_body_element.insertRow(0);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var time_cell = new_table_row.insertCell(0);
    var number_cell = new_table_row.insertCell(1);

    var now = new Date();
    var now_string = now.toLocaleString();

    time_cell.innerHTML = now_string;
    number_cell.innerHTML = get_random_number(1,100);
}

