
// Write a page with a selector showing ids. (including HTML and Javascript)
// Once an option is selected, corresponding data ("title", "url", "thumbnailUrl") about the photo is displayed
// https://jsonplaceholder.typicode.com/photos/2

function change_post(){

    var post_title = document.getElementById('selection_title');
    var post_url = document.getElementById('selection_url');
    var post_url2 = document.getElementById('selection_url2');

    var sel = document.getElementById('post_selector');
    var sel_val = sel.options[sel.selectedIndex].value;

    var url = 'https://jsonplaceholder.typicode.com/photos/'+sel_val;
    console.log(sel);
    console.log(sel_val);
    console.log(url);

    fetch(url)
        .then((resp) => resp.json())
            .then(function(response){
                post_title.innerHTML = response["title"];
                post_url.innerHTML = response["url"];
                post_url2.innerHTML = response["thumbnailUrl"];
    });
}