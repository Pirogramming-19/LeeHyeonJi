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