function change_post(){

    var post_body = document.getElementById('selected_post_body');
    var post_title = document.getElementById('selected_post_title');
    var selector = document.getElementById('post_selector');
    var selected_value = selector.options[selector.selectedIndex].value;

    var url = 'https://jsonplaceholder.typicode.com/posts/'+selected_value;
    console.log(selector);
    console.log(selected_value);
    console.log(url);

    fetch(url)
        .then((resp) => resp.json())
            .then(function(response){
                post_title.innerHTML = response["title"];
                post_body.innerHTML = response["body"];
    });
}
