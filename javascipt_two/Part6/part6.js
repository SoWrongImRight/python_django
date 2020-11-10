var employee ={
    name:"John Smith",
    job:"Programmer",
    age:31,
    nameLength : function(){
        console.log(this.name.length);
    },
    lastName:function(){
        var lname = this.name.split(' ');
        console.log(lname[1]);
    }
}
employee.nameLength();

/* 
for (i in employee){
    alert(employee[i])
}
*/
employee.lastName();
