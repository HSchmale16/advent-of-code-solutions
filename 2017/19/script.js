const fs = require('fs');

let grid = fs.readFileSync(process.argv[2], 'utf8').split('\n');
let width = grid.length;
let height = grid.map(a => a.length).reduce((a, b) => Math.max(a, b))

