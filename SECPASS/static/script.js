document.addEventListener("DOMContentLoaded", function () {
    const saveBtn = document.getElementById("saveBtn");
    const passwordList = document.getElementById("passwordList");

    saveBtn.addEventListener("click", async () => {
        const website = document.getElementById("website").value;
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        await savePassword(website, username, password);
        displayPasswords();
    });

    async function savePassword(website, username, password) {
        await fetch("/save", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ website, username, password }),
        });
    }

    async function displayPasswords() {
        passwordList.innerHTML = "";

        const response = await fetch("/passwords");
        const passwords = await response.json();

        passwords.forEach((password) => {
            const li = document.createElement("li");
            li.textContent = `${password.website} - ${password.username}: ${password.password}`;
            passwordList.appendChild(li);
        });
    }

    displayPasswords();
});
