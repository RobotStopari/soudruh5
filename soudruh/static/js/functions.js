function getRandomFloat(min, max) {
	return Math.random() * (max - min) + min;
}

function waitTime(time) {
	return new Promise((resolve) => setTimeout(resolve, time));
}
