let copyRight = () => {
	date = new Date().getFullYear();
	document.querySelector('.copyright').innerHTML = `©️  ${date}`;
}

copyRight();

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

openForm();
closeForm();
