
var op1 = document.getElementById('optionid-1');
var op2 = document.getElementById('optionid-2');
var op3 = document.getElementById('optionid-3');
var op4 = document.getElementById('optionid-4');
var correct_ans = document.getElementById('corr_op');

function selectCorrectAns(id, divId) {
    var Cans = document.getElementById('Canswer')
    console.log(Cans+'---------------');
    var nextBtn = document.getElementById('nextBtn')
    var mainDiv = document.getElementById(divId);
    console.log("MAIN DIV ", mainDiv)
    var spans = mainDiv.getElementsByTagName('span');
    console.log(spans);
    if (spans[1].innerHTML == 'check_circle') {
        console.log(spans[1])
        spans[1].innerHTML = 'radio_button_unchecked'
        mainDiv.classList.remove('cid');
        spans[1].classList.remove('greenicon')
        nextBtn.disabled = true;
    }
    else {
        console.log('ELSEEEEEE');
        spans[1].innerHTML = 'check_circle';
        spans[1].classList.add('greenicon');
        mainDiv.classList.add('cid');
        nextBtn.disabled = false;

        if (mainDiv != op1) {
            deSelectRest(op1)
        }
        else{
            correct_ans.value = 1;
        }
        
        if (mainDiv != op2) {
            deSelectRest(op2)
        }
        else{
            correct_ans.value = 2;
        }

        if (mainDiv != op3) {
            deSelectRest(op3)
        }
        else{
            correct_ans.value = 3;
        }
        
        if (mainDiv != op4) {
            deSelectRest(op4)
        }
        else{
            correct_ans.value = 4;
        }
    }

}



function deSelectRest(divRef) {

    var spans = divRef.getElementsByTagName('span');
    console.log(spans+' <<<=====');
    if (spans[1].innerHTML == 'check_circle') {
        console.log(spans[1])
        spans[1].innerHTML = 'radio_button_unchecked'
        divRef.classList.remove('cid');
        spans[1].classList.remove('greenicon')
    }
}


function disableImgInp(opId, imgId) {
    var opText = document.getElementById(opId)
   
    console.log(opText.value)
    var img = document.getElementById(imgId)
    if (opText.value == '') {
        img.style.pointerEvents = 'auto'  
        img.style.opacity = '1'  
        
    }
    else {
        img.style.pointerEvents = 'none'
        img.style.opacity = '0.5'
        

    }
}



function disableTextInput(fileId,opId){
    //alert("HELLO BHARAT")
    var file = document.getElementById(fileId)
    var op = document.getElementById(opId) 
    var imgLen = file.files.length
    console.log("IMAGESSSS LENGTH",imgLen)
    if (imgLen>0){
        op.style.display = 'none'
         
    }
    else{
        op.style.display = 'block' 
    }
}
