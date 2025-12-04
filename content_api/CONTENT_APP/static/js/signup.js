// Simple micro-interaction on input focus
document.querySelectorAll("input").forEach(inp => {
    inp.addEventListener("focus", () => {
        inp.style.transform = "scale(1.02)";
    });

    inp.addEventListener("blur", () => {
        inp.style.transform = "scale(1)";
    });
});
