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

// Define the escapeHtml function to sanitize input
function escapeHtml(unsafe) {
    return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

async function sendChatMessage() {
    const url = "/send-chat-message/";
    const messageInput = document.querySelector('#napsat-zpravu input.form-control');
    let message = messageInput.value;

    // Escape HTML characters
    message = escapeHtml(message);

    if (message.length > 2000) {
        alert("Message cannot exceed 2000 characters.");
        return;
    }

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            const errorText = await response.text(); // Get detailed error response
            throw new Error(`HTTP error! Status: ${response.status}, Response: ${errorText}`);
        }
    } catch (error) {
        console.error("Error sending message:", error);
        alert("An error occurred: " + error.message); // Show a user-friendly error message
    }

    // Clear the input field
    messageInput.value = '';
    reloadRoom()
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
        notifications,
        chat_messages
    } = data;

    const player = data.players.find(p => p.id === player_id);

    const history_records_div = document.getElementById('messages');
    const chat_messages_div = document.getElementById('chat-messages');
    const cube = document.getElementById('hod_kostkou');
    history_records_div.innerHTML = '';
    chat_messages_div.innerHTML = '';

    for (let i = notifications.length - 1; i >= 0; i--) {
        displayNotification(notifications, i)
    }

    if (player.on_move) {
        cube.style.display = ""
    } else {
        cube.style.display = "none"
    }

    for (let i = history_records.length - 1; i >= 0; i--) {
        createHistoryRecord(history_records[i], history_records_div);
    }

    for (let i = chat_messages.length - 1; i >= 0; i--) {
        createChatMessage(chat_messages[i], chat_messages_div);
    }

    PLAYERS = players;

    drawBoard(true);

    return players;
}