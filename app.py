import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Nokia Snake", layout="centered")

st.title("🐍 Nokia Snake Game")
st.write("Use Arrow Keys to Play!")

snake_game = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    overflow: hidden;
    background-color: #111;
}

canvas {
    display: block;
    margin: auto;
    background-color: black;
}
</style>
</head>
<body>

<canvas id="game" width="400" height="400"></canvas>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

const grid = 20;
let count = 0;
let score = 0;

let snake = {
    x: 160,
    y: 160,
    cells: [],
    maxCells: 4,
    dx: grid,
    dy: 0
};

let apple = {
    x: 320,
    y: 320
};

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max-min)) + min;
}

function loop() {
    requestAnimationFrame(loop);

    if (++count < 6) return;
    count = 0;

    ctx.clearRect(0,0,canvas.width,canvas.height);

    snake.x += snake.dx;
    snake.y += snake.dy;

    // wall wrap (classic Nokia feel)
    if (snake.x < 0) snake.x = canvas.width - grid;
    else if (snake.x >= canvas.width) snake.x = 0;

    if (snake.y < 0) snake.y = canvas.height - grid;
    else if (snake.y >= canvas.height) snake.y = 0;

    snake.cells.unshift({x: snake.x, y: snake.y});

    if (snake.cells.length > snake.maxCells) {
        snake.cells.pop();
    }

    // draw apple
    ctx.fillStyle = "red";
    ctx.fillRect(apple.x, apple.y, grid-1, grid-1);

    // draw snake
    ctx.fillStyle = "#00ff88";
    snake.cells.forEach(function(cell, index) {

        ctx.fillRect(cell.x, cell.y, grid-1, grid-1);

        // eating apple
        if (cell.x === apple.x && cell.y === apple.y) {
            snake.maxCells++;
            score++;

            apple.x = getRandomInt(0,20) * grid;
            apple.y = getRandomInt(0,20) * grid;
        }

        // self collision
        for (let i = index + 1; i < snake.cells.length; i++) {
            if (cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {

                snake.x = 160;
                snake.y = 160;
                snake.cells = [];
                snake.maxCells = 4;
                snake.dx = grid;
                snake.dy = 0;
                score = 0;
            }
        }
    });

    // Score
    ctx.fillStyle = "white";
    ctx.font = "16px Arial";
    ctx.fillText("Score: " + score, 10, 20);
}

document.addEventListener("keydown", function(e) {

    if (e.which === 37 && snake.dx === 0) {
        snake.dx = -grid;
        snake.dy = 0;
    }
    else if (e.which === 38 && snake.dy === 0) {
        snake.dy = -grid;
        snake.dx = 0;
    }
    else if (e.which === 39 && snake.dx === 0) {
        snake.dx = grid;
        snake.dy = 0;
    }
    else if (e.which === 40 && snake.dy === 0) {
        snake.dy = grid;
        snake.dx = 0;
    }
});

requestAnimationFrame(loop);
</script>

</body>
</html>
"""

components.html(snake_game, height=420)
