
function init() {
    document.getElementById("header").addEventListener("click", viewHome);
    document.getElementById("logout").addEventListener("click", logout);


    document.getElementById("renter_maintenance_link").addEventListener("click", renterGetBuildings);



    isManager = window.location.hash == "#view=manager";
    isCanvasser = window.location.hash == "#view=canvasser";
    isSalesPerson = window.location.hash == "#view=salesPerson";
    console.log(window.location.hash);
    viewHome();
}

////// calls init function when DOM loads ////////////
document.addEventListener("DOMContentLoaded", init);


function userListener() {
    console.log(this.responseText);
    window.user = JSON.parse(this.responseText);
    if (user.user_id == "0"){
        window.location = "/login.html";
    }
}

function getUser() {
    xhr = new XMLHttpRequest();
    xhr.onload = userListener;
    xhr.open("get", "/logged_in/", true);
    xhr.send();
}
getUser()


//function statusListener(){
//    console.log(this.responseText);
//    window.statusList = JSON.parse(this.responseText);
//    console.log(statusList);
//    console.log(statusList.length);
//}
//
//function getStatus(){
//    sReq = new XMLHttpRequest();
//    sReq.onload = statusListener;
//    sReq.open("get", "/status/", true);
//    sReq.send();

}

function viewHome(){
    document.getElementById('body').innerHTML = '';
    if (window.location == isCanvasser) {
        showCanvasserView()
    }
    else if (window.location == isSalesPerson) {
        showSalesView()
    }
    else {
        showManagerView()
    }
}

function showCanvasserView() {
    document.getElementById('body').classList.add('canvassView');
}

function showManagerView(){
    document.getElementById('body').classList.add('managerView');
}


function showSalesView() {
    document.getElementById('body').classList.add('salesView');

}



function sendPost(item, url, show) {

    var xhr = new XMLHttpRequest();
    var form_data = new FormData();

    for (var key in item) {
        form_data.append(key, item[key]);
    }
    xhr.onload = show;
    xhr.open("POST", url);    //xhr.open("GET", url);
    xhr.send(form_data)
}
