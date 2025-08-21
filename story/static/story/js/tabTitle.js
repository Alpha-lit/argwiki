document.addEventListener("DOMContentLoaded", () => {
    const titles = ["Hi", "hI"];
    let i = 0;
    setInterval(() => {
        document.title = titles[i % titles.length];
        i++;
    }, 2000);
});
