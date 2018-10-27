function change_photo(){

    var photo_url = document.getElementById('selected_photo_url');
    var photo_thumbnailurl = document.getElementById('selected_photo_thumbnailurl');
    var photo_title = document.getElementById('selected_photo_title');
    var selector = document.getElementById('photo_selector');
    var selected_value = selector.options[selector.selectedIndex].value;

    var url = 'https://jsonplaceholder.typicode.com/photos/'+selected_value;
    console.log(selector);
    console.log(selected_value);
    console.log(url);

    fetch(url)
        .then((resp) => resp.json())
            .then(function(response){
                photo_title.innerHTML = response["title"];
                photo_url.src = response['url'];
                photo_thumbnailurl.src = response['thumbnailUrl'];
    });

    /*
        import json
        lambda resp: json.loads(resp)
        def some_func(resp):
            return json.loads(resp)
    */

    //JSON_ARRAYS[]


}