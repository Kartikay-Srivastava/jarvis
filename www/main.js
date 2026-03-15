
$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounceIn',  // correct case
        },
        out: {
            effect: 'bounceOut'  // correct case
        }
    });

    // this is for waves seach siriwaves on google click on first link
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style:"ios9",
    amplitude:"1",
    speed:"0.30",
  });

//   this is for text animation
$('.siri-msg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'fadeInUp',
            sync:true  // correct case
        },
        out: {
            effect: 'fadeOutRight',
            sync:true  // correct case
        }
    });
});

// mic btn click event handle by jquery

$("#MicBtn").click(function () { 
    // your code here
    // eel.playAssistantSound(); //just checking mic 
    $("#oval").attr("hidden", true); //jquery set attertibute
    $("#SiriWaves").attr("hidden", false); //jquery set attertibute
    eel.takecommand()()
});