var visible = false

function clicked() {
	visible = !visible
	obj = document.getElementById("mainformular")
	obj.style.setProperty("display", visible ? "initial" : "none")
    document.getElementById("formularknapp").innerHTML = visible ? "Stäng" : "Skapa inlägg"
}

function kommentera(id) {
    post = document.getElementById("post-" + id)
    falt = post.getElementsByClassName("kommentarsfalt")[0]
    knapp = post.getElementsByClassName("kommentera knapp")[0]

    if (falt.innerHTML == "") {
        knapp.innerHTML = "Stäng"
        falt.innerHTML = `
<form method="post" class="kommentarsformular formular" action="/forum/kommentera` + id + `">
  <label for="rubrik">Rubrik</label><br>
  <input type="text" id="rubrik" name="rubrik" required maxlength="60"><br>
  <label for="text">Innehåll</label><br>
  <textarea cols=40 rows=5 name="text" required maxlength="1200" spellcheck="false"></textarea><br><br>
  <label for="namn">Namn</label><br>
  <input type="text" id="namn" name="namn" required maxlength="60"><br>
  <input type="submit" value="Skicka" id="skickaknapp" class="knapp">
</form>
`

    } else {
        knapp.innerHTML = "Kommentera"
        falt.innerHTML = ""
    }
}
