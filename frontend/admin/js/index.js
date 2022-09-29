let launch = document.querySelectorAll("#launch_button");
let text = document.querySelector("#text");

launch.item(0).addEventListener("click", () => {
    console.log("Sending request")
    fetch("/rest/hello").then(function (response) {
        return response.json();
    }).then(function (data) {
        text.insertAdjacentText('beforeend', data.message + " " + data.ip + " ")
        console.log(data);
    }).catch(function () {
        console.log("Booo");
    });
})