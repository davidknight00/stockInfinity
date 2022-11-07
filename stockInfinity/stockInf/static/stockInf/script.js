function makeNavResponsive() {
    var nav = document.getElementById("myNavbar");
    if(nav.className === "navbar") {
        nav.ClassName += " responsive";
    }
    else {
        nav.ClassName = "navbar";
    }
}
