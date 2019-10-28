/*
	File for creating listeners on page elements.
*/

var Session_List = document.getElementById("session_list");

var Add_Session_Btn = document.getElementById("add_session_btn");

Add_Session_Btn.addEventListeners("click", addSession(session_list));


