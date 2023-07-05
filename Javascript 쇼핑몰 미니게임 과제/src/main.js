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

loadItems()
    .then(items => {
        displayItems(items); //items는 배열
        // setEventListeners(items);
    })
    .catch(console.log);
