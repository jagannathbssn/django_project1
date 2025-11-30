document.getElementById("use_sid").style.display = "none";
document.getElementById("use_email").style.display = "none";
document.getElementById("others").style.display = "none";

document.getElementById("type").addEventListener("change", () => {
  let val = document.getElementById("type").value;

  document.getElementById("use_sid").style.display = "none";
  document.getElementById("use_email").style.display = "none";
  document.getElementById("others").style.display = "none";

  if (val === "id") {
    document.getElementById("use_sid").style.display = "block";
  } else if (val === "email") {
    document.getElementById("use_email").style.display = "block";
  } else if (val === "others") {
    document.getElementById("others").style.display = "block";
  }
});

function clr() {
  const url = "/student/student-updation/";
  window.location.href = url;
}

document.getElementById("photo").addEventListener("change", function (e) {
  let img = document.getElementById("preview");
  img.src = URL.createObjectURL(e.target.files[0]);
  img.style.display = "block";
});
