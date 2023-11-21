window.addEventListener("load", () => {
  const form = document.querySelector("#form-video");
  const btn = document.querySelector("#submit-btn");

  if (btn) {
    btn.addEventListener("click", async (e) => {
      e.preventDefault();
      var formData = new FormData(form);
      var obj = {};
      formData.forEach((value, key) => {
        obj[key] = value;
      });
      var json = JSON.stringify(obj);
      document.querySelector(".signal-download").classList.add("block");
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
      });
    });
  }
});
