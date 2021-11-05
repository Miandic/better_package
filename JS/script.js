function checkJson (jsonPath){
    return(fetch(jsonPath)
        .then(response => response.json())
        .then(data => {
            return (data)
        }))
}
let jsonData = checkJson('data.json')

const interval = setInterval(() => {
    if(jsonData != checkJson('data.json')){
        jsonData = checkJson('data.json')
        fetch('data.json')
            .then(response => response.json())
            .then(data => {
                let d = data
                console.log('Updated')
                document.getElementById("name").innerHTML = d[0].Name
                document.getElementById("cost").innerHTML = d[0].Cost
                document.getElementById("date").innerHTML = d[0].Date
                document.getElementById("name").className = 'vis'
                document.getElementById("cost").className = 'vis'
                document.getElementById("date").className = 'vis'
            })
    }
}, 1000)


