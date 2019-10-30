function addSession (session_list) {
	loaded_sessions = session_list.getElementsByClassName('list-btn');

	for(var i = 0; i < loaded_sessions.length; i++);
	var id = 'session_' + i;
	var name = 'New Empty Session (Click to Edit)'

	var text = '<button class="btn list-btn col-12 btn-outline-dark"';
		text +=	('id="' + id);
		text += ('">' + name + '</button>');

	session_list.innerHTML += text;

	new_session = document.getElementById(id);

	console.log(new_session);

	new_session.addEventListener("click", function() {
		sessionClick(id);
	});
};

function removeSession(session_list, id) {
	var session_to_remove = session_list.getElementById(id);
	session_to_remove.parentNode.removeChild(session_to_remove);
}

function sessionClick (id) {
	console.log(id);
	/* TO DO */
}

