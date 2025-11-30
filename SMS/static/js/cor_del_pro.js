document.getElementById("pid").style.display = "none";
document.getElementById("pname").style.display = "none";
document.getElementById("detai").style.display = "none";
document.getElementById("get").addEventListener("change", () => {
  let g = document.getElementById("get");
  document.getElementById("detai").style.display = "none";
  if (g.value === "pid") {
    document.getElementById("pname").style.display = "none";
    document.getElementById("detai").style.display = "block";
    document.getElementById("pid").style.display = "block";
  } else if (g.value === "pname") {
    document.getElementById("pid").style.display = "none";
    document.getElementById("detai").style.display = "block";
    document.getElementById("pname").style.display = "block";
  }
});
