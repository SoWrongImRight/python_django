var studentRoster = []

start = prompt("Start roster program? ");
if (start == "yes"){
    main();
}
else{
   // break
}

function main() {
    choice = prompt("Choose your action:  add, remove display, or quit")
    if (choice == "add"){
        name = prompt("Enter name to add: ");
        addName(name);
    }else if(choice == "remove"){
        name = prompt("Enter Name to remove: ");
        removeName(name);
    }else if(choice == "display"){
        displayRoster();
    }else if(choice == "quit"){
        // break //
    }
}

function addName(name) {
    studentRoster.push(name);
    console.log("Added "+ name +" to the roster.");
    main();    
}

function removeName(name){
    //for (i =0; i < studentRoster.length; i++){
        // if (studentRoster[i] == name){
        //    studentRoster.splice[i,1];
        //    i--;
        //       console.log("Removed "+ name +" from the roster.");
    //    }
    //}
    var nameIndex = studentRoster.indexOf(name);
    studentRoster.splice(nameIndex,1);
    console.log("Removed "+name+" from the roster.");
    main();
}

function displayRoster() {
    studentRoster.forEach(console.log);
    main();
}
