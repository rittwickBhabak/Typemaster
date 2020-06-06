inputfield = document.getElementById('inputfield');
giventext = document.getElementById('giventext').textContent;
myForm = document.getElementById('myForm');

spanText = ``;
for(let  i = 0; i<giventext.length;i++){
    spanText += `<span class="givenLetter">${giventext[i]}</span>`
}
document.getElementById('giventext').innerHTML = spanText;
let error = 0;
let previousText = '';
let starttime = '';
let started = 0;
let updateWpm = '';
let totalKeyPress = 0;

inputfield.addEventListener('keyup',(event)=>{
    totalKeyPress++;
    let currentText = inputfield.value;
    if(started==0){
        started = 1;
        starttime = new Date().getTime();
        updateWpm = setInterval(()=>{
            currentTime = new Date().getTime();
            speed = (currentTime - starttime)/1000;
            words = inputfield.value.length/5;
            wpm = words/speed*60;
            wpm = parseInt(wpm)
            document.getElementById('wpm').textContent = wpm;
        },1000);
    }
    if(event.getModifierState("CapsLock")){
        // Do restart
        setTimeout(restart,0);
        document.getElementById('caps-lock-on-alert').innerHTML = `
        <div class="alert alert-danger" role="alert">
            You Caps Lock is ON. Please off Caps Lock
        </div>
        `;
        setTimeout(()=>{
            document.getElementById('caps-lock-on-alert').innerHTML = '';
        },5000);
    }
    if(inputfield.value===giventext){
        endtime = new Date().getTime();
        speed = (endtime - starttime)/1000;
        words = inputfield.value.length/5;
        wpm = words/speed*60;
        document.getElementById('wpminput').value =parseInt(wpm);
        document.getElementById('typoinput').value = error;
        clearInterval(updateWpm);
        myForm.submit();
    }

    if((giventext.slice(0,inputfield.value.length)!=inputfield.value) && (previousText.length < currentText.length)){
            error = error + 1;
    }

    let accuracy = parseInt((totalKeyPress-error)/totalKeyPress*100);
    let accuracySpan = document.getElementById('accuracy');
    if(accuracySpan!=null){
        accuracySpan.textContent = accuracy+'%';
    }
    


    let spanList = document.getElementsByClassName("givenLetter")
    let errorFoundAt = -1;
    for(let i=0;i<inputfield.value.length;i++){
        if(spanList[i].textContent==inputfield.value[i] && errorFoundAt==-1){
            spanList[i].className = "givenLetter text-success"
        }
        if(spanList[i].textContent!=inputfield.value[i] && errorFoundAt==-1){
            errorFoundAt = i;
            spanList[i].className = "givenLetter bg-danger text-white rounded";
        }
        if(giventext.slice(0,inputfield.value.length)==inputfield.value && inputfield.value.length<giventext.length){
            spanList[inputfield.value.length].className = "givenLetter bg-success text-white rounded"
        }
    }


    previousText = currentText;
    let typoSpan = document.getElementById('typo')
    if(typoSpan!=null){
        document.getElementById('typo').textContent = error;
    }
      
})

// Do restart when copy paste occours
inputfield.addEventListener('paste',()=>{
    // Do restart
    setTimeout(restart,0)
    // restart();
    document.getElementById('copy-paste-alert').innerHTML = `
    <div class="alert alert-danger" role="alert">
    Please do not paste any text.
    </div>
    `;
    setTimeout(()=>{
        document.getElementById('copy-paste-alert').innerHTML = '';
    },5000);
})

function restart(){
    clearInterval(updateWpm);
    error = 0;
    previousText = '';
    starttime = '';
    started = 0;
    updateWpm = '';
    document.getElementById('wpm').textContent = '';
    let typoSpan = document.getElementById('typo');
    let accuracySpan = document.getElementById('accuracy');
    if(typoSpan!=null){
        document.getElementById('typo').textContent = '';
    }
    if(accuracySpan!=null){
        document.getElementById('accuracy').textContent = '';
    }
    document.getElementById('inputfield').value = '';
    let letterList = document.getElementsByClassName("givenLetter")
    for(let i=0;i<letterList.length;i++){
        letterList[i].className = "givenLetter";
        console.log(letterList[i].textContent)
    }
}

document.getElementById('btn-restart').addEventListener('click',restart);