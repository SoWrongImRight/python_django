var ham = 00;
var cheese = 0;

var report = "blank";

if (ham >= 10 && cheese >= 10) {
    report = "Strong sales of hame and cheese."
}else if (ham === 0 && cheese === 0){
    report = "Nothing sold"
}else {
    report = "We had some sale of products"
}

console.log(report);