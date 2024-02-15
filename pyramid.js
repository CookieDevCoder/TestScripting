const size = 50
var finaltext = ""
for (var i = 0; i < size; i++) {
    for(var s = size - i + 1; s > 0; s--) {
        finaltext += " ";
    }
    for(var d = 1 + (2*i); d > 0; d--) {
        finaltext += "*";
    }
    finaltext += "\n";
}
console.log(finaltext);