const amountInput = document.getElementById('amount');
const amounthelp = document.getElementById('amounthelp');
const BALANCE = document.getElementById('account-balance').value;

let peopleCheckbox = document.querySelectorAll('.person-checkbox');
let peopleCount = 0; 
let checkedCnt = 0;

peopleCheckbox.forEach((element) => {
    element.setAttribute('disabled', true);
    element.checked = false;
})


amountInput.addEventListener('keyup', ()=>{
    peopleCount =  Math.floor(BALANCE/amountInput.value);
    amounthelp.innerHTML = peopleCount != Infinity ? `You can send at most ${peopleCount} persons.` : 'Enter Amount';
    if(peopleCount > 0 && peopleCount != Infinity){
        peopleCheckbox.forEach((element) => {
            element.removeAttribute('disabled', true);
            element.checked = false;
        })
    }else{
        peopleCheckbox.forEach((element) => {
            element.setAttribute('disabled', true);
        })
    }
})

peopleCheckbox.forEach(element => {
    element.addEventListener('change', (e) => {
        // counting no. of elements which is checked
        peopleCount =  Math.floor(BALANCE/amountInput.value);
        checkedCnt = 0;
        peopleCheckbox = document.querySelectorAll('.person-checkbox');
        peopleCheckbox.forEach((element) => {
            if(element.checked){
                checkedCnt++;
            }
        })


        // if checkbox reaches it people limit disable all the others
        if(checkedCnt >= peopleCount){
            peopleCheckbox.forEach((element) => {
                if(!element.checked){
                    element.setAttribute('disabled', true);
                }
            })
        }else{
            peopleCheckbox.forEach((element) => {
                element.removeAttribute('disabled', true);
            })
        }
    })
})
