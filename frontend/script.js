document.addEventListener("DOMContentLoaded", function () {
  const frm = document.querySelector("form");

  const result = document.querySelector("#inResult");

  const textInput = document.querySelector("#inText");

  frm.addEventListener("submit", (e) => {
    e.preventDefault();

    const textoDigitado = textInput.value;

    fetch("/conversor", {
      method: "POST",

      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },

      body: "texto=" + encodeURIComponent(textoDigitado),
    })
      .then((response) => response.blob())

      .then((blob) => {
        const objectURL = URL.createObjectURL(blob);

        const audioPlayer = document.createElement("audio");

        audioPlayer.controls = true;

        audioPlayer.src = objectURL;
      })

      .catch((error) => {
        console.error("Erro ao converter o texto:", error);

        result.innerHTML =
          "<p>Ocorreu um erro ao converter o texto para áudio.</p>";
      });
  });
});
