function increase(num) {
    const interest = document.getElementById('interest' + num);
    interest.innerText = Number(interest.innerText) + 1;

    const Http = new XMLHttpRequest();
    Http.open('GET', 'http://127.0.0.1:8000/idea/' + num + '/inc/');
    Http.send();
}

function decrease(num) {
    const interest = document.getElementById('interest' + num);
    if (Number(interest.innerText) > 0) {
        interest.innerText = Number(interest.innerText) - 1;

        const Http = new XMLHttpRequest();
        Http.open('GET', 'http://127.0.0.1:8000/idea/' + num + '/dec/');
        Http.send();
    }
}

function star(num) {
    const star = document.querySelector('.star' + num);
    if (star.innerText == '☆') {
        star.innerText = '★';
        url = 'http://127.0.0.1:8000/idea/staron/' + num + '/';
    }
    else if (star.innerText == '★') {
        star.innerText = '☆';
        url = 'http://127.0.0.1:8000/idea/staroff/' + num + '/';
    }

    const Http = new XMLHttpRequest();
    Http.open('GET', url);
    Http.send();
}