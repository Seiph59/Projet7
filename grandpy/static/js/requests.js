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

        var enter = true;
        if (enter == true);
            var divElt = document.createElement("div");
            var paraElt = document.createElement("p");
            paraElt.className = "user-conversation";
            paraElt.textContent = questionElt.value;
            var asso = divElt.appendChild(paraElt)
            document.getElementById("chat").appendChild(asso);
            enter = false;
    }
});




/* document.querySelector().addEventListener('keypress', function (e) {
    var key = e.which || e.keycode;
    if (key === 13) {
        console.log("test touche entrée");
        ajaxGet()
    }
}); */