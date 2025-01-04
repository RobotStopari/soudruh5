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


async function reloadRoom() {

    const url = "/ajax/data/"
    const response = await fetch(url, {
        method: 'GET',
    });
    const data = await response.json();
    const {
        players,
        history_records,
        player_id
    } = data;

    const player = data.players.find(p => p.id === player_id);

    const players_div = document.getElementById('players');
    const history_records_div = document.getElementById('messages');
    const cube = document.getElementById('hod_kostkou');
    players_div.innerHTML = '';
    history_records_div.innerHTML = '';


    console.log('Ajax successful')

    /*if (messages.length > last_message) {
        incoming_message = messages[messages.length - 1];
        last_message = incoming_message.id;
        mes.info({
            message: incoming_message.message,
        });
    }*/

    if (player.on_move) {
        cube.style.display = ""
    } else {
        cube.style.display = "none"
    }

    for (let p of players) {
        players_div.innerHTML += `<p style="font-size: 1.4em;">${p.name} - ${p.pindex}</p>`;
    }

    for (let i = history_records.length - 1; i >= 0; i--) {
        createHistoryRecord(history_records[i], history_records_div);
    }

    updateBoard(players)
    return players;
}