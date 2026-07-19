const textarea = document.querySelector("textarea");
const counter = document.getElementById("counter");

function updateCounter() {
    if (textarea && counter) {
        counter.innerHTML = textarea.value.length + " Characters";
    }
}

// Page load hote hi count update hoga
updateCounter();

// Typing ke time count update hoga
if (textarea) {
    textarea.addEventListener("input", updateCounter);
}

// Clear button
function clearText() {
    textarea.value = "";
    updateCounter();
    textarea.focus();
}