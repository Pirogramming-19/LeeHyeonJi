function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(items) {
    const container = document.querySelector(".items");
    container.innerHTML = items.map(item => createHTMLString(item)).join('');
}

 //배열의 요소 -> HTML li 태그(문자열)로 변경
function createHTMLString(item) {
    return `
        <li class="item">
            <img src="${item.img}" alt="${item.type}" class="item_thumnail">
            <span class="item_description">${item.gender}, ${item.size}</span>
        </li>
    `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;        //ex1) type     ex2) color
    const value = dataset.value;    //ex1) tshirt   ex2) blue

    //btn 외의 영역을 클릭한 경우
    if (key==null || value==null) {
        return;
    }

    //배열.filter(): 배열에서 특정 데이터만 추출해서 새로운 배열 만들기
    displayItems(items.filter(item => item[key] === value));
}

function setEventListeners(items) {
    const logo = document.querySelector(".logo");
    logo.addEventListener('click', () => displayItems(items));

    const btns = document.querySelector(".btns"); //이벤트의 위임(이벤트를 한 곳에서만 핸들링하기 위함)
    btns.addEventListener('click', event => onButtonClick(event, items));
}

loadItems()
    .then(items => {
        displayItems(items); //items는 배열
        setEventListeners(items);
    })
    .catch(console.log);