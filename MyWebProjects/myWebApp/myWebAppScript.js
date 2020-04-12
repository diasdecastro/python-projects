function hello(){
    var el = document.createElement("h1");
    var txt = document.createTextNode("Hello Again");
    el.appendChild(txt);
    var tag = document.getElementById("id1")
    tag.appendChild(el)
};

function createUnsortedArray(){
    arr = new Array();
    for(var i = 0; i < 200; i++){
        arr[i] = i + 1;
    }
    arr.sort(() => Math.random() - 0.5);
    return arr
};

function drawLines(){
    arr = createUnsortedArray();
    for(var i = 0; i < arr.length; i++){
        drawLine(arr[i]*2.7);
    }

};

function drawLine(length){  
    var my_length = parseInt(length) + "px";
    var line = document.createElement("span");
    line.className = "line";    
    line.style.borderLeft = "3px solid black";
    line.style.height = my_length;
    line.style.position = "relative";
    line.style.float = "left";
    line.style.margin = "0.1px";
    var tag = document.getElementById("contentBox");    
    tag.appendChild(line);
};