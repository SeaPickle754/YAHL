var callsign = null;
var frequency = null;
var rstSent = null;
var rstRecv = null;
var mode = null;
var date = null;
var time = null;
var comments = null;
var exchange = null;
// just to reset everything back to null, after contact has been 
// successfully pushed to server.
function init_variables(){
    callsign = null;
    frequency = null;
    rstSent = null;
    rstRecv = null;
    mode = null;
    date = null;
    time = null;
    comments = null;
    exchange = null;
}
// declare a socket for the server/frontend interface

var contactTbl = document.getElementById("contactTbl")
var tbodyRef = document.getElementById('contactTbl').getElementsByTagName('tbody')[0];
function logContact(){
    callsign = document.getElementById("callsign").value
    frequency = document.getElementById("freq").value
    rstSent = document.getElementById("rsts").value
    rstRecv = document.getElementById("rstr").value
    mode = document.getElementById("mode").value
    comments = document.getElementById("cmnts").value
    time = document.getElementById("logTime").value
    date = document.getElementById("logDate").value
    mode = mode.toUpperCase()
    var p = document.getElementById("output");
    p.innerText = "Callsign:" + callsign + " freq:"+frequency+" rsts: " + rstSent + " rstr:" + rstRecv + " mode "+mode;
    updateTable();
    pushDataToServer();
};
function updateTable(){
    var newRow = tbodyRef.insertRow();
    newRow.innerHTML = "<tr>\
			<td>"+callsign+"</td>\
			<td>"+ mode +"</td>\
			<td>"+frequency+"</td>\
			<td>"+ time +"</td>\
			<td>"+ date +"</td>\
			<td>"+ comments +"</td>\
		</tr>"
}

function packData(){
    // this fuction will pack the data into one long string.
    var dataString = "";
    // server will split at | (straight line) character.
    // IMPORTANT:
    // format is call, freq, sent, recv, mode, date, time, exchange
    // Here we just append everything to the packet string
    dataString += callsign + "|";
    dataString += frequency + "|";
    dataString += rstSent + "|";
    dataString += rstRecv + "|";
    dataString += mode + "|";
    dataString += date + "|";
    dataString += time + "|";
    dataString += exchange + "|";
    // send it to console in case we care
    console.log(dataString)
    return dataString;

}
function pushDataToServer(){
    var isSocketReady = false;
    const socket = new WebSocket("ws://localhost:12345/")
    var dataString = "";
    dataString = packData();
    // book keeping: print rcved msg to console
    // and also send status to console
    socket.onopen = () => {
        console.log('WebSocket connected');
        isSocketReady = true;
    };
    // after we know websocket has been opened
    socket.onmessage = (event) => {
        const receivedMessage = event.data;
        console.log(receivedMessage);
        // send packet
        socket.send(dataString);
        
    };
    socket.onclose = () => {
        console.log('WebSocket disconnected');
    }
    init_variables();
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
