// 设置画布

const canvas = document.querySelector('canvas');
const ctx = canvas.getContext('2d');
const para = document.querySelector('p');

const width = canvas.width = window.innerWidth;
const height = canvas.height = window.innerHeight;

// 生成随机数的函数

function random(min, max) {
    const num = Math.floor(Math.random() * (max - min)) + min;
    return num;
}

// 生成随机颜色值的函数

function randomColor() {
    const color = 'rgb(' +
        random(0, 255) + ',' +
        random(0, 255) + ',' +
        random(0, 255) + ')';
    return color;
}

// 定义 Shape 类
class Shape {
    constructor(x, y, velX, velY) {
        this.x = x;
        this.y = y;
        this.velX = velX;
        this.velY = velY;
    }
}

// 定义 Ball 类
class Ball extends Shape {
    constructor(x, y, velX, velY, color, size) {
        super(x, y, velX, velY);
        this.color = color;
        this.size = size;
        this.exists = true;
    }

    draw() {
        if (this.exists) {
            ctx.beginPath();
            ctx.fillStyle = this.color;
            ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
            ctx.fill();
        }
    }

    update() {
        if (this.exists) {
            if ((this.x + this.size) >= width) {
                this.velX = -(this.velX);
            }

            if ((this.x - this.size) <= 0) {
                this.velX = -(this.velX);
            }

            if ((this.y + this.size) >= height) {
                this.velY = -(this.velY);
            }

            if ((this.y - this.size) <= 0) {
                this.velY = -(this.velY);
            }

            this.x += this.velX;
            this.y += this.velY;
        }
    }

    collisionDetect() {
        if (this.exists) {
            for (let j = 0; j < balls.length; j++) {
                if (this !== balls[j] && balls[j].exists) {
                    const dx = this.x - balls[j].x;
                    const dy = this.y - balls[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < this.size + balls[j].size) {
                        balls[j].color = this.color = randomColor();
                    }
                }
            }
        }
    }
}

class EvilCircle extends Shape {
    constructor(x, y) {
        super(x, y, 20, 20);
        this.color = 'white';
        this.size = 10;

        window.addEventListener("keydown", (e) => {
            switch (e.key) {
                case "a":
                    this.x -= this.velX;
                    break;
                case "d":
                    this.x += this.velX;
                    break;
                case "w":
                    this.y -= this.velY;
                    break;
                case "s":
                    this.y += this.velY;
                    break;
            }
        });
    }

    draw() {
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = this.color;
        ctx.arc(this.x, this.y, this.size, 0, 2 * Math.PI);
        ctx.stroke();
    }

    checkBounds() {
        if ((this.x + this.size) >= width) {
            this.x -= this.size;
        }

        if ((this.x - this.size) <= 0) {
            this.x += this.size;
        }

        if ((this.y + this.size) >= height) {
            this.y -= this.size;
        }

        if ((this.y - this.size) <= 0) {
            this.y += this.size;
        }
    }

    collisionDetect() {
        for (let j = 0; j < balls.length; j++) {
            if (balls[j].exists) {
                const dx = this.x - balls[j].x;
                const dy = this.y - balls[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.size + balls[j].size) {
                    balls[j].exists = false;
                }
            }
        }
    }
}

let evilBall = new EvilCircle(20, 20);

// 定义一个数组，生成并保存所有的球

let balls = [];

while (balls.length < 25) {
    const size = random(10, 20);
    let ball = new Ball(
        // 为避免绘制错误，球至少离画布边缘球本身一倍宽度的距离
        random(0 + size, width - size),
        random(0 + size, height - size),
        random(-7, 7),
        random(-7, 7),
        randomColor(),
        size
    );
    balls.push(ball);
}

// 定义一个循环来不停地播放

function loop() {
    ctx.fillStyle = 'rgba(0,0,0,0.25)';
    ctx.fillRect(0, 0, width, height);

    for (let i = 0; i < balls.length; i++) {
        balls[i].draw();
        balls[i].update();
        balls[i].collisionDetect();
        evilBall.draw();
        evilBall.checkBounds();
        evilBall.collisionDetect();
    }
    para.textContent = balls.filter((item) => item.exists).length

    requestAnimationFrame(loop);
}

loop();