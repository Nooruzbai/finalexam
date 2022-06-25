async function make_request(url, context) {
    let response = await fetch(url, context);
    if (response.ok) {
        console.log('OK')
        return await response.json();
    } else {
        console.log('Not Successful')
        let error = new Error(response.statusText);
        error.response = response;
        error_res = await response.json()
        console.log(error_res.error)
        return error_res;
    }

}


let Moderate = async function (event) {
    let url = event.target.dataset.apiUrl;

    let data = await make_request(url, {
        method: "GET", headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    }
    )

}

let Cancel = async function (event) {
    console.log(event.target)

    let url = event.target.dataset.apiUrl;
    console.log(url)

      let data = await make_request(url, {
        method: "GET", headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
}
