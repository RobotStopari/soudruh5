async function reloadRoom() {

    const url = "/ajax/players/"
    const response = await fetch(url, {
        method: 'GET',
    });
    const data = await response.json();
    const {
        players,
        player_id
    } = data;

    const player = data.players.find(p => p.id === player_id);

    const div = document.getElementById('players');
    const kostka = document.getElementById('hod_kostkou');
    div.innerHTML = '';

    console.log(players)
    popup.info({
        message: 'Refreshed data',
    });

    for (let p of players) {
        div.innerHTML += `<p style="font-size: 1.4em;">${p.name} - ${p.pindex}</p>`;
    }

    if (player.on_move) {
        kostka.style.display = ""
    } else {
        kostka.style.display = "none"
    }
}