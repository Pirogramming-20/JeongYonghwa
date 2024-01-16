function changeMarked(pk) {
    var mark = document.getElementById('mark_' + pk);
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                mark.classList.toggle('marked', response.marked);
                mark.innerHTML = response.marked ? '❤️' : '🤍';
            }
        };
        xhr.open('GET', '/idea/change_marked/' + pk);
        xhr.send();
}