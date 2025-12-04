async function loadItems() {
    const res = await fetch('/content/api/items/');
    const data = await res.json();
    const items = Array.isArray(data) ? data : (data.results || []);
    const tbody = document.getElementById("itemsBody");

    // Update statistics
    document.getElementById("statTotal").innerText = items.length;
    document.getElementById("statToday").innerText = items.filter(i => {
        return new Date(i.created).toDateString() === new Date().toDateString();
    }).length;
    document.getElementById("statUsers").innerText = new Set(items.map(i => i.user_username)).size;

    // Populate User Filter
    const filterUser = document.getElementById("filterUser");
    [...new Set(items.map(i => i.user_username))].forEach(username => {
        const opt = document.createElement("option");
        opt.value = username;
        opt.textContent = username;
        filterUser.appendChild(opt);
    });

    // Build Table
    tbody.innerHTML = items.map(item => `
        <tr>
            <td>${item.title}</td>
            <td>${item.body || ""}</td>
            <td>${item.user_username || "Unknown"}</td>
            <td>${new Date(item.created).toLocaleDateString()}</td>
           <td>
    <span class="action-btn edit" onclick="editItem(${item.id})">✏️</span>
    <span class="action-btn delete" onclick="deleteItem(${item.id})">🗑️</span>
</td>

        </tr>
    `).join('');
}

function editItem(id) {
    window.location.href = `/content/edit-item/${id}/`;
}

async function deleteItem(id) {
    if (!confirm("Delete this item?")) return;
    await fetch(`/content/api/items/${id}/`, { method: "DELETE" });
    loadItems();
}

// Search Filter
document.getElementById("searchBox").addEventListener("keyup", function () {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll("#itemsBody tr");
    rows.forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(filter) ? "" : "none";
    });
});

loadItems();
