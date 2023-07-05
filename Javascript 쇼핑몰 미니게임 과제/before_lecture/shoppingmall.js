//id="clothes"의 모든 자식 노드를 제거하는 함수
function removeAllNodes() {
    let clothesChildren = document.getElementById("clothes").children;
    for(let i=clothesChildren.length-1; i>=0; i--) {
        clothesChildren[i].remove();
    }
}

//id="clothes"의 자식 노드를 id="clothes"에 추가하는 함수
function addNodes(clothes, gender, size) {
    let clothesDiv = document.getElementById("clothes");
    for (let tmp=0; tmp<2; tmp++) {
        for (let i=0; i<clothes.length; i++) {
            child = makeNodes(clothes[i], gender[i] + ", " + size[i] +  " size"); //"pink_t", "female, large size"
            clothesDiv.appendChild(child);
        }
    }
}

//id="clothes"의 자식 노드 1개를 생성하는 함수
function makeNodes(clothes, text) {
    let divTag = document.createElement("div");

    let imgTag = document.createElement("img");
    imgTag.setAttribute("src", "./img/" + clothes + ".png");
    imgTag.setAttribute("alt", clothes);
    divTag.append(imgTag);

    let textNode = document.createTextNode(text);
    divTag.append(textNode);

    return divTag;
}

window.onload = function() {
    let clothes = ["pink_t", "blue_p", "yellow_p", "yellow_s", "blue_s", "blue_t", "yellow_t", "pink_p"];
    let gender = ["female", "man", "man", "man", "female", "male", "male", "female"];
    let size = ["large", "small", "large", "large", "small", "large", "large", "small"];
    
    addNodes(clothes, gender, size);
}

function getT() {
    let clothes = ["pink_t", "blue_t", "yellow_t"];
    let gender = ["female", "male", "male"];
    let size = ["large", "large", "large"];

    removeAllNodes();
    addNodes(clothes, gender, size);
}

function getP() {
    let clothes = ["blue_p", "yellow_p", "pink_p"];
    let gender = ["man", "man", "female"];
    let size = ["small", "large", "small"];
    
    removeAllNodes();
    addNodes(clothes, gender, size);
}

function getS() {
    let clothes = ["yellow_s", "blue_s"];
    let gender = ["man", "female"];
    let size = ["large", "small"];

    removeAllNodes();
    addNodes(clothes, gender, size);
}

function getBlue() {
    let clothes = ["blue_p", "blue_s", "blue_t"];
    let gender = ["man", "female", "male"];
    let size = ["small", "small", "large"];
    
    removeAllNodes();
    addNodes(clothes, gender, size);
}

function getYellow() {
    let clothes = ["yellow_p", "yellow_s", "yellow_t"];
    let gender = ["man", "man", "male"];
    let size = ["large", "large", "large"];
    
    removeAllNodes();
    addNodes(clothes, gender, size);
}

function getPink() {
    let clothes = ["pink_t", "pink_p"];
    let gender = ["female", "female"];
    let size = ["large", "small"];
    
    removeAllNodes();
    addNodes(clothes, gender, size);
}
