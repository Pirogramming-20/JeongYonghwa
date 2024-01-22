const requestComment = new XMLHttpRequest();
const requestDeleteComment = new XMLHttpRequest();
const requestLike = new XMLHttpRequest();

function onClickLike(id, user_id) {
    const url = "/like/";
    requestLike.open("POST", url, true);
    requestLike.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    requestLike.send(JSON.stringify({post_id : id, user_id : user_id}));
}

function onClickSubmit(id, user_id) {
    const url = "/comment/create/";
    const content_input = document.getElementById('comment_input_' + id);
    const content = content_input.value;
    content_input.value = '';
    requestComment.open("POST", url, true);
    requestComment.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
        );
    requestComment.send(JSON.stringify({post_id : id, author_id : user_id, content : content}));
}

function onClickDelete(comment_id, post_id) {
    const url = "/comment/delete/";
    requestComment.open("POST", url, true);
    requestComment.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
        );
    requestComment.send(JSON.stringify({comment_id : comment_id, post_id : post_id}));
}
    
requestComment.onreadystatechange = () => {
    if (requestComment.readyState === XMLHttpRequest.DONE) {
        if (requestComment.status < 400) {
            const {html_content, post_id} = JSON.parse(requestComment.response);
            const container = document.getElementById('comment_container_'+ post_id);
            container.innerHTML = html_content;
        }
    }
}

requestDeleteComment.onreadystatechange = () => {
    if (requestDeleteComment.readyState === XMLHttpRequest.DONE) {
        if (requestDeleteComment.status < 400) {
            const {html_content, post_id} = JSON.parse(requestDeleteComment.response);
            const container = document.getElementById('comment_container_'+ post_id);
            container.innerHTML = html_content;
        }
    }
}

requestLike.onreadystatechange = () => {
    if (requestLike.readyState === XMLHttpRequest.DONE) {
        if (requestLike.status < 400) {
            const {post_id, liked, like_count} = JSON.parse(requestLike.response);
            const like_icon = document.getElementById('like_icon_' + post_id);
            const like_element = document.getElementById('like_count_'+post_id)
            if (liked){
                like_icon.innerText = '❤️';
            } else {
                like_icon.innerText = '🤍';
            }
            like_element.innerText = `좋아요: ${like_count}개`
        }
    }
} 