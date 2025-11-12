function reg() {
  const url = "/student/student-registration/";
  window.location.href = url;
}

function up() {
  const url = "/student/updating-student-details";
  window.location.href = url;
}

function cls_sel() {
  const opt = document.getElementById("cls");
  const inp = document.getElementById("clsname");
  console.log(opt);
  inp.value = opt.value;
}
