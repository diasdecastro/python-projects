
export function drawLines(arr, x, y, rightPivot, leftPivot){
    let array = arr.slice();
    let container = document.getElementById("centerContent");
    let line = undefined;
    container.innerHTML = '';
    for(let i = 0; i < array.length; i++){
        let my_length = (array[i]/(7.5)).toString() + "em";
        line = document.createElement("div");
        line.className = "line";
        if(i === x || i === y){
            line.style.borderLeftWidth = (0.13).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "red";
        }
        else if(i === rightPivot){
            line.style.borderLeftWidth = (0.13).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "aqua";
        }
        else if(i === leftPivot){
            line.style.borderLeftWidth = (0.13).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "orange";
        }
        else{
            line.style.borderLeftWidth = (0.13).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "blue";
        }        
        line.style.height = my_length;
        container.appendChild(line);
    }
}