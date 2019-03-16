var questionElt = document.getElementById("question")

questionElt.addEventListener('keypress', (event) =>{
    keyName = event.key;
    if (keyName === "Enter") {
        event.preventDefault()
        input_data = {

            data : questionElt.value
        }
        data = JSON.stringify(input_data);

        ajaxPost("/user_question", data, function(reponse){
            console.log("Requete envoyée " + reponse + " !");
        } )

        var divElt = document.createElement("div");
        divElt.className = "user-conversation";
        var paraElt = document.createElement("p");
        paraElt.textContent = questionElt.value;
        var asso = divElt.appendChild(paraElt);
        document.getElementById("chat").appendChild(asso).className = "user-conversation";
        questionElt.value = "";

        var divElt2 = document.createElement("div")
        var paraElt2 = document.createElement("p");
        paraElt2.textContent = "Ah je vois...Laisse moi quelques secondes pour me souvenir";
        var asso2 = divElt.appendChild(paraElt2);
        document.getElementById("chat").appendChild(asso2).className = "grandpy_react";

        divElt3 = document.createElement("div");
        document.getElementById("chat").appendChild(divElt3).className = "map";

    }
});




/* document.querySelector().addEventListener('keypress', function (e) {
    var key = e.which || e.keycode;
    if (key === 13) {
        console.log("test touche entrée");
        ajaxGet()
    }
}); */