//get all keys
const keys = document.querySelectorAll('.key')
//play notes
function playNotes(evento){
    //keyCode
    let audioKeyCode = getKeyCode(evento);
    //tecla digitada
    const key = document.querySelector(`.key[data-key="${audioKeyCode}"]`)
    console.log(key)
    //if key exist
    const isKeyExist = key
    if(!isKeyExist){
    return;
    }
    //play audio

    const audio = document.querySelector(`audio["data-key${audioKeyCode}"]`)
    audio.currentTime = 0;
    audio.play()
}

function getKeyCode(evento){
    let keyCode;
    const isKeyboard = evento.type === 'keydown'

    if(isKeyboard){
        keyCode = evento.keyCode
    }else{
        keyCode = evento.target.dataset.key;
    }

    console.log(evento.type)
    console.log(keyCode)
    return keyCode
}

//click with mouse

keys.forEach((tecla) =>{
    tecla.addEventListener("click", playNotes)
})
//keyboard type
window.addEventListener("keydown", playNotes)