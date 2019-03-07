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

        document.getElementById("start_convers")
    }
});




/* document.querySelector().addEventListener('keypress', function (e) {
    var key = e.which || e.keycode;
    if (key === 13) {
        console.log("test touche entrée");
        ajaxGet()
    }
}); */