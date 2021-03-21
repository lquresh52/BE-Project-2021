
function selectCorrectAns(id, divId, counter) {

    var op1 = document.getElementById('optionid-1'+counter);
    var op2 = document.getElementById('optionid-2'+counter);
    var op3 = document.getElementById('optionid-3'+counter);
    var op4 = document.getElementById('optionid-4'+counter);

    // question_type will tll us if question is objective or descriptive
    var question_type = document.getElementById('question-type-'+counter); 
    var correct_ans = document.getElementById('selected-op-'+counter);

    var Cans = document.getElementById('Canswer')
    console.log(Cans + '---------------');
    var nextBtn = document.getElementById('nextBtn')
    var mainDiv = document.getElementById(divId);
    console.log("MAIN DIV ", mainDiv)
    var spans = mainDiv.getElementsByTagName('span');
    console.log(spans);
    if (spans[0].innerHTML == 'check_circle') {
        console.log(spans[0])
        spans[0].innerHTML = 'radio_button_unchecked'
        mainDiv.classList.remove('cid');
        spans[0].classList.remove('greenicon')
        nextBtn.disabled = true;
    }
    else {
        console.log('ELSEEEEEE');
        spans[0].innerHTML = 'check_circle';
        spans[0].classList.add('greenicon');
        mainDiv.classList.add('cid');
        nextBtn.disabled = false;

        if (mainDiv != op1) {
            deSelectRest(op1)
        }
        else {
            correct_ans.value = 1;
        }

        if (mainDiv != op2) {
            deSelectRest(op2)
        }
        else {
            correct_ans.value = 2;
        }

        if (mainDiv != op3) {
            deSelectRest(op3)
        }
        else {
            correct_ans.value = 3;
        }

        if (mainDiv != op4) {
            deSelectRest(op4)
        }
        else {
            correct_ans.value = 4;
        }
    }

}

function descriptiveAns(id, loopCount){
    var descAns = document.getElementById(id).value;
    document.getElementById('selected-op-'+loopCount).value = descAns;
    console.log(document.getElementById('selected-op-'+loopCount).value);
}



function deSelectRest(divRef) {

    var spans = divRef.getElementsByTagName('span');
    console.log(spans + ' <<<=====');
    if (spans[0].innerHTML == 'check_circle') {
        console.log(spans[0])
        spans[0].innerHTML = 'radio_button_unchecked'
        divRef.classList.remove('cid');
        spans[0].classList.remove('greenicon')
    }
}

