inputfield = document.getElementById('inputfield');
giventext = document.getElementById('giventext').textContent;
myForm = document.getElementById('myForm');

let error = 0;
let previousText = '';
let starttime = '';
let started = 0;
let updateWpm = '';
inputfield.addEventListener('keyup',(event)=>{
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
    previousText = currentText;
    document.getElementById('typo').textContent = error;
      
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
    document.getElementById('typo').textContent = '';
    document.getElementById('inputfield').value = '';

    
}

document.getElementById('btn-restart').addEventListener('click',restart);