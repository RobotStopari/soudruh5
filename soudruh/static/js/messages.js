const mes = Notification({
    position: 'top-right',
    duration: 3000,
    isHidePrev: false,
    isHideTitle: true,
    maxOpened: 3,
});

function formatDateTime(isoString) {
    const date = new Date(isoString);

    const day = date.getDate(); // Day of the month (1-31)
    const month = date.getMonth() + 1; // Months are zero-indexed
    const hours = date.getHours(); // Hours (0-23)
    const minutes = date.getMinutes().toString().padStart(2, '0'); // Minutes (00-59)

    return `${day}. ${month}. ${hours}:${minutes}`;
}

function createHistoryRecord(h, history_records_div) {
    history_records_div.innerHTML +=
        `<div class="alert alert-primary d-flex align-items-center" role="alert">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
            <div>
                ${formatDateTime(h.created_at)} - ${h.message} 
            </div>
        </div>`;
}