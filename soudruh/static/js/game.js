const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const board = document.getElementById("gameboard");
const fig = document.getElementById("fig");

const a = 200 // velikost pole

const fig_h = a - 30; // výška figurky
const fig_w = (fig_h / fig.height) * fig.width // šířka figurky podle její výšky
const fig_av = 15; // odstup figurky od vrchu
const fig_ah = (a - fig_w) / 2 //šířka pole mínus šířka figurky děleno dvěma = odstup figurky zleva

const canvasWidth = 27 * a;
const canvasHeight = 20 * a;
canvas.width = canvasWidth;
canvas.height = canvasHeight;

const camera = {
    x: 0,
    y: 0,
    zoom: 1,
    zoomSpeed: 0.1,
    moveSpeed: 50,
    maxZoom: 2,
    minZoom: 1,
};

let isMouseOverCanvas = false;
let isDragging = false;
let lastMousePos = {
    x: 0,
    y: 0
};

function drawPlayers(ctx) {
    try {
        PLAYERS.forEach((player) => {
            // Create an off-screen canvas to manipulate the image
            const offscreenCanvas = document.createElement('canvas');
            const offscreenCtx = offscreenCanvas.getContext('2d');

            // Draw the image onto the offscreen canvas
            offscreenCanvas.width = fig.width;
            offscreenCanvas.height = fig.height;
            offscreenCtx.drawImage(fig, 0, 0);

            // Get image data from the offscreen canvas
            const imageData = offscreenCtx.getImageData(0, 0, fig.width, fig.height);
            const data = imageData.data;

            // Convert the player's color (hex) to RGB
            const hexColor = player.color; // Assuming player.color is in hex (e.g., "#FF5733")
            const r = parseInt(hexColor.substring(1, 3), 16);
            const g = parseInt(hexColor.substring(3, 5), 16);
            const b = parseInt(hexColor.substring(5, 7), 16);

            // Loop through the image data and apply the tint
            for (let i = 0; i < data.length; i += 4) {
                // Get the grayscale value (average of the RGB values)
                const grayscale = 0.3 * data[i] + 0.59 * data[i + 1] + 0.11 * data[i + 2];

                // Blend the grayscale with the player's color
                data[i] = Math.min(255, grayscale + (r - 128)); // Red
                data[i + 1] = Math.min(255, grayscale + (g - 128)); // Green
                data[i + 2] = Math.min(255, grayscale + (b - 128)); // Blue
            }

            // Put the modified image data back onto the offscreen canvas
            offscreenCtx.putImageData(imageData, 0, 0);

            // Draw the manipulated image onto the main canvas
            drawFigOnBoard(player, offscreenCanvas);
        });

    } catch {
        console.log('loading PLAYERS');
    }
}

function drawFigOnBoard(player, offscreenCanvas) {
    const pindex = player.pindex;
    let x = 15;
    let y = 10;
    let rot = 1;

    // Calculate the width and height of the player's name
    const nameText = player.name.charAt(0).toUpperCase() + player.name.slice(1);
    ctx.font = "70px Arial"; // Set the font for the name text
    ctx.textAlign = "center"; // Align the text to be centered
    ctx.textBaseline = "bottom"; // Position the text above the figure
    ctx.fillStyle = 'white';

    // Set the drop shadow properties
    ctx.shadowColor = "rgba(0, 0, 0, 1)"; // Shadow color (black with some transparency)
    ctx.shadowBlur = 20; // The blur radius of the shadow
    ctx.shadowOffsetX = 2; // Horizontal offset of the shadow
    ctx.shadowOffsetY = 2; // Vertical offset of the shadow

    // Determine where to draw the player's figure
    if (pindex === 0) {
        ctx.drawImage(offscreenCanvas, 15.5 * a - a + fig_ah, 11.5 * a - a + fig_av, (fig_h / fig.height) * fig.width, fig_h);
        ctx.fillText(nameText, 15.5 * a - a / 2, 11.5 * a - a + fig_av - 5); // Draw the name above the figure
    } else if (pindex === 1000) {
        ctx.drawImage(offscreenCanvas, 13 * a - a + fig_ah, 11 * a - a + fig_av, (fig_h / fig.height) * fig.width, fig_h);
        ctx.fillText(nameText, 13 * a - a / 2, 11 * a - a + fig_av - 5);
    } else if (pindex === 1001) {
        ctx.drawImage(offscreenCanvas, 10 * a - a + fig_ah, 11 * a - a + fig_av, (fig_h / fig.height) * fig.width, fig_h);
        ctx.fillText(nameText, 10 * a - a / 2, 11 * a - a + fig_av - 5);
    } else {
        for (let i = 1; i < pindex; i++) {
            if (CORNERS.includes(i)) {
                rot++;
                if (rot > 4) {
                    rot = 1;
                }
            }

            switch (rot) {
                case 1:
                    x++;
                    break;
                case 2:
                    y++;
                    break;
                case 3:
                    x--;
                    break;
                case 4:
                    y--;
                    break;
            }
        }

        ctx.drawImage(offscreenCanvas, x * a - a + fig_ah, y * a - a + fig_av, (fig_h / fig.height) * fig.width, fig_h);
        ctx.fillText(nameText, x * a - a / 2, y * a - a + fig_av - 5); // Draw the name above the figure
    }

    // Reset shadow properties to avoid affecting other parts of the drawing
    ctx.shadowColor = "transparent";
    ctx.shadowBlur = 0;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 0;
}


// Draw the game board on the canvas
const drawBoard = () => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(-camera.x, -camera.y);
    ctx.scale(camera.zoom, camera.zoom);
    ctx.drawImage(board, 0, 0, board.width, board.height, 0, 0, canvas.width, canvas.height);
    drawPlayers(ctx);
    ctx.restore();
};

// Event listener for when the board image is loaded
board.addEventListener("load", drawBoard);

// Handle zoom with mouse wheel
const handleWheel = (e) => {
    if (isMouseOverCanvas) {
        e.preventDefault();

        // Zoom direction (zoom in if wheel is up, zoom out if down)
        const zoomDirection = e.deltaY > 0 ? -1 : 1;

        // Calculate the new zoom level, clamping it between minZoom and maxZoom
        const newZoom = Math.min(
            Math.max(camera.zoom + zoomDirection * camera.zoomSpeed, camera.minZoom),
            camera.maxZoom
        );

        // Update the camera's zoom level
        camera.zoom = newZoom;

        // Get the center position of the canvas
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        // Calculate the position on the board under the center of the canvas
        const centerOnBoardX = (centerX + camera.x) / camera.zoom;
        const centerOnBoardY = (centerY + camera.y) / camera.zoom;

        // Adjust the camera position based on the new zoom, so that the zoom happens around the center
        camera.x = centerOnBoardX * camera.zoom - centerX;
        camera.y = centerOnBoardY * camera.zoom - centerY;

        // Calculate the maximum offsets for the camera
        const maxOffsetX = (board.width * camera.zoom - canvas.width);
        const maxOffsetY = (board.height * camera.zoom - canvas.height);

        // Ensure the camera stays within the board boundaries
        camera.x = Math.max(0, Math.min(camera.x, maxOffsetX));
        camera.y = Math.max(0, Math.min(camera.y, maxOffsetY));

        // Redraw the board with the new camera settings
        drawBoard();
    }
};



// Handle dragging start (mouse down)
const handleMouseDown = (e) => {
    if (isMouseOverCanvas) {
        isDragging = true;
        lastMousePos = {
            x: e.clientX,
            y: e.clientY
        };
    }
};

// Handle dragging movement (mouse move)
let isDrawing = false;

const handleMouseMove = (e) => {
    if (isDragging) {
        const deltaX = e.clientX - lastMousePos.x;
        const deltaY = e.clientY - lastMousePos.y;

        const dragFactor = camera.zoom;

        const newCameraX = camera.x - deltaX * dragFactor;
        const newCameraY = camera.y - deltaY * dragFactor;

        const maxOffsetX = (board.width * camera.zoom - canvas.width);
        const maxOffsetY = (board.height * camera.zoom - canvas.height);

        camera.x = Math.max(0, Math.min(newCameraX, maxOffsetX));
        camera.y = Math.max(0, Math.min(newCameraY, maxOffsetY));

        lastMousePos = {
            x: e.clientX,
            y: e.clientY
        };

        if (!isDrawing) {
            isDrawing = true;
            requestAnimationFrame(() => {
                drawBoard();
                isDrawing = false;
            });
        }
    }
};


// Stop dragging on mouse up
const handleMouseUp = () => {
    isDragging = false;
};

// Event listeners for mouse enter and leave
canvas.addEventListener("mouseenter", () => {
    isMouseOverCanvas = true;
});
canvas.addEventListener("mouseleave", () => {
    isMouseOverCanvas = false;
});

// Event listeners for wheel, mouse, and keyboard actions
canvas.addEventListener("wheel", handleWheel);
canvas.addEventListener("mousedown", handleMouseDown);
window.addEventListener("mousemove", handleMouseMove);
window.addEventListener("mouseup", handleMouseUp);

// Reset camera on spacebar press
window.addEventListener("keydown", (e) => {
    if (isMouseOverCanvas && e.key === " ") {
        e.preventDefault();
        camera.x = 0;
        camera.y = 0;
        camera.zoom = 1;
        drawBoard();
    }
});

// Initial drawing
drawBoard();