const fs = require ('fs');

let grid = fs.readFileSync (process.argv[2], 'utf8').split ('\n');
let height = grid.length;
let width = grid.map (a => a.length).reduce ((a, b) => Math.max(a, b))

grid = grid.map(a => {
    let z = Array(width).fill(' ');
    a.split('').forEach((v, i) => z[i] = v);
    return z;
});
console.log(grid);

let x = 0, y = 0, dx = 0, dy = 1;
let str = '';
let path_chars = ['-', '|'];
let count = 0;

x = grid[0].indexOf ('|');

while (true) {
    if (grid[y][x] === '+') {
        // Search Left and Right
        if (dx === 0) {
            // Going Up and Down
            if (grid[y][x - 1] !== ' ') {
                dx = -1;
            } else {
                dx = 1;
            }
            dy = 0;  
        } else {
            // Going Left Or Right
            if (grid[y - 1][x] !== ' ') {
                dy = -1;
            } else {
                dy = 1;
            }
            dx = 0;
        }
    } else if (grid[y][x] === ' ') {
        break;
    } else if (!path_chars.includes(grid[y][x])) {
        str += grid[y][x];
    }
    x += dx;
    y += dy;
    if (x < 0 || x >= width)
        break;
    if (y < 0 || y >= height)
        break;
    ++count;
}
console.log(str);
console.log(count)
