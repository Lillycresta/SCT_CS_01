const typingArea = document.getElementById("typingArea");
const logs = document.getElementById("logs");

const clearBtn = document.getElementById("clearBtn");
const downloadBtn = document.getElementById("downloadBtn");

let keyLogs = "";

// Detect keys typed inside textarea
typingArea.addEventListener("keydown", function(event) {

    let key = event.key;

    // Space key
    if (key === " ") {
        key = "[SPACE]";
    }

    // Enter key
    if (key === "Enter") {
        key = "[ENTER]<br>";
    }

    keyLogs += key + " ";

    logs.innerHTML = keyLogs;
});

// Clear logs
clearBtn.addEventListener("click", function() {

    keyLogs = "";

    logs.innerHTML = "";

    typingArea.value = "";
});

// Download logs
downloadBtn.addEventListener("click", function() {

    const blob = new Blob([keyLogs], {
        type: "text/plain"
    });

    const a = document.createElement("a");

    a.href = URL.createObjectURL(blob);

    a.download = "keylogs.txt";

    a.click();
});