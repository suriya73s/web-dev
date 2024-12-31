var sidenav = document.getElementById("sidenavi");
var menu = document.querySelector(".menu");
var menucross = document.querySelector(".menucross");

function menuclick()
{ 
    if(sidenav.style.width === "0px")
        {
            sidenav.style.width = "180px"; 
            menu.style.display = "none";
            menucross.style.display = "inline-block";
        }
        else
        {
            sidenav.style.width = "0px" 
            menu.style.display = "inline-block";
            menucross.style.display = "none";
        }
   
}

function handlesize()
{
    if (window.innerWidth > 770) 
        { sidenav.style.width = "0px" 
            menu.style.display = "none";
            menucross.style.display = "none";
     }
     else {
        if(sidenav.style.width == "0px")
            {
             menu.style.display = "inline-block";
            }
        }
}
window.addEventListener('resize',handlesize);
handlesize();

var scroll = new SmoothScroll('a[href*="#"]', {
	speed: 500,
	speedAsDuration: true
});