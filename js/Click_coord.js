//<script id="Координаты клика">
function printMousePos(event) {
    document.getElementsByClassName("crds")[0].innerHTML = "X: " + event.clientX + "Y: " + event.clientY;
    //document.getElementsById("_2").style.margin = event.clientY + 'px ' + ' 0px ' + ' 0px ' + event.clientX + 'px' ;
}

document.addEventListener("click", printMousePos);

//</script>