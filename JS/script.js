
fetch('data.json')
.then(response => response.json())
.then(data => {
    var d = data
    console.log(d)
    document.getElementById("name").innerHTML = d[0].Name
    document.getElementById("cost").innerHTML = d[0].Cost
    document.getElementById("date").innerHTML = d[0].Date
    document.getElementById("name").className = 'vis'
    document.getElementById("cost").className = 'vis'
    document.getElementById("date").className = 'vis'
})
