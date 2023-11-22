window.addEventListener("load", () => {
  const downloadVideo = async (form) => {
    var formData = new FormData(form);
    var obj = {};
    formData.forEach((value, key) => {
      obj[key] = value;
    });
    var json = JSON.stringify(obj);
    document.querySelector(".signal-download").classList.add("block");
    btn.disabled = true;
    await fetch(form.getAttribute("action"), {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-type": "application/json",
      },
      body: json,
    }).then(() => {
      document.querySelector(".signal-download").classList.remove("block");
      document.querySelector(".signal-success").classList.add("block");

      setTimeout(() => {
        document.querySelector(".signal-success").classList.remove("block");
        form.querySelectorAll(".form-control").forEach((input) => {
          input.value = "";
        });
        btn.disabled = false;
      }, 3500);
    });
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
  inputs.forEach((input, index) => {
    input.classList.remove("input-error");
    msgsErros[index].style.display = "none";
    if (input.value === "") {
      input.classList.add("input-error");
      msgsErros[index].style.display = "block";
      return false;
    }
    return true;
  });
};
