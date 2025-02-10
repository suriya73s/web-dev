var pop = document.getElementById("pop")

function savefun() {
    var tittle = document.getElementById("tittle")
    var author = document.getElementById("author")
    var textarea = document.getElementById("text-content")

    var divE = document.createElement("div")
    var h3E = document.createElement("h3")
    var h4E = document.createElement("h4")
    var pE = document.createElement("p")
    document.querySelector(".container").insertAdjacentElement("beforeend", divE)

    h3E.textContent = tittle.value;
    h4E.textContent = author.value;
    pE.textcontent = textarea.value;

    divE.innerHTML = `<h3>${tittle.value}</h3>
    <h4>${author.value}</h4>
    <p>${textarea.value}</p>
    <button class="save-bt" onclick="deletefun(event)">Delete</button>`;


    pop.style.display = "none"
    tittle.value = "";
    author.value = "";
    textarea.value = "";

}

function add() {
    pop.style.display = "block";

}

function deletefun(event) {
    event.target.parentElement.remove();
}