var visible = false

function clicked() {
	visible = !visible
	obj = document.getElementById("formulär")
	obj.style.setProperty("display", visible ? "initial" : "none")
}
