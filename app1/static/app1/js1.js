var counter = 1;
setInterval(function () {
  document.getElementById("radio" + counter).checked = true;
  counter++;
  if (counter > 4) {
    counter = 1;
  }
}, 5000);

$(document).ready(function () {
  $(".1111").animate({ height: "110px" }, "50");
  $(".1111").animate({ height: "80px" }, "50");
});

$(document).ready(function () {
  $(".jq1").click(function () {
    $(".jq11").slideToggle();
  });
});

