let copyRight = () => {
	date = new Date().getFullYear();
	document.querySelector('.copyright').innerHTML = `©️  ${date}`;
}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

function showMessages() {
	document.getElementById('feed-messages-hidden').style.display = "block";
}

function showCommentForm() {
	document.querySelector('.feed-comment-form').style.display = 'block';
}

copyRight();
