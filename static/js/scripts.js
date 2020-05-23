function copyFunction() {
  var copyText = document.getElementById('imageurl');
  copyText.select();
  document.execCommand("copy");
  alert("image url copied to clipboard");
}