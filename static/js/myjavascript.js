function alertFunction() {
	alert("Please create an account via the sign up page.")
}

function loadDoc() {
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				document.getElementById("demo").innerHTML = this.responseText;
			}
		};
		xhttp.open("GET", ajax_info.txt", true);
		xhttp.send();
}

$.get("/users", function(response){
	name = response.name;
	console.log(first_name);
});	