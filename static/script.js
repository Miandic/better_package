import {$,jQuery} from 'jquery-3.5.1.min.js';
//хуй
let list = document.querySelector('.list');
//хуй
var flag = jQuery.parseJSON("data.json")
while (flag["a"] == 0) {
    flag = jQuery.parseJSON("data.json")
}
var e = jQuery.parseJSON("data.json")
alert(e.a)
var arr = [["http://cyberforum.ru/images/cyberforum_logo.png", "Cdek", "500"], ["http://cyberforum.ru/images/cyberforum_logo.png", "DHL","300"]]; //массив хуйни сайтов

var but = document.getElementById("submit");
function ButClick() {
    arr.forEach(function(item, i, arr){

    let inlist = document.createElement('div');
    inlist.classList = "inlist";

    let logo = document.createElement('div');
    let img = document.createElement('img');
    img.src = item[0];
    logo.append(img);
    inlist.append(logo);

    let name = document.createElement('div');
    name.classList = "line";
    name.textContent = item[1];
    inlist.append(name);

    let cost = document.createElement('div');
    cost.classList = "line";
    cost.textContent = item[2];
    inlist.append(cost);

    list.append(inlist);
    });
};
but.onclick = ButClick;
