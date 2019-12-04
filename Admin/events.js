/*
* File: events.js
* Description: This Javascrpt file creates listeners on the
* Admin's page elements.
*/

var Session_List = document.getElementById('session_list');

console.log(Session_List);

var Add_Session_Btn = document.getElementById('add_session_btn');

console.log(Add_Session_Btn);

Add_Session_Btn.addEventListener("click", function() {
	addSession(Session_List);
});
