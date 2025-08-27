const sfxToggle = document.getElementById("sfx-toggle");
const savedPreference = localStorage.getItem("sfxEnabled") === "true";

const roomSfxInput = document.getElementById("room-sfx-url");
let sfxAudio = null;

if (roomSfxInput) {
    sfxAudio = new Audio(roomSfxInput.value);
    sfxAudio.preload = "auto";
}

// Restore toggle state
if (sfxToggle) {
    sfxToggle.checked = savedPreference;

    // Auto-play when entering a room (if enabled)
    if (savedPreference && sfxAudio) {
        sfxAudio.play().catch(() => {});
    }

    sfxToggle.addEventListener("change", () => {
        if (!sfxAudio) return;
        if (sfxToggle.checked) {
            sfxAudio.play().catch(() => {});
            localStorage.setItem("sfxEnabled", "true");
        } else {
            sfxAudio.pause();
            sfxAudio.currentTime = 0;
            localStorage.setItem("sfxEnabled", "false");
        }
    });
}
