
//get element by id
function getE(id) {
    return document.getElementById(id)
}

//show or hide element by id
function showHide(id) {
    var element = getE(id);
    if (element.style.display == 'none') {return element.style.display = 'block'}
    else {element.style.display = 'none'}
}


function init () {

    getE('intro').addEventListener('click', showHide('intro'))


}

document.addEventListener("DOMContentLoaded", init);
