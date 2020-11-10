// restart game button

var restart = document.querySelector("#b")

// grab all squares

var squares = document.querySelectorAll("td")

// clear all squares

function clearBoard() {
    for (i in squares){
        squares[i].textContent = '';
    }
    
}

restart.addEventListener("click", clearBoard);

// for loop to add eventlisteners

/*
var topleft = document.querySelector('#tl')

topleft.addEventListener('click', function(){
    if (topleft.textContent === ""){
        topleft.textContent = "X"
    }else if (topleft.textContent === "X"){
        topleft.textContent = "O"
    }else{
        topleft.textContent = ""
    }
})
*/

function changeMarker() {
    if(this.textContent===""){
        this.textContent="X";
    }else if(this.textContent==="X"){
        this.textContent="O";
    }else{
        this.textContent="";
    }
}

for (i=0; i < squares.length; i++){
    squares[i].addEventListener('click',changeMarker);
}


    
