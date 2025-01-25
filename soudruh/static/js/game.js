function prepareColoredPlayerFigure(player) {
	// Create an off-screen canvas to manipulate the image
	const offscreenCanvas = document.createElement("canvas");
	const offscreenCtx = offscreenCanvas.getContext("2d");

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

	return offscreenCanvas;
}

function preparePlayerName(player) {
	// Calculate the width and height of the player's name
	const nameText = player.name.charAt(0).toUpperCase() + player.name.slice(1);
	ctx.font = "70px Arial"; // Set the font for the name text
	ctx.textAlign = "center"; // Align the text to be centered
	ctx.textBaseline = "bottom"; // Position the text above the figure
	ctx.fillStyle = "white";

	// Set the drop shadow properties
	ctx.shadowColor = "rgba(0, 0, 0, 1)"; // Shadow color (black with some transparency)
	ctx.shadowBlur = 20; // The blur radius of the shadow
	ctx.shadowOffsetX = 2; // Horizontal offset of the shadow
	ctx.shadowOffsetY = 2; // Vertical offset of the shadow

	return nameText;
}

function resetCanvasShadow(context) {
	context.shadowColor = "transparent";
	context.shadowBlur = 0;
	context.shadowOffsetX = 0;
	context.shadowOffsetY = 0;
}

function drawFigImage(pl_name, x, y, canvas, offset) {
	let new_x = offset > 0 ? getRandomFloat(x - offset, x + offset) : x;
	let new_y = offset > 0 ? getRandomFloat(y - offset, y + offset - 0.2) : y;

	ctx.drawImage(
		canvas,
		new_x * a - a + fig_ah,
		new_y * a - a + fig_av,
		(fig_h / fig.height) * fig.width,
		fig_h
	);
	ctx.fillText(pl_name, new_x * a - a / 2, new_y * a - a + fig_av - 5);
}

function drawFigOnBoard(player, offscreenCanvas, location) {
	const pindex = location;

	const nameText = preparePlayerName(player);

	// Default coordinates and rotation for the figure
	let { x, y } = startCoords;
	let rotation = 1;

	// Helper function to calculate new coordinates based on rotation
	const getNextCoords = (currentX, currentY, rotation) => {
		switch (rotation) {
			case 1:
				return { x: currentX + 1, y: currentY }; // Right
			case 2:
				return { x: currentX, y: currentY + 1 }; // Down
			case 3:
				return { x: currentX - 1, y: currentY }; // Left
			case 4:
				return { x: currentX, y: currentY - 1 }; // Up
			default:
				return { x: currentX, y: currentY }; // No change
		}
	};

	if (specialPositions[pindex]) {
		// Draw figure at a predefined special position
		const { x, y, scale } = specialPositions[pindex];
		drawFigImage(nameText, x, y, offscreenCanvas, scale);
	} else {
		// Calculate position for general player indices
		for (let i = 1; i < pindex; i++) {
			if (CORNERS.includes(i)) {
				// Increment rotation and reset if exceeding 4
				rotation = (rotation % 4) + 1;
			}
			// Update coordinates based on rotation
			({ x, y } = getNextCoords(x, y, rotation));
		}
		drawFigImage(nameText, x, y, offscreenCanvas, 0);
	}

	// Reset shadow properties to avoid affecting other drawings
	resetCanvasShadow(ctx);
}

function drawPlayers(ctx) {
	try {
		PLAYERS.forEach((player) => {
			let move_times = player.pindex - player.heading_from;
			for (move_times; move_times > 0; move_times--) {
				drawFigOnBoard(
					player,
					prepareColoredPlayerFigure(player),
					move_times + player.heading_from
				);
			}
		});
	} catch {
		console.log("loading PLAYERS");
	}
}
