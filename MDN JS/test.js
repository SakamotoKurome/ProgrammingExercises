const canvas = document.querySelector('.myCanvas');
const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;
const ctx = canvas.getContext('2d');

ctx.translate(width / 2, height / 2);
const image = new Image();
image.src = './walk-right.png';
image.onload = draw;
let sprite = 0;
let posX = 0;
function draw() {
    ctx.fillRect
}