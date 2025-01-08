async function rollDice() {
    const url = "/cube/";
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({})
    });

    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    } else {
        reloadRoom()
    }
}

let PLAYERS

async function reloadRoom() {

    const url = "/ajax/data/"
    const response = await fetch(url, {
        method: 'GET',
    });
    const data = await response.json();
    const {
        players,
        history_records,
        player_id,
        notifications
    } = data;

    const player = data.players.find(p => p.id === player_id);

    const history_records_div = document.getElementById('messages');
    const cube = document.getElementById('hod_kostkou');
    history_records_div.innerHTML = '';

    for (let i = notifications.length - 1; i >= 0; i--) {
        displayNotification(notifications, i)
    }

    if (player.on_move) {
        cube.style.display = ""
    } else {
        cube.style.display = "none"
    }

    console.log(history_records.length)

    for (let i = history_records.length - 1; i >= 0; i--) {
        createHistoryRecord(history_records[i], history_records_div);
    }

    PLAYERS = players;

    drawBoard(true);

    return players;
}