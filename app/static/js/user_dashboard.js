// ── Habit card click to mark done ──
document.querySelectorAll('.habit-card').forEach(card => {
    card.addEventListener('click', () => {
        const today = card.querySelector('.streak-dot.today');
        if (today) {
            today.classList.remove('today');
            today.classList.add('done');
            const count = card.querySelector('.streak-count');
            const num = parseInt(count.textContent);
            count.textContent = `${num + 1} day streak 🔥`;
        }
    });
});

// ── Two Minute Rule Timer ──
let timerInterval = null;
let seconds = 120;
let running = false;

const display = document.getElementById('timerDisplay');
const startBtn = document.getElementById('startBtn');
const resetBtn = document.getElementById('resetBtn');

function formatTime(s) {
    const m = Math.floor(s / 60);
    const sec = s % 60;
    return `${m}:${sec.toString().padStart(2, '0')}`;
}

if (display) display.textContent = formatTime(seconds);

if (startBtn) {
    startBtn.addEventListener('click', () => {
        if (!running) {
            running = true;
            startBtn.textContent = 'Pause';
            timerInterval = setInterval(() => {
                if (seconds <= 0) {
                    clearInterval(timerInterval);
                    running = false;
                    startBtn.textContent = 'Done!';
                    display.textContent = '0:00';
                    display.style.color = '#C9A84C';
                    return;
                }
                seconds--;
                display.textContent = formatTime(seconds);
            }, 1000);
        } else {
            clearInterval(timerInterval);
            running = false;
            startBtn.textContent = 'Resume';
        }
    });
}

if (resetBtn) {
    resetBtn.addEventListener('click', () => {
        clearInterval(timerInterval);
        running = false;
        seconds = 120;
        display.textContent = formatTime(seconds);
        display.style.color = '';
        startBtn.textContent = 'Start';
    });
}

// ── Rotating quotes ──
const quotes = [
    { text: "Every action you take is a vote for the type of person you wish to become.", author: "James Clear" },
    { text: "You do not rise to the level of your goals. You fall to the level of your systems.", author: "James Clear" },
    { text: "Habits are the compound interest of self-improvement.", author: "James Clear" },
    { text: "The most effective form of motivation is progress.", author: "James Clear" },
];

let quoteIndex = 0;
const quoteText = document.getElementById('quoteText');
const quoteAuthor = document.getElementById('quoteAuthor');

if (quoteText) {
    setInterval(() => {
        quoteIndex = (quoteIndex + 1) % quotes.length;
        quoteText.style.opacity = 0;
        setTimeout(() => {
            quoteText.textContent = `"${quotes[quoteIndex].text}"`;
            quoteText.style.opacity = 1;
        }, 400);
    }, 6000);
}