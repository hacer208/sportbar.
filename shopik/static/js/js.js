function openNav() {
    if (window.screen.width < 800){
        document.getElementById("mySidenav").style.width = "100%";
    }
    else {
        document.getElementById("mySidenav").style.width = "250px";
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
