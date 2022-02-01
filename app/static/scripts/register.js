let popup = document.querySelector('#popup');
showDiv = () => {
    popup.style.visibility="visible";
}


hideDiv = () => {
    popup.style.visibility="hidden";
}

showDiv();

setTimeout("hideDiv()", 1500);