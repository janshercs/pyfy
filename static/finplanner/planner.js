
function calc_timeRemaining(form){
    var c_age = parseInt(form.elements['id_c_age'].value);
    var r_age = form.elements['id_r_age'].value;
    if (Number.isInteger(c_age)) {
        var timeRemaining = r_age - c_age;
        return timeRemaining;
    }
    else {
        return;
    }
}

function calc_savings(form){
    var salary = form.elements['id_salary'].value;
    var expense = form.elements['id_expense'].value;
    return salary-expense
}

function display(){
    var theForm = document.forms["user_data"];
    var timeRemaining = calc_timeRemaining(theForm);
    var savings = calc_savings(theForm);
    if (Number.isInteger(timeRemaining)){
       theForm.elements['time_remaining'].value = timeRemaining;
    }
    if (Number.isInteger(savings)){
        theForm.elements['id_savings'].value = savings;
    }
    
}

document.getElementById('id_r_age').addEventListener("change", display);
document.getElementById('id_expense').addEventListener("change", display);