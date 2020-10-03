
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
    return salary-expense;
}

function calc_final_years(form){
    var r_age = form.elements['id_r_age'].value;
    return 80-r_age;
}

function calc_r_expense(form){
    var expense = parseInt(form.elements['id_expense'].value);
    var years = calc_timeRemaining(form);
    var inflation = 1 + form.elements['id_inflation'].value/100;
    var exp_inflation = inflation ** years;
    var result = expense*exp_inflation*0.7;
    return Math.round(result);
}

function display(){
    var theForm = document.forms["user_data"];
    var timeRemaining = calc_timeRemaining(theForm);
    var savings = calc_savings(theForm);
    var final_years = calc_final_years(theForm);
    var r_expense = calc_r_expense(theForm);
    if (Number.isInteger(timeRemaining)){
       theForm.elements['time_remaining'].value = timeRemaining;
    }
    if (Number.isInteger(savings)){
        theForm.elements['id_savings'].value = savings;
    }
    if (Number.isInteger(final_years)){
        theForm.elements['id_final_years'].value = final_years;
    }
    if (!Number.isNaN(r_expense)){
        theForm.elements['id_r_expense'].value = r_expense;
    }
}

document.getElementById('id_r_age').addEventListener("change", display);
document.getElementById('id_expense').addEventListener("change", display);
document.getElementById('id_inflation').addEventListener("change", display);