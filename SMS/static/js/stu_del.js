document.getElementById("use_sid").style.display = "none";
document.getElementById("use_email").style.display = "none";
document.getElementById("others").style.display = "none";

document.getElementById("type").addEventListener("change", () => {
  document.getElementById("use_sid").style.display = "none";
  document.getElementById("use_email").style.display = "none";
  document.getElementById("others").style.display = "none";

  if (document.getElementById("type").value == "id") {
    document.getElementById("use_sid").style.display = "block";
  } else if (document.getElementById("type").value == "email") {
    document.getElementById("use_email").style.display = "block";
  } else if (document.getElementById("type").value == "others") {
    document.getElementById("others").style.display = "block";
  }
});

function func() {
  document.getElementById("message").innerHTML =
    "Please check the student details will be lost";
}
