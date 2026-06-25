function animateValue(id,end){

    let count=0;

    let speed=Math.ceil(end/100);

    let interval=setInterval(function(){

        count += speed;

        document.getElementById(id).innerText =
        count + "+";

        if(count >= end){

            document.getElementById(id).innerText =
            end + "+";

            clearInterval(interval);
        }

    },20);
}

window.onload = function(){

    animateValue("users",5000);

    animateValue("items",12000);

    animateValue("sales",8000);
}