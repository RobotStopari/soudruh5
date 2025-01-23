const drawBoard = () => {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.save();
	ctx.translate(-camera.x, -camera.y);
	ctx.scale(camera.zoom, camera.zoom);
	ctx.drawImage(
		board,
		0,
		0,
		board.width,
		board.height,
		0,
		0,
		canvas.width,
		canvas.height
	);
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
		const maxOffsetX = board.width * camera.zoom - canvas.width;
		const maxOffsetY = board.height * camera.zoom - canvas.height;

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
			y: e.clientY,
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

		const maxOffsetX = board.width * camera.zoom - canvas.width;
		const maxOffsetY = board.height * camera.zoom - canvas.height;

		camera.x = Math.max(0, Math.min(newCameraX, maxOffsetX));
		camera.y = Math.max(0, Math.min(newCameraY, maxOffsetY));

		lastMousePos = {
			x: e.clientX,
			y: e.clientY,
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
