let requestURL = 'data.json';
let request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

function createData(jsonObj){

    jsonObj.forEach(function(item, i, jsonObj){
        let list = document.querySelector('.list');
        let inlist = document.createElement('div');
        inlist.classList = "inlist";

        let logo = document.createElement('div');
        let img = document.createElement('img');
        img.src = item[0];
        logo.append(img);
        inlist.append(logo);

        let cost = document.createElement('div');
        cost.classList = "line";
        cost.textContent = item[1];
        inlist.append(cost);

        let date = document.createElement('div');
        date.classList = "line";
        date.textContent = item[2];
        inlist.append(date);

        list.append(inlist);
    });
}

function move() {
    var elem = document.getElementById("blueBar");
    var width = 0;
    var id = setInterval(frame, 10);
    function frame() {
        if (width >= 100) {
            clearInterval(id);
        }
        else {
            width++;
            elem.style.width = width + '%';
        }
    }
}

let butSearch = document.getElementById("submit");

function ButClick() {
    request.onload = function() {
        let arr = request.response;
        createData(arr);
    }
}

butSearch.onclick = ButClick;

function changeData(arr){

}

let butSortDate = document.getElementById("sortDate")

function SortData() {
    function compare(a, b) {
        if (a.Data > b.Data) return 1;
        if (a.Data < b.Data) return -1;
        return 0;
    }
    let arr = request.response;
    arr.sort(compare);
    changeData(arr)
}

butSortDate.onclick = SortData;


let butSortCost = document.getElementById("sortCost")

function SortCost() {
    function compare(a, b) {
        if (a.Cost > b.Cost) return 1;
        if (a.Cost < b.Cost) return -1;
        return 0;
    }
    let arr = request.response;
    arr.sort(compare);
    changeData(arr)
}

butSortCost.onclick = SortCost;


let butSortName = document.getElementById("sortName")

function SortName() {
    let arr = request.response;
    arr.sort();
    changeData(arr)
}

butSortName.onclick = SortName;
