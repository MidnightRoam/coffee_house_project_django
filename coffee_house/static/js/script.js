// const goods = document.querySelectorAll(".item");
checkboxElements = document.querySelectorAll("[name='goods']")
resultElement = document.querySelector(".result")
buttonElement = document.querySelector(".btn")
inputGoods = document.querySelector("input[type=number]");
inputName = document.querySelector("#name")
inputSurname = document.querySelector("#surname")
resultElement.textContent = '€0';
let totalPrice = 0;

const user = {
    name: "",
    surname: "",
};

checkboxElements.forEach(element => {
    element.addEventListener("change", function(){
        if (element.checked) {
            if (inputGoods.value <= 0 || inputGoods.value > 100) {
                inputGoods.value = 1;
            }
            totalPrice += parseInt(element.value) * parseInt(inputGoods.value);
        } else {
            totalPrice -= parseInt(element.value) * parseInt(inputGoods.value);
        }

        if (totalPrice !== 0) {
            resultElement.textContent = `€${totalPrice}`;
        } else {
            resultElement.textContent = '€0'
        }
    })
})

// function totalCounting() {
//     for (const product of goods) {
//         if (checkboxElement.checked) {
//             if (inputGoods.value <= 0 || inputGoods.value > 100) {
//                 inputGoods.value = 1;
//             }
//             totalPrice += parseInt(checkboxElement.dataset.price) * parseInt(inputGoods.value);
//         } else {
//             totalPrice -= parseInt(checkboxElement.value) * parseInt(inputGoods.value);
//         }
//     }
// }

buttonElement.addEventListener("click", function () {
    let total = 0;
    user.name = inputName.value;
    user.surname = inputSurname.value;

    for (const element of checkboxElements) {
        if (element.checked) {
            total += parseInt(element.value)
        }
    }

    if (totalPrice != 0 && user.name != '' && user.surname != '') {
        resultElement.textContent = alert(
            `Customer: ${user.name} ${user.surname} \nTotal: €${totalPrice}`
        )
    } else if (totalPrice == 0) {
        resultElement.textContent = alert("You didn't order anything")
    } else if (user.name == '' || user.surname == '') {
        resultElement.textContent = alert('Enter contact details')
    }
})