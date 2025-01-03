function toggleLeftNavBar(btn){
    containers = document.getElementsByClassName('left-nav-container');

    if(btn.innerHTML == "&lt;"){
        [...containers].forEach(function(container, i){
            container.style.display = "none";
        });

        navLeft.style.gridTemplateColumns = "0 24px";
        navLeft.style.width = "24px";
        navLeft.style.paddingLeft = "0";

        mainBlock.style.gridTemplateColumns = "32px auto";
        // animate(200);
        
        btn.innerHTML = "&gt;";
    }
    else {
        [...containers].forEach(function(container, i){
            container.style.display = "";
        });

        navLeft.style.gridTemplateColumns = "";
        navLeft.style.width = "";
        navLeft.style.paddingLeft = "";

        mainBlock.style.gridTemplateColumns = "";
        
        btn.innerHTML = "&lt;";
    }
}

function animate(duration) {

    let start = Date.now(); // запомнить время начала

    let timer = setInterval(function() {
        // сколько времени прошло с начала анимации?
        let timePassed = Date.now() - start;

        if (timePassed >= duration) {
            clearInterval(timer); // закончить анимацию через 2 секунды
            return;
        }
        
        [...document.getElementsByClassName('left-nav-container')].forEach(function(container, i){
            container.style.opacity = (100 - 120 * timePassed / duration) + "%";});
        mainBlock.style.gridTemplateColumns = (220 - 170 * timePassed / duration) + "px auto";
        navLeft.style.gridTemplateColumns = (200 - 200 * timePassed / duration) + "px 20px";
        navLeft.style.width = (220 - 200 * timePassed / duration) + "px";
    }, 10);
}