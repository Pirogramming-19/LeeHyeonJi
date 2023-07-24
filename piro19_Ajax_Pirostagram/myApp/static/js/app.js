const requestLike = new XMLHttpRequest();

function upAndDownLike(post_id) {
    const likeTag = document.querySelector('.post-id-' + post_id);
    const like = likeTag.innerText;

    if (like == '♡') {
        likeTag.innerText = '♥';
        incdec = 'inc';
    }
    else {
        likeTag.innerText = '♡';
        incdec = 'dec';
    }

    requestLike.open('POST', '/like_ajax/', true);
    requestLike.setRequestHeader(
        'Content-Type',
        'application/x-www-form-urlencoded'
    );
    requestLike.send(JSON.stringify({'post_id':post_id, 'incdec':incdec}));
}

requestLike.onreadystatechange = () => {
    if (requestLike.readyState === XMLHttpRequest.DONE) {
        if (requestLike.status < 400) {
            const {post_id, like_cnt} = JSON.parse(requestLike.response);
            document.querySelector('.post-id-' + post_id + '-count').innerText = like_cnt;
        }
    }
}