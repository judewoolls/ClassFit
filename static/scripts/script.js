function navigateTo(rawDate) {
    const d = new Date(rawDate); // rawDate can be a date string or object
    if (isNaN(d)) {
        console.error("Invalid date:", rawDate);
        return;
    }

    const year = d.getFullYear();
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const day = String(d.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

    console.log("Navigating to:", formattedDate);
    window.location.href = `/booking/${formattedDate}/`;
}
