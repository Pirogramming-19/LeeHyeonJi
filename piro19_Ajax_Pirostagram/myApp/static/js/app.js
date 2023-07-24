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

const requestLvComm = new XMLHttpRequest();

function leaveComment(post_id) {
    const comment = document.querySelector('.post-id-' + post_id + '-comment').value;
    
    requestLvComm.open('POST', '/leave_comment_ajax/', true);
    requestLvComm.setRequestHeader(
        'Content-Type',
        'application/x-www-form-urlencoded'
    );
    requestLvComm.send(JSON.stringify({'post_id':post_id, 'comment':comment}));
}

requestLvComm.onreadystatechange = () => {
    if (requestLvComm.readyState === XMLHttpRequest.DONE) {
        if (requestLvComm.status < 400) {
            const {post_id, comment, comment_id} = JSON.parse(requestLvComm.response);
            makeNodes(post_id, comment, comment_id);
            removeNewComment(post_id);
        }
    }
}

function makeNodes(post_id, comment, comment_id) {
    let spanTag = document.createElement('span');
    let textNode = document.createTextNode(comment);
    spanTag.appendChild(textNode);

    buttonTag = document.createElement('button');
    buttonTag.setAttribute('type', 'button');
    buttonTag.setAttribute('class', 'xBtn');
    buttonTag.setAttribute('onclick', 'removeComment(' + comment_id + ')');
    textNode = document.createTextNode('삭제');
    buttonTag.appendChild(textNode);

    const pTag = document.createElement('p');
    pTag.setAttribute('class', 'comment-id-' + comment_id);
    pTag.appendChild(spanTag);
    pTag.appendChild(buttonTag);

    const divTag = document.querySelector('.post-id-' + post_id + '-comments');
    divTag.appendChild(pTag);
}

function removeNewComment(post_id) {
    const inputTag = document.querySelector('.post-id-' + post_id + '-comment');
    inputTag.value = '';
}

const requestRmComm = new XMLHttpRequest();

function removeComment(comment_id) {
    requestRmComm.open('POST', '/remove_comment_ajax/', true);
    requestRmComm.setRequestHeader(
        'Content-Type',
        'application/x-www-form-urlencoded'
    );
    requestRmComm.send(JSON.stringify({'comment_id':comment_id}));
}

requestRmComm.onreadystatechange = () => {
    if (requestRmComm.readyState === XMLHttpRequest.DONE) {
        if (requestRmComm.status < 400) {
            const {comment_id} = JSON.parse(requestRmComm.response);
            const comment = document.querySelector('.comment-id-' + comment_id);
            comment.remove();
        }
    }
}
