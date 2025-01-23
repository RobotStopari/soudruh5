async function updateFigs(data) {
	const figs = document.getElementById("figs");

	figs.innerHTML = "";

	try {
		const players = await data;

		players.forEach((player, index) => {
			insertFigure(player, index);
		});
	} catch (error) {
		console.error("Error loading players:", error);
	}
}

function insertFigure(player, index) {
	// Append the SVG to the board
	figs.innerHTML += FIG_SVG.trim();

	// Select the last appended SVG element
	const svgElement = figs.querySelectorAll(".fig_svg")[index];

	// Adjust the SVG attributes dynamically
	const pathElement = svgElement.querySelector("path");
	pathElement.setAttribute("fill", player.color || "#000000"); // Set the fill color

	// Set width and height via inline styles
	svgElement.style.width = "40px"; // Set the width
	svgElement.style.height = "auto"; // Maintain aspect ratio
	svgElement.style.display = "block"; // Ensure it doesn't overflow its container
}
