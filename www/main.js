$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn'
        },
        out: {
            effect: 'bounceOut'
        }
    });

    // this is for waves search siriwaves on google click on first link
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.30
    });

    // this is for text animation
    $('.siri-msg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync: true
        },
        out: {
            effect: 'fadeOutRight',
            sync: true
        }
    });

});


// mic btn click event handle by jquery
$("#MicBtn").click(function () {
    $("#oval").attr("hidden", true);
    $("#SiriWaves").attr("hidden", false);
    eel.allCommands()();
});


function doc_keyUp(e) {
    if (e.key === 'j' && e.metaKey) {
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#SiriWaves").attr("hidden", false);
        eel.allCommands()();
    }
}


// this fucntion took message from the text field and show send btn
function PlayAssistant(message) {
    if (message != "") {

        $("#oval").attr("hidden", true);
        $("#SiriWaves").attr("hidden", false);

        eel.allCommands(message)();   // fixed

        $("#chatbox").val("");
        $("#MicBtn").attr("hidden", false);
        $("#SendBtn").attr("hidden", true);
    }
}

function ShowHiddenButton(message){
    if(message.length == 0){
        $("MicBtn").attr("hidden",false);
        $("SendBtn").attr("hidden",true);   
    }
    else{
        $("MicBtn").attr("hidden",true);
        $("SendBtn").attr("hidden",false);
    }
}

ShowHiddenButton("helel")

// correct event name
document.addEventListener('keyup', doc_keyUp, false);