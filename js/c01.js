var fs = require("fs");
fs.readFile("./mytext.txt", function(text){
    var textByLine = text.split("\n")
});

document.write('<h3>' + textByLine + '</h3>');