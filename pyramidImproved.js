const size = 10
var finaltext = ""
for (var i = 1; i <= size; i++) {
    for (var j = 0; j < size + i + 1; j++) {
        finaltext += (j > size - i + 1) ? "*" : " ";
    }
    finaltext += "\n";
}
console.log(finaltext);