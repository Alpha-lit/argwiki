document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("audio-toggle");
    const audioEls = document.querySelectorAll("audio");

    if (toggle) {
        toggle.addEventListener("click", () => {
            const enabled = toggle.dataset.enabled === "true";
            toggle.dataset.enabled = !enabled;
            localStorage.setItem("sfxEnabled", !enabled);
            audioEls.forEach(audio => {
                audio.muted = enabled;
            });
            toggle.innerText = enabled ? "🔊 Enable SFX" : "🔇 Disable SFX";
        });

        const savedState = localStorage.getItem("sfxEnabled");
        if (savedState === "false") {
            audioEls.forEach(audio => { audio.muted = true; });
            toggle.dataset.enabled = false;
            toggle.innerText = "🔊 Enable SFX";
        }
    }
});
