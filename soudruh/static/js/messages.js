function formatDateTime(isoString) {
    const date = new Date(isoString);

    const day = date.getDate(); // Day of the month (1-31)
    const month = date.getMonth() + 1; // Months are zero-indexed
    const hours = date.getHours(); // Hours (0-23)
    const minutes = date.getMinutes().toString().padStart(2, '0'); // Minutes (00-59)

    return `${day}. ${month}. ${hours}:${minutes}`;
}

function displayNotification(notifications, i) {
    const top = Notification({
        position: 'top-right',
        duration: 3000,
        isHidePrev: false,
        isHideTitle: true,
        maxOpened: 3,
    });

    const mid = Notification({
        position: 'center',
        duration: 4000,
        isHidePrev: false,
        isHideTitle: true,
        maxOpened: 3,
    });

    switch (notifications[i].type) {
        case 'dice':
            top.info({
                message: notifications[i].message,
            });
            break;
        case 'leave':
        case 'join':
            top.warning({
                message: notifications[i].message,
            });
            break;
        case 'sad':
            mid.dialog({
                message: notifications[i].message,
            });
            break;
        case 'happy':
            mid.dialog({
                message: notifications[i].message,
            });
    }
}

function createHistoryRecord(h, history_records_div) {
    switch (h.type) {
        case 'dice':
            history_records_div.innerHTML +=
                `<div class="alert alert-primary d-flex align-items-center" role="alert">
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
                <div>
                    ${formatDateTime(h.created_at)} - ${h.message} 
                </div>
            </div>`;
            break;
        case 'move':
            history_records_div.innerHTML +=
                `<div class="alert alert-secondary d-flex align-items-center" role="alert">
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
                <div>
                    ${formatDateTime(h.created_at)} - ${h.message} 
                </div>
            </div>`;
            break;
        case 'join':
        case 'leave':
            history_records_div.innerHTML +=
                `<div class="alert alert-warning d-flex align-items-center" role="alert">
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                <div>
                    ${formatDateTime(h.created_at)} - ${h.message} 
                </div>
            </div>`;
            break;
        case 'sad':
            history_records_div.innerHTML +=
                `<div class="alert alert-danger d-flex align-items-center" role="alert">
                    <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                    <div>
                        ${formatDateTime(h.created_at)} - ${h.message} 
                    </div>
                </div>`;
            break;
        case 'happy':
            history_records_div.innerHTML +=
                `<div class="alert alert-success d-flex align-items-center" role="alert">
                        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#exclamation-triangle-fill"/></svg>
                        <div>
                            ${formatDateTime(h.created_at)} - ${h.message} 
                        </div>
                    </div>`;
            break;
    }
}

function createChatMessage(m, history_records_div) {
    history_records_div.innerHTML +=
        `
        <strong>${formatDateTime(m.created_at)} - ${capitalize(m.name)}:</strong><br>${m.message}<br><br>
        `;
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}