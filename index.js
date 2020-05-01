//Bring this wordlist through a get request
let wordList = ['India', 'is','a','very','great','country.'];

//Prepare the text to show on the screen and the text to check every now and then
let textShow = '<pre class="styletext" id="spanList-pre">';
let textCheck = '';
for(let i =0;i<wordList.length;i++){
    textShow += `<span>${wordList[i]}</span>`;
    textCheck += wordList[i];
    if(i+1<wordList.length && (wordList[i+1]!=',' && wordList[i+1]!='.')){
        textShow +=  `<span> </span>`
        textCheck +=  ' ';
    }
}
textShow += `</pre>`;
// console.log(textShow)
document.getElementById('exText').innerHTML=textShow;

//Dismiss the error messsage. Do it through jQuery
document.getElementById('close-btn').addEventListener('click',()=>{
    // document.getElementsByClassName('errorMsg')[0].style.display = 'none';
    // document.getElementsByClassName('errorMsg')[1].style.display = 'none';
    $('.errorMsg').fadeOut(1000);
});
