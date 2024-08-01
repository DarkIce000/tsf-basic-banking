// get the usr data from the server
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
console.log(csrftoken);



const submitbtn = document.getElementById('submit-form');
submitbtn.addEventListener('click', (e) => {
    e.preventDefault();

    const receiversInputBox = document.querySelectorAll('.person-checkbox');
    let recieversIds = [];
    receiversInputBox.forEach((element) => {
        if(element.checked){
            recieversIds.push(element.getAttribute('id'))
        }
    })

    const amountValue = document.querySelector('#amount').value;
    fetch('transaction/', {
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        method: 'POST',
        body: JSON.stringify({
            'amount': amountValue,
            'recievers_ids':recieversIds,
        })
    })
    .then(response => response.json())
    .then(result => {
        location.reload()
    })
})


// fetch('transcation/',{
//     headers:{'X-CSRFToken': csrftoken},
//     mode: 'cors',

// })