const click_submit = () => {
  json = create_json(new FormData(document.querySelector("form")));

  fetch("/result", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: json,
  }).then((res) => {
    res.text().then((data) => {
      var element = document.getElementById("results");
      element.style.display = "inline";
      if (data === "Positive") {
        element.style.color = "#ce1205";
        element.innerHTML = "Result: Positive";
      } else if (data === "Negative") {
        element.style.color = "#0051ff";
        element.innerHTML = "Result: Negative";
      }
    });
  });
};

const create_json = (formData) => {
  var object = {};
  formData.forEach((value, key) => (object[key] = value));
  return JSON.stringify(object);
};
