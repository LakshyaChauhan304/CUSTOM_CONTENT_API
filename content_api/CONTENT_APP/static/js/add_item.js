/* 🌙 Dark Mode Toggle */
function toggleDarkMode() {
    document.body.classList.toggle("dark");
}

/* 📝 Auto Word Count */
const editorArea = document.getElementById("editorArea");
const wordCountSpan = document.getElementById("wordCount");
const saveStatus = document.getElementById("saveStatus");

editorArea.addEventListener("input", () => {
    const words = editorArea.value.trim().split(/\s+/).filter(w => w.length);
    wordCountSpan.textContent = words.length;

    saveStatus.textContent = "Saving...";
    setTimeout(() => saveStatus.textContent = "Saved", 600);
});

/* 📂 Drag & Drop Media Upload */
const dropzone = document.getElementById("dropzone");
const mediaInput = document.getElementById("mediaInput");

// Click to open file picker
dropzone.addEventListener("click", () => mediaInput.click());

// Drag Enter
dropzone.addEventListener("dragover", e => {
    e.preventDefault();
    dropzone.style.background = "#e0e0ff";
});

// Drag Leave
dropzone.addEventListener("dragleave", () => {
    dropzone.style.background = "";
});

// Drop file
dropzone.addEventListener("drop", e => {
    e.preventDefault();
    dropzone.style.background = "";

    const file = e.dataTransfer.files[0];
    mediaInput.files = e.dataTransfer.files;

    dropzone.innerHTML = `<p>Uploaded: <strong>${file.name}</strong></p>`;
});

/* ✨ WordPress-like Tools */
function insertHeading() {
    editorArea.value += "\n\n## New Heading\n";
}
function insertDivider() {
    editorArea.value += "\n\n---\n";
}
function insertChecklist() {
    editorArea.value += "\n\n- [ ] Checklist item\n";
}
function insertQuote() {
    editorArea.value += `\n\n> Quoted text\n`;
}
function insertWarning() {
    editorArea.value += `\n\n⚠️ WARNING: Something important here!\n`;
}
