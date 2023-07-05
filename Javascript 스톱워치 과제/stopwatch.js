const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const resetBtn = document.getElementById("reset-btn");
const trashIcon = document.getElementById("trash");
const allChbx = document.getElementById("all-chbx");
const chbxs = document.getElementsByClassName("chbx");
let interval;

//<div class="row"> 노드를 만들어서 반환하는 함수
function makeRowNode(sec, millisec) {
    let divTag = document.createElement("div");
    divTag.setAttribute("class", "row"); //<div class="row"></div>

    let inputTag = document.createElement("input");
    inputTag.setAttribute("type", "checkbox");
    inputTag.setAttribute("class", "chbx");
    inputTag.setAttribute("onclick", "chbx()"); //<input type="checkbox" class="chbx" onclick="chbx()">
    divTag.appendChild(inputTag);

    let h2Tag = document.createElement("h2");
    let h2InnerText = document.createTextNode(sec + ":" + millisec);
    h2Tag.appendChild(h2InnerText); //<h2>01:36</h2>
    divTag.appendChild(h2Tag);

    return divTag;
}

//<div class="row">를 <div id="record">의 자식 노드로 추가하는 함수
function addRowNode(sec, millisec) {
    let record = document.getElementById("record");
    record.appendChild(makeRowNode(sec, millisec));
}

function getMillisecSpan() {
    return document.getElementById("millisec");
}

function getSecSpan() {
    return document.getElementById("sec");
}

function getAllChbx() {
    return document.getElementById("all-chbx");
}

function getChbxs() {
    return document.getElementsByClassName("chbx");
}

function getRows() {
    return document.getElementsByClassName("row");
}

//'start' 버튼 클릭 시, 스톱워치 동작
startBtn.addEventListener("click", () =>  {
    let millisecSpan = getMillisecSpan();
    let secSpan = getSecSpan();

    let millisec = parseInt(millisecSpan.innerText);
    let sec = parseInt(secSpan.innerText);
    
    interval = setInterval(() => {
        millisec++;
        if (millisec == 100) {
            millisec = 0;
            sec++;
        }
        millisecSpan.innerText = String(millisec).padStart(2, "0");
        secSpan.innerText = String(sec).padStart(2, "0");
    }, 10);
});

//'stop' 버튼 클릭 시, (1) 스톱워치 중단 (2) 구간 기록에 row 추가
stopBtn.addEventListener("click", () => {
    clearInterval(interval);
    addRowNode(getSecSpan().innerText, getMillisecSpan().innerText);
});

//'reset' 버튼 클릭 시, 스톱워치 reset
resetBtn.addEventListener("click", () => {
    clearInterval(interval);

    getMillisecSpan().innerText = "00";
    getSecSpan().innerText = "00";
});

//trash 아이콘 클릭 시, (1) 전체 삭제 (2) 일부 삭제
trashIcon.addEventListener("click", () => {

    let allChbx = getAllChbx();
    let rows = getRows();
    if (allChbx.checked) {
        for (let i=rows.length-1; i>=0; i--) {
            rows[i].remove();
        }
        allChbx.checked = false;
    }
    else {
        let chbxs = getChbxs();
        for (let i=chbxs.length-1; i>=0; i--) {
            if (chbxs[i].checked) {
                rows[i].remove();
            }
        }
    }
});

//id="all-chbx" 체크박스 클릭 시, 나머지 체크박스 전체 선택 또는 전체 해제
allChbx.addEventListener("click", () => {
    let allChbx = getAllChbx();
    let chbxs = getChbxs();
    if (allChbx.checked) {
        for (let chbx of chbxs) {
            chbx.checked = true;
        }
    }
    else {
        for (let chbx of chbxs) {
            chbx.checked = false;
        }
    }
});

//class="chbx"에 따라서 id="all-chbx"의 체크 여부 결정
function chbx() {
    let chbxs =  getChbxs();
    let allChbx = getAllChbx();
    for (let chbx of chbxs) {
        if (!chbx.checked) {
            if (allChbx.checked == true) {
                allChbx.checked = false;
            }
            return;
        }
    }
    allChbx.checked = true;
}