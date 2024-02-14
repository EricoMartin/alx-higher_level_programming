// script that fetches the character name from a URL
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('div#character').html(data);
});
