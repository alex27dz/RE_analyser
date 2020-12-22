//javascript 

async function onGetAddrBtnClick() {
    const payload = {};
    payload.street = document.getElementById("street").value;
    payload.city = document.getElementById("city").value;
    payload.short_state = document.getElementById("short_state").value;
    payload.state = document.getElementById("state").value;
    const response = await getAddrData(payload);
    outputParams(response)
    console.log(response);
    //debugger
}

async function getAddrData(payload) {
    try {
        console.log(payload);
        const flask_server='http://127.0.0.1:5000/address'
        const response = await axios.post(flask_server, payload);
        return response;
    } catch (error) {
        console.error(error);
    }
    
}

function outputParams(response) {
    const test = document.getElementById("output-page").innerHTML = JSON.stringify(response.data, undefined, '\n');
    let htmlString = ''
    for (const [key, value] of Object.entries(response.data)) {
        htmlString+= `<div><span>${key}:</span><span>${value}</span></div>`
        }

    const htmlObject = document.getElementById('output-page');   
    //htmlObject.innerHTML = htmlString  
    htmlObject.innerHTML = response.data  
    console.log(`test is ${test}`)
}