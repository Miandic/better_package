let lenghtInput = document.getElementById('lenght').value
let widthInput = document.getElementById('width').value
let highInput = document.getElementById('high').value
let weightInput = document.getElementById('weight').value
let city1Input = document.getElementById('city1').value
let city2Input = document.getElementById('city2').value

const interval = setInterval(() => {
    lenghtInput = document.getElementById('lenght').value
    widthInput = document.getElementById('width').value
    highInput = document.getElementById('high').value
    weightInput = document.getElementById('weight').value
    city1Input = document.getElementById('city1').value
    city2Input = document.getElementById('city2').value
}, 500)

function logInputs(){
    console.log(lenghtInput)
    console.log(widthInput)
    console.log(highInput)
    console.log(weightInput)
    console.log(city1Input)
    console.log(city2Input)
    console.log(' ')
    postData('Хуй');
    console.log(' ')

}


function postData(input) {
    let bruh = $.ajax({
        type: 'POST',
        url: 'testing_responce.py',
        data: { param: input },
        
    });
    return bruh.responseText;
}





