
var form = document.getElementById("create");
form.addEventListener("submit", function(event){
	event.preventDefault();
	create = document.getElementById("create");
	r = {
		title: create.title,
		repo_link: create.link,
		share_permissions: getRadio("share"),
		auto_pull_request: getRadio("pullreq"),
		is_assignment: getRadio("note"),
		
		deadline: create.deadline,
		checkpoints: [] //implement this
	}
	
	for(var row=0; row < document.getElementById("checkpoints"); row++){
		//r.checkpoints.push({name: create.n0})
	}
	
	window.alert(JSON.stringify(r));
	
	
	
});

//takes in the name of a radio input in the form and returns true or false
function getRadio(name){
	var radios = document.getElementsByName(name);
	return radios[0].value == "true";
}

//enables the deadline info section
function enableDeadlines(){
	document.getElementById("deadline").disabled = false;
}

//disables the deadline info section
function disableDeadlines(){
	document.getElementById("deadline").disabled = true;
	//disable the pullreq radio button
}

//updates the table with number of checkpoints specified by #numcheck
function changeTable(){
	t = document.getElementById("checkpoints");
	t.innerHTML = "<tr><th>Name (optional)</th><th>Date</th><th>Number of Commits</th></tr>"; //clears content
	for(var i=0; i<document.getElementById("numcheck").value; i++){
		t.innerHTML += "<tr><td><input type=\"text\" name=\"n" + i + "\"></td><td><input name=\"d" + i +"\" type=\"date\"></td><td><input name=\"nc"+i+"\" type=\"number\" min=\"0\"></td></tr>";
	}
}
