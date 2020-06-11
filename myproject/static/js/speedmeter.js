inputfield = document.getElementById('inputfield');
giventext = document.getElementById('giventext').textContent;
myForm = document.getElementById('myForm');
function flashKey(event){
    let item = document.getElementById(event.code);
    if(item!=null){
    let id = document.getElementById(event.code).id;
    if(id=='Backspace'){
            item.className = `col-2 border m-1 key d-flex flex-column bg-success text-white`;
            setTimeout(()=>{
                item.className = `col-2 border m-1 key d-flex flex-column`;
            },200);
        }else if(id=='Space'){
            item.className = `col-6 border m-1 key d-flex flex-column bg-success text-white`;
            setTimeout(()=>{
                item.className = `col-6 border m-1 key d-flex flex-column`;
            },200);
        }
        else{
            item.className = `col border m-1 key d-flex flex-column bg-success text-white`;
            setTimeout(()=>{
                item.className = `col border m-1 key d-flex flex-column`;
            },200);
        }
    }
    
}

let weakkeys = {"97": 0, "98": 0, "99": 0, "100": 0, "101": 0, "102": 0, "103": 0, "104": 0, "105": 0, "106": 0, "107": 0, "108": 0, "109": 0, "110": 0, "111": 0, "112": 0, "113": 0, "114": 0, "115": 0, "116": 0, "117": 0, "118": 0, "119": 0, "120": 0, "121": 0, "122": 0, "65": 0, "66": 0, "67": 0, "68": 0, "69": 0, "70": 0, "71": 0, "72": 0, "73": 0, "74": 0, "75": 0, "76": 0, "77": 0, "78": 0, "79": 0, "80": 0, "81": 0, "82": 0, "83": 0, "84": 0, "85": 0, "86": 0, "87": 0, "88": 0, "89": 0, "90": 0, "96": 0, "49": 0, "50": 0, "51": 0, "52": 0, "53": 0, "54": 0, "55": 0, "56": 0, "57": 0, "48": 0, "45": 0, "61": 0, "126": 0, "33": 0, "64": 0, "35": 0, "36": 0, "37": 0, "94": 0, "38": 0, "42": 0, "40": 0, "41": 0, "95": 0, "43": 0, "91": 0, "93": 0, "123": 0, "125": 0, "124": 0, "59": 0, "39": 0, "58": 0, "34": 0, "44": 0, "46": 0, "47": 0, "60": 0, "62": 0, "63": 0}
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
let accuracy = '100%';
inputfield.addEventListener('keydown',function(event){
    flashKey(event);
})
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
        if(document.getElementById('accuracyinput')!=null){
            document.getElementById('accuracyinput').value = accuracy;
        }
        weakstring = '{';
        Object.keys(weakkeys).forEach((val)=>{
            weakstring += `"${val}":${weakkeys[val]},`
        })
        weakstring = weakstring.slice(0,weakstring.length-1) + '}'
        document.getElementById('weakkeys').value = weakstring
        console.log(accuracy);
        clearInterval(updateWpm);
        myForm.submit();
    }

    if((giventext.slice(0,inputfield.value.length)!=inputfield.value) && (previousText.length < currentText.length)){
            error = error + 1;
    }

    // console.log(giventext.slice(0,previousText.length));
    // console.log(previousText);
    // console.log(giventext.slice(0,currentText.length));
    // console.log(currentText);
    if(giventext.slice(0,previousText.length)==previousText && giventext.slice(0,currentText.length)!=currentText){
        let ch = giventext[currentText.length-1];
        let asci = ch.charCodeAt()
        weakkeys[asci]++;
    }

    accuracy = parseInt((totalKeyPress-error)/totalKeyPress*100);
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
    for(let i = inputfield.value.length+1;i<giventext.length;i++){
        spanList[i].className = "givenLetter";
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