var visible = false

function clicked() {
	visible = !visible
	obj = document.getElementById("mainformular")
	obj.style.setProperty("display", visible ? "initial" : "none")
    document.getElementById("formularknapp").innerHTML = visible ? "Stäng" : "Skapa inlägg"
}
