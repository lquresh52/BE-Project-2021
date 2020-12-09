
let ans1 = document.getElementById("ans1")
let ans2 = document.getElementById("ans2")
let ans3 = document.getElementById("ans3")
let ans4 = document.getElementById("ans4")

getInput=(id,ans)=>{
    if(id == 'option1text'){
        ans = ans1
    }else if(id == 'option2text'){
        ans = ans2
    }else if(id == 'option3text'){
        ans = ans3
    }else if(id == 'option4text'){
        ans = ans4
    }
    let input_text = document.getElementById(id).value
    console.log(input_text)
    console.log(ans)
    ans.value = input_text
    ans.innerHTML = input_text 
}