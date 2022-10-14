let launch = document.querySelectorAll("#launch_button");
let text = document.querySelector("#text");
let inputVuln = document.querySelector("#vuln_input");

launch.item(0).addEventListener("click", () => {
    console.log("Sending request")
    vuln_name = inputVuln.value
    fetch("/rest/deploy/" + vuln_name).then(function (response) {
        return response.json();
    }).then(function (data) {
        text.insertAdjacentText('beforeend', data.message + " " + data.ip + " ")
        console.log(data.remote_message);
    }).catch(function () {
        console.log("Booo");
    });
})