import data from "../data.json"

function createData(jsonObj){

    jsonObj.forEach(function(item, i, jsonObj){
        let list = document.querySelector('.list');
        let inlist = document.createElement('div');
        inlist.classList = "inlist";

        let name = document.createElement('div');
        name.classList = "line";
        name.textContent = item.Name;
        inlist.append(name);

        let cost = document.createElement('div');
        cost.classList = "line";
        cost.textContent = item.Cost;
        inlist.append(cost);

        let date = document.createElement('div');
        date.classList = "line";
        date.textContent = item.Date;
        inlist.append(date);

        list.append(inlist);
    });
}

let butSearch = document.getElementById("submit");

function ButClick() {
    data.onload = function() {
        let arr = JSON.parse(data)
        createData(arr);
    }
}

butSearch.onclick = ButClick;

let butSortDate = document.getElementById("sortDate")

function SortData() {
    function compare(a, b) {
        if (a.Data > b.Data) return 1;
        if (a.Data < b.Data) return -1;
        return 0;
    }
    let arr = JSON.parse(data)
    arr.sort(compare);
    let list = document.querySelector('.list');
    list.innerHTML = '';
    createData(arr)
}

butSortDate.onclick = SortData;


let butSortCost = document.getElementById("sortCost")

function SortCost() {
    function compare(a, b) {
        if (a.Cost > b.Cost) return 1;
        if (a.Cost < b.Cost) return -1;
        return 0;
    }
    let arr = JSON.parse(data)
    arr.sort(compare);
    let list = document.querySelector('.list');
    list.innerHTML = '';
    createData(arr)
}

butSortCost.onclick = SortCost;


let butSortName = document.getElementById("sortName")

function SortName() {
    let arr = JSON.parse(data)
    arr.sort();
    let list = document.querySelector('.list');
    list.innerHTML = '';
    createData(arr)
}

butSortName.onclick = SortName;
