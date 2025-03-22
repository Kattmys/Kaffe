/*
var bild_i = 0
var bilder = [
	"images/animatedcoffeeduck.png",
	"images/fransk-press.jpg",
	"images/bg.png"
]

function clicked() {
	bild_i++
	if (bild_i >= bilder.length) {
		bild_i = 0
	}

	document.getElementById("anka").src = bilder[bild_i]
}
*/

var deg = 0
var fps = 60
var speed = 0.5

function rotate() {
	deg = deg + 360 * speed / fps
	if (deg > 360) {
		deg = 0
	}
	
	objs = document.getElementsByClassName("rot")
	for (i=0; i<objs.length; i++) {
		objs[i].style.setProperty("rotate", "" + deg + "deg")
	}
	
	clearTimeout()
	setTimeout(rotate, 1000 / fps)
}