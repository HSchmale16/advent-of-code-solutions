const fs =require('fs');
const readline = require('readline');
const ohm = require('ohm-js');


const readIface = readline.createInterface({
    input: process.stdin,
    console: false
});

const myGrammar = ohm.grammar(fs.readFileSync("test3.ohm"));

var count = 0;
readIface.on('line', (line) => {
    line = line.trim();
    var m = myGrammar.match(line, "A0");
    if (m.succeeded()) {
        console.log(line)
        ++count;
    } else {
    
    }
});

readIface.on('close', () => {
    console.log(count);
})