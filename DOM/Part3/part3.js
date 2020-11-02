var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

headOne.addEventListener('mouseover', function (){
    headOne.textContent = 'Mouse Currently Over';
    headOne.style.color = 'red';    
})

headOne.addEventListener('mouseout', function(){
    headOne.textContent = "Hover over me"
    headOne.style.color = "black"
})

headTwo.addEventListener('click',function() {
    headTwo.textContent = "You clicked me!"
    headTwo.style.color = "Blue"    
})

headThree.addEventListener('dblclick', function(){
    headThree.textContent = "Double clicked"
    headThree.style.color = 'red'
})