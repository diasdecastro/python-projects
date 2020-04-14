function drawLine(length){  
    var my_length = parseInt(length) + "px";
    var line = document.createElement("span");
    line.className = "line";    
    line.style.borderLeft = "3px solid black";
    line.style.height = my_length;
    line.style.position = "relative";
    line.style.margin = "1px";
    var tag = document.getElementById("contentBox");    
    tag.appendChild(line);
}

function drawLines(arr){
    container = document.getElementById("contentBox");
    container.innerHTML = '';
    for(var i = 0; i < arr.length; i++){ 
        drawLine(arr[i]*2.7);
    }
}

function createUnsortedArray(){
    arr = new Array();
    for(var i = 0; i < 200; i++){
        arr[i] = i + 1;
    }
    arr.sort(() => Math.random() - 0.5);
    return arr;
}

function generateArray(){
    container = document.getElementById("contentBox");
    container.innerHTML = '';
    arr = createUnsortedArray();
    drawLines(arr);
}

function bubbleSort(arr){
    container = document.getElementById("contentBox");    
    Array.prototype.swap = function(x, y){
        var b = this[x];
        this[x] = this[y];
        this[y] = b;
        return this;
    }   
    for(var i = arr.length; i > 1; i--){
        for(var j = 0; j < arr.length - 1; j++){
            if(arr[j] > arr[j + 1]){
                arr.swap(j, j+1);                                                  
            }                        
        }
        setTimeout(function(){drawLines(arr);}, 1);         
    }    
    /* container = document.getElementById("contentBox");
    container.innerHTML = ''; 
    return drawLines(arr) */
}
