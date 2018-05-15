
var form = document.getElementById("create");
form.addEventListener("submit", function(event){
	
	
	
	
});

//enables the deadline info section
function enableDeadlines(){
	document.getElementById("deadline").disabled = false;
}

//disables the deadline info section
function disableDeadlines(){
	document.getElementById("deadline").disabled = true;
}

//updates the table with number of checkpoints specified by #numcheck
function changeTable(){
	t = document.getElementById("checkpoints");
	t.innerHTML = "<tr><th>Name (optional)</th><th>Date</th><th>Number of Commits</th></tr>"; //clears content
	for(var i=0; i<document.getElementById("numcheck").value; i++){
		t.innerHTML += "<tr><td><input type=\"text\" name=\"n" + i + "\"></td><td><input name=\"d" + i +"\" type=\"date\"></td><td><input name=\"nc"+i+"\" type=\"number\" min=\"0\"></td></tr>";
	}
}
