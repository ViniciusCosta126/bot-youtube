window.addEventListener("load", () => {
  const downloadVideo = async (form) => {
    var formData = new FormData(form);

    document.querySelector(".signal-download").classList.add("block");
    btn.disabled = true;

    try {
      const response = await fetch(form.getAttribute("action"), {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorMessage = await response.json();
        throw new Error(errorMessage.erro);
      }

      document.querySelector(".signal-download").classList.remove("block");
      const success = document.querySelector(".signal-success");
      const resposta = await response.json();
      success.querySelector("p").innerHTML = resposta.message;
      success.classList.add("block");
      setTimeout(() => {
        document.querySelector(".signal-success").classList.remove("block");

        form.querySelectorAll(".form-control").forEach((input) => {
          input.value = "";
        });

        btn.disabled = false;
      }, 3500);
    } catch (error) {
      document.querySelector(".signal-download").classList.remove("block");
      var errorMsg = document.querySelector(".signal-error");
      errorMsg.querySelector("p").innerHTML = error.message;
      errorMsg.classList.add("block");
      setTimeout(() => {
        btn.disabled = false;
        errorMsg.classList.remove("block");
      }, 3000);
    }
  };

  const form = document.querySelector("#form-video");
  const btn = document.querySelector("#submit-btn");

  if (btn && form) {
    const msgsErros = form.querySelectorAll(".msg-erro");
    const inputs = form.querySelectorAll(".form-control");
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      var inputsValidos = validaForms(inputs, msgsErros);
      if (inputsValidos) {
        downloadVideo(form);
      }
    });
  }
});

const validaForms = (inputs, msgsErros) => {
  let inputsValidos = true;

  for (let i = 0; i < inputs.length; i++) {
    if (inputs[i].value.trim() === "") {
      inputs[i].classList.add("input-error");
      msgsErros[i].style.display = "block";
      inputsValidos = false;
    } else {
      inputs[i].classList.remove("input-error");
      msgsErros[i].style.display = "none";
    }
  }
  return inputsValidos;
};
