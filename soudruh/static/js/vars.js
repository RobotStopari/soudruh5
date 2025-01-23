// SETTING GAME BOARD

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const board = document.getElementById("gameboard");
const fig = document.getElementById("fig");

const a = 200; // velikost pole

const fig_h = a - 30; // výška figurky
const fig_w = (fig_h / fig.height) * fig.width; // šířka figurky podle její výšky
const fig_av = 15; // odstup figurky od vrchu
const fig_ah = (a - fig_w) / 2; //šířka pole mínus šířka figurky děleno dvěma = odstup figurky zleva

const canvasWidth = 27 * a;
const canvasHeight = 20 * a;
canvas.width = canvasWidth;
canvas.height = canvasHeight;

// GAME BOARD CAMERA

const camera = {
	x: 0,
	y: 0,
	zoom: 1,
	zoomSpeed: 0.02,
	moveSpeed: 50,
	maxZoom: 2,
	minZoom: 1,
};

let isMouseOverCanvas = false;
let isDragging = false;
let lastMousePos = {
	x: 0,
	y: 0,
};

// SPECIAL BOARD PLACES

const startCoords = { x: 15, y: 10 };

const specialPositions = {
	0: { x: 15.5, y: 11.5, scale: 0.9 },
	1000: { x: 13, y: 11, scale: 1.4 },
	1001: { x: 10, y: 11, scale: 1.4 },
};

// PLAYER FIGURE SVG

const FIG_SVG =
	'<svg class="fig_svg m-2" version="1.0" xmlns="http://www.w3.org/2000/svg" width="772.000000pt" height="1280.000000pt" viewBox="0 0 772.000000 1280.000000" preserveAspectRatio="xMidYMid meet"> <g transform="translate(0.000000,1280.000000) scale(0.100000,-0.100000)" fill="#000000" stroke="none"><path d="M3610 12788 c-595 -55 -1159 -311 -1588 -722 -217 -207 -440 -535-555 -816 -121 -297 -171 -557 -171 -885 0 -239 15 -369 69 -580 108 -423 311 -773 639 -1100 213 -213 404 -351 671 -483 72 -36 131 -66 133 -67 2 -2 -244 -619 -546 -1372 -303 -752 -816 -2032 -1142 -2843 -326 -811 -710 -1770 -855 -2130 l-263 -655 3 -75 c3 -94 16 -142 55 -204 104 -164 363 -324 729 -451 1290 -446 3649 -536 5351 -204 818 160 1366 401 1524 670 14 26 33 79 42 119 l15 73 -202 516 c-111 284 -291 743 -399 1021 -109 278 -483 1236 -833 2130 -786 2011 -1337 3422 -1337 3425 0 1 33 17 73 35 216 100 465 273 657 456 400 384 644 852 727 1394 24 159 24 492 -1 648 -57 365 -172 665 -370 967 -309 470 -792 833 -1346 1013 -340 111 -724 153 -1080 120z"/></g></svg>';

// GENERATING CORNERS

let CORNERS = [];

function generateCorners(numberOfCorners) {
	let short = 3;
	let long = 9;
	let shorter = true;
	let now = 3;
	CORNERS = [now];

	for (let c = 0; c < numberOfCorners; c++) {
		if (shorter) {
			now = now + short;
			short += 1;
			shorter = false;
		} else {
			now = now + long;
			long += 1;
			shorter = true;
		}
		CORNERS.push(now);
	}

	return CORNERS;
}

generateCorners(100);
