var fName = null;
var lName = null;
var age = 0;
var height = 0
var petName = null;

var fName = prompt("Please enter your first name:")
var lName = prompt("Please enter your last name:")
var age = prompt("Please enter your age:")
var height = prompt("Please enter your heigh in centimters:")
var petName = prompt("Please enter your pet's name:")
var petNameLength = petName.length -1

if (fName[0] == lName[0] && age < 30 && age > 20 && height > 170 && petName[petNameLength] == "y") {
    console.log("Top secret message");
}