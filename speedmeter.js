//Wordlist contains the words
//textShow contains the giver line html
//input id='parc' contains the userinput
//textCheck contains the given line

let spanList = document.getElementById('spanList-pre').children;
let wordsX60 = textCheck.length / 5 * 60;
let error = 0;
let prevLen = 0;
let prevState = 1;
let startTime;
let started = 0;
let endTime;
let ended = 0;
let timeTaken;
let wpm;
let errorObj = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"~":0,"`":0,"!":0,"@":0,"#":0,"$":0,"%":0,"^":0,"&":0,"*":0,"(":0,")":0,"_":0,"+":0,"-":0,"=":0,"|":0,"}":0,"\\":0,"]":0,"[":0,";":0,"\'":0,'"':0,":":0,"<":0,">":0,"?":0,"/":0,".":0,",":0," ":0,"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
$((document) => {
    $('#parc').focus()
})
document.getElementById('parc').addEventListener('keyup',function(e)  {
    if(e.getModifierState('CapsLock')){
        document.getElementById('parc').disabled = true;
        restart();
    }
    if (started == 0) {
        startTime = Date.now();
        started = 1;
        // console.log('started');
    }
    let x = e.target.value.split(' ');
    let inputList = [];
    for (let i = 0; i < x.length; i++) {
        inputList.push(x[i]);
        if (i + 1 != x.length) {
            inputList.push(' ');
        }
    }
    // console.clear();
    // console.log(inputList);
    let cst = -1, ps = 0;
    for (i = 0; i < spanList.length; i++) {
        if (inputList[i] == spanList[i].textContent) {
            cst++;
            ps = cst + 1;
        }
        else {
            break;
        }
    }
    // console.log(cst, ps);
    for (let i = 0; i <= cst; i++) {
        spanList[i].className = 'success'
    }
    let wordTillNow = inputList[ps];
    if (wordTillNow != undefined && spanList[ps] != undefined) {

        let wordLengthTillNow = wordTillNow.length;
        // console.log(wordTillNow, spanList[ps].textContent.slice(0, wordLengthTillNow))
        if (wordTillNow == spanList[ps].textContent.slice(0, wordLengthTillNow)) {
            if (inputList[ps + 1] != undefined) {
                spanList[ps].className = 'active-danger'
            }
            else {
                spanList[ps].className = 'active-success'
            }
        }
        else if (wordTillNow != spanList[ps].textContent.slice(0, wordLengthTillNow)) {
            spanList[ps].className = 'active-danger'
        }
    }
    for (let i = ps + 1; i < spanList.length; i++) {
        spanList[i].className = '';

    }

    let inputLine = e.target.value;
    let currentLen = inputLine.length;
    let piece = textCheck.slice(0, currentLen);
    // console.log(inputLine, piece);
    if (piece != inputLine && prevState == 1) {
        prevState = 0;
        error++;
        let errorChar = piece[piece.length-1];
        errorObj[errorChar]++;
        console.log(errorChar)
        // console.log('inside if')
    }
    else if (piece != inputLine && prevState == 0) {
        prevState = 0;
        if (currentLen > prevLen) {
            error++;
        }
    }
    else {
        prevState = 1;
    }
    prevLen = currentLen;
    document.getElementById('error').textContent = error;   //Error detected here done

    let correctChars = 0;
    for (let i = 0; i < inputLine.length; i++) {
        if (inputLine[i] == textCheck[i]) {
            correctChars++;
        }
    }
    let correctWordsX60 = correctChars / 5 * 60;
    let currentWPM = parseInt(correctWordsX60 / ((Date.now() - startTime) / 1000));
    // console.log(currentWPM);
    document.getElementById('wpm').textContent = currentWPM;

    if (textCheck == inputLine) {
        ended = 1;
        endTime = Date.now();
        timeTaken = (endTime - startTime) / 1000;
        wpm = parseInt(wordsX60 / timeTaken);
        console.log(errorObj)
        document.getElementById('parc').disabled = 'true';
        
    }
})

$('#restart').click(restart);

function restart() {
    error = 0;
    prevLen = 0;
    prevState = 1;
    started = 0;
    ended = 0;
    document.getElementById('parc').value = '';
    $('#parc').focus()
    document.getElementById('parc').disabled = false;
    // document.getElementById('parc').setAttribute('disabled','false')
    // console.log("present value", document.getElementById('parc').value);
    document.getElementById('wpm').textContent = "";
    document.getElementById('error').textContent = "";
    $("#parc").focus();
    let spanList = document.getElementById('spanList-pre').children;

    for (span of spanList) {
        span.className = '';
    }
    inputLine = '';
}