function openColorPicker(){
  document.getElementById("colorize-color-picker").click();
}

function makeColorize(elem){
  colorize(elem.value);
}

function colorize(color){
  var box = document.getElementById('change');
  box.style.background = color;
}

function loadtemplate(){
  var num = sessionStorage.getItem('num');
  console.log(num)

  if (num == 1){
    console.log("squarebox");
    document.getElementById('cube').checked = true;
    document.getElementById('medium').checked = true;
    document.getElementById('matte').checked = true;
    colorize("#1aa321")
  }
  else if (num == 2){
    console.log("rectanglebox")
    document.getElementById('rect').checked = true;
    document.getElementById('medium').checked = true;
    document.getElementById('glossy').checked = true;
    
    changeToMedium();
    changeToRectangular();
    colorize("#000000")
  }
  else if (num == 3){
    console.log("slimrectangle")
    document.getElementById('rect').checked = true;
    document.getElementById('small').checked = true;
    document.getElementById('flat').checked = true;
    
    changeToSmall()
    changeToRectangular()
    colorize("#ffffff")
  }
  else if (num == 4){
    console.log("blank")
    document.getElementById('cube').checked = true;
    document.getElementById('small').checked = true;
    document.getElementById('matte').checked = true;
    changeToSmall()
    colorize("#ffffff")
  }
  else{
    console.log("else")
    document.getElementById('cube').checked = true;
    document.getElementById('large').checked = true;
    document.getElementById('glossy').checked = true;
    colorize("#ffffff")
  }
}

function loadstyle(a){
  num = a
  console.log(a + " : " + num)
  sessionStorage.setItem('num', a);
  document.getElementById('cube').checked = false;
  document.getElementById('rect').checked = false;
  document.getElementById('small').checked = false;
  document.getElementById('medium').checked = false;
  document.getElementById('large').checked = false;
  document.getElementById('matte').checked = false;
  document.getElementById('glossy').checked = false;
  document.getElementById('flat').checked = false;
}