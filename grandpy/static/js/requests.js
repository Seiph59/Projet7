var questionElt = document.getElementById("question")

function user_chat_and_automatic_response(){
    var divElt = document.createElement("div");
    divElt.className = "user-conversation";
    var paraElt = document.createElement("p");
    paraElt.textContent = questionElt.value;
    var asso = divElt.appendChild(paraElt);
    document.getElementById("chat").appendChild(asso).className = "user-conversation";
    questionElt.value = "";

    var divElt2 = document.createElement("div");
    divElt2.className = "grandpy_react";
    var paraElt2 = document.createElement("p");
    paraElt2.textContent = "Ah je vois...Laisse moi quelques secondes pour me souvenir";
    var asso2 = divElt.appendChild(paraElt2);
    document.getElementById("chat").appendChild(asso2).className = "grandpy_react";
}

function display_loader(){
    var getId = document.getElementById("loader");
    getId.style.visibility = "visible";
}

function hide_loader(){
    var getId = document.getElementById("loader");
    getId.style.visibility = "hidden";
}

function question_grandpy_wiki(){
    var divElt = document.createElement("div");
    var pElt= document.createElement("p");
    pElt.textContent = "Mais t'ai-je déjà parlé de l'histoire de ce quartier ?";

    document.getElementById("chat").appendChild(divElt).className = "grandpy_react";
    divElt.appendChild(pElt);
}

function grandpy_response_wiki(input){
    var divElt = document.createElement("div");
    var pElt= document.createElement("p");
    pElt.textContent = input[0][0]
    var aElt = document.createElement("a");
    var chat = document.getElementById("chat");
    aElt.href = input[0][1];
    aElt.textContent = "En savoir plus sur Wikipedia";

    chat.appendChild(divElt).className = "grandpy_react";
    divElt.appendChild(pElt);
    divElt.appendChild(aElt);
    chat.scrollTo(0, chat.scrollHeight);
}

function initMap(input_response) {
    var lat = input_response[1][0];
    var lng = input_response[1][1];
    var divElt = document.createElement("div");
    divElt.className = "map";

    document.getElementById("chat").appendChild(divElt);
    var place = {lat: lat, lng: lng};
    var map = new google.maps.Map(
        document.querySelector(".map:last-child"), {zoom: 12, center: place});
    var marker = new google.maps.Marker({position: place, map: map});
    var styleMap = document.querySelector(".map:last-child");
    styleMap.style.height = "300px";
    styleMap.style.width = "100%";
  }

questionElt.addEventListener('keypress', (event) =>{
    keyName = event.key;
    if (keyName === "Enter") {

        event.preventDefault()
        input_data = {

            data : questionElt.value
        }
        data = JSON.stringify(input_data);
        user_chat_and_automatic_response();
        display_loader();
        ajaxPost("/user_question", data, function(response){
            hide_loader();
            var transform = JSON.parse(response);
            initMap(transform);
            question_grandpy_wiki();
            grandpy_response_wiki(transform);
            console.log("Requete envoyée " + transform + " !");
        },
        true);
    }
});

