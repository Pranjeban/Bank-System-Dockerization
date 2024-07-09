document.getElementById("add-user-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    let account_id = document.getElementById("account_id").value;
    let name = document.getElementById("name").value;
    let current_balance = document.getElementById("current_balance").value;

    let response = await fetch("/add_user/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ account_id: account_id, name: name, current_balance: current_balance })
    });

    let result = await response.json();
    alert(result.message);
});

document.getElementById("get-user-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    let account_id = document.getElementById("search_account_id").value;

    let response = await fetch(`/get_user/${account_id}`);
    if (response.status === 404) {
        alert("User not found");
        return;
    }

    let user = await response.json();
    let detailsDiv = document.getElementById("user-details");
    detailsDiv.innerHTML = `<p>Account ID: ${user.account_id}</p><p>Name: ${user.name}</p><p>Current Balance: ${user.current_balance}</p> `;
});
