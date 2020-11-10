function sleepIn(weekday, vacation) {
    if (weekday == "false" && vacation == "false"){
        return true
    }else if(weekday == "false" || vacation == "true"){
        return true
    }else{
        return false
    }    
}