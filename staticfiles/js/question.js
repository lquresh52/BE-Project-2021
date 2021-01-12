let neg_mark_yes = document.getElementById('neg_mark_yes')
let neg_mark_no = document.getElementById('neg_mark_yes')
let negativeMarksInput = document.getElementById('negativeMarksInput')

function Radio1(){
    negativeMarksInput.classList.remove('negative_input_hide')
    negativeMarksInput.classList.add('negative_input_show')

}
function Radio2() {
    negativeMarksInput.classList.remove('negative_input_show')
    negativeMarksInput.classList.add('negative_input_hide')
}
Radio2()