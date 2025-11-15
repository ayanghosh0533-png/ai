const video = document.getElementById("video");
const resultText = document.getElementById("result");

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => { video.srcObject = stream; });

setInterval(async () => {
    let canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    let ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    let base64Image = canvas.toDataURL("image/jpeg");

    let res = await fetch("/detect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ image: base64Image })
    });

    let data = await res.json();
    resultText.innerText = `Faces detected: ${data.faces}`;
}, 500);
