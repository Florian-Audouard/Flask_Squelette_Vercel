fetch("/getDatabase")
	.then((res) => {
		return res.json();
	})
	.then((data) => {
		document.querySelector("#databaseText").innerText = data[0];
	});
