function jonFunction() {
	console.log("hello")
}

let input = document.getElementById("inputJS")
let output = document.getElementById("outputJS")
let b = document.getElementById("btnJS")

b.addEventListener("click", () => {
	console.log(input.value)
	output.innerText = "input:" + input.value
})
