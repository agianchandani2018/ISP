
var form = document.getElementById("create");
form.addEventListener("submit", function(event){
	//use preventDefault for testing
	event.preventDefault();
	var create = document.getElementById("create");
	var r = {
		title: create.title,
		repo_link: create.link,
		share_permissions: getRadio("share"),
		auto_pull_request: getRadio("pullreq"),
		is_assignment: getRadio("note"),
		
		deadline: create.deadline,
		checkpoints: []
	}
	
	for(var row=0; row < document.getElementById("checkpoints").rows.length-1; row++){
		r.checkpoints.push({name: document.getElementById("n"+row).value, date: document.getElementById("d"+row).value, num_commits: document.getElementById("nc"+row).value});
	}
	
	window.alert(JSON.stringify(r));
	//and then we'll send this somewhere
	
	//actually we probably don't need this anymore?
	$.ajax({
		url: "http://compsci-dev.pingry.k12.nj.us/",//put something here, depending on where we're sending it
		type: 'PUT',
		data: JSON.stringify(r),
		contentType: 'application/json',
		success: function(result){
			alert("success?");
		}
	});
	/*
	var xhr = new XMLHttpRequest();
	xhr.open('PUT', "", true); //what link to put here???
	xhr.send();
	*/
	
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
		t.innerHTML += "<tr><td><input type=\"text\" id=\"n" + i + "\"></td><td><input id=\"d" + i +"\" type=\"date\"></td><td><input id=\"nc"+i+"\" type=\"number\" min=\"0\"></td></tr>";
	}
}
