window.addEventListener("load", () => {
  const downloadVideo = (btn, form) => {
    btn.addEventListener("click", async (e) => {
      e.preventDefault();
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
    });
  };

  const form = document.querySelector("#form-video");
  const btn = document.querySelector("#submit-btn");

  if (btn && form) {

    
    downloadVideo(btn, form);
  }

});
