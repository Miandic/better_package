import "../data.json"

let xhr = new XMLHttpRequest();
let url = "../static/data.json";
xhr.open("POST", url, true);
setRequestHeader("Content-Type", "application/json");

let city1 = document.querySelector('city1');
let city2 = document.querySelector('city2');
let length = document.querySelector('length');
let width = document.querySelector('width');
let high = document.querySelector('high');
let userData = JSON.stringify({ "city1": city1.value, "city2": city2.value, "length" : length.value, "width" : width.value, "high" : high.value})

let butCompare = document.getElementById('submit');
function ButClick() {
    let city1 = document.querySelector('city1');
    let city2 = document.querySelector('city2');
    let length = document.querySelector('length');
    let width = document.querySelector('width');
    let high = document.querySelector('high');
    let userData = JSON.stringify({ "city1": city1.value, "city2": city2.value, "length" : length.value, "width" : width.value, "high" : high.value})
    xhr.send(userData);

    data.onload = function() {
        if (Switch.checked){
            let arr = JSON.parse(train);
            updateData(arr);
        }
        else{
            let arr = JSON.parse(truck);
            updateData(arr);
        }
    }
}
butCompare.onclick = ButClick;

function updateData(jsonObj){
    let list = document.querySelector('.list');
    list.innerHTML = '';

    jsonObj.forEach(function(item, i, jsonObj){
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

let Switch = document.getElementByld('switch')
function SwitchOn() {
    $('.switch-btn').click(function(){
        $(this).toggleClass('switch-on');
        if ($(this).hasClass('switch-on')) {
          $(this).trigger('on.switch');
        } else {
          $(this).trigger('off.switch');
        }
      });
}
Switch.onclick = ButClick, SwitchOn;

let butSortDate = document.getElementById('sortDate')
function SortData() {
    function compare(a, b) {
        if (a.Data > b.Data) return 1;
        if (a.Data < b.Data) return -1;
        return 0;
    }
    let arr = JSON.parse(data)
    arr.sort(compare);
    updateData(arr)
}
butSortDate.onclick = SortData;

let butSortCost = document.getElementById('sortCost')
function SortCost() {
    function compare(a, b) {
        if (a.Cost > b.Cost) return 1;
        if (a.Cost < b.Cost) return -1;
        return 0;
    }
    let arr = JSON.parse(data)
    arr.sort(compare);
    updateData(arr)
}
butSortCost.onclick = SortCost;

let butSortName = document.getElementById('sortName')
function SortName() {
    let arr = JSON.parse(data)
    arr.sort();
    updateData(arr)
}
butSortName.onclick = SortName;