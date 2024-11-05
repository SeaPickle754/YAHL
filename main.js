var callsign = null
var frequency = null
var rstSent = null
var rstRecv = null
var mode = null
var date = null
var time = null
var comments = null
function logContact(){
    callsign = document.getElementById("callsign").value
    frequency = document.getElementById("freq").value
    rstSent = document.getElementById("rsts").value
    rstRecv = document.getElementById("rstr").value
    mode = document.getElementById("mode").value
    comments = document.getElementById("cmnts").value

    mode = mode.toUpperCase()
    var p = document.getElementById("output");
    p.innerText = "Callsign:" + callsign + " freq:"+frequency+" rsts: " + rstSent + " rstr:" + rstRecv + " mode "+mode;
    pushDataToServer();
};

function pushDataToServer(){
    
}
// chat gpt
function updateClock() {
            // Get current time and date in UTC
            const now = new Date();

            // Format date as YYYY-MM-DD
            const year = now.getUTCFullYear();
            const month = String(now.getUTCMonth() + 1).padStart(2, '0'); // Months are 0-indexed
            const day = String(now.getUTCDate()).padStart(2, '0');
            const currentDate = `${year}-${month}-${day}`;

            // Format time as HH:MM:SS
            const hours = String(now.getUTCHours()).padStart(2, '0');
            const minutes = String(now.getUTCMinutes()).padStart(2, '0');
            const seconds = String(now.getUTCSeconds()).padStart(2, '0');
            const currentTime = `${hours}:${minutes}:${seconds}`;


            document.getElementById("clock").textContent = currentDate + " # " + currentTime;
            document.getElementById('logTime').value = `${hours}:${minutes}`;
            document.getElementById('logDate').value = `${year}-${month}-${day}`;


}


// Update the clock every second
setInterval(updateClock, 1000);
