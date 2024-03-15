const body = document.querySelector("body");
const btnToggleSwitch = document.querySelector(".toggle-switch");
const icon = document.querySelector("#icon");
// const sun = document.querySelector("#sun");
// const moon = document.querySelector("#moon");

btnToggleSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");            

    if(body.className == "dark"){
        icon.classList.remove("sun", "bx-sun")
        icon.classList.add("moon", "bx-moon")
    }else{
        icon.classList.remove("moon", "bx-moon")
        icon.classList.add("sun", "bx-sun")
    }

})


