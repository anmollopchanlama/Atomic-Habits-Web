// Count up animation for stats
document.querySelectorAll('.stat-value').forEach(el => {
    const target = parseInt(el.textContent);
    if (isNaN(target)) return;
    let count = 0;
    const step = Math.ceil(target / 30);
    const timer = setInterval(() => {
        count = Math.min(count + step, target);
        el.textContent = count;
        if (count >= target) clearInterval(timer);
    }, 40);
});

// Search/filter users table
const searchInput = document.getElementById('searchInput');
if (searchInput) {
    searchInput.addEventListener('input', () => {
        const query = searchInput.value.toLowerCase();
        document.querySelectorAll('.users-table tbody tr').forEach(row => {
            const text = row.textContent.toLowerCase();
            row.style.display = text.includes(query) ? '' : 'none';
        });
    });
}