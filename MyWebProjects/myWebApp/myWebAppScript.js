function drawLines(arr, x, y, rightPivot, leftPivot){
    let array = arr.slice();
    let container = document.getElementById("centerContent");
    let line = undefined;
    container.innerHTML = '';
    for(let i = 0; i < array.length; i++){
        let my_length = (array[i]/6.7).toString() + "vw";line = document.createElement("div");
        line.className = "line";
        if(i === x || i === y){
            line.style.borderLeft = (1/7).toString() + "vw solid red";
        }
        else if(i === rightPivot){
            line.style.borderLeft = (1/7).toString() + "vw solid aqua";
        }
        else if(i === leftPivot){
            line.style.borderLeft = (1/7).toString() + "vw solid orange";
        }
        else{
            line.style.borderLeft = (1/7).toString() + "vw solid black";
        }        
        line.style.height = my_length;
        container.appendChild(line);
    }
}

function createUnsortedArray(){
    let arr = [];
    for(let i = 0; i < 200; i++){
        arr[i] = i + 1;
    }
    arr.sort(() => Math.random() - 0.5);
    return arr;
}

function generateArray(){
    let container = document.getElementById("centerContent");
    container.innerHTML = '';
    let arr = createUnsortedArray();
    drawLines(arr, -1, -1);
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Array.prototype.swap = function(x, y) {
    let b = this[x];
    this[x] = this[y];
    this[y] = b;
    return this;
}
function bubbleSort(arr){
    for(let i = arr.length; i > 1; i--){
        for(let j = 0; j < arr.length - 1; j++){
            if(arr[j] > arr[j + 1]){
                arr.swap(j, j+1);
                const arrCopy = arr.slice();                          
                setTimeout(() => {drawLines(arrCopy, j, j+1);});
            }
        }       
    }
    setTimeout(() => {drawLines(arr, -1, -1);});
}

function quickSort(arr, firstElIndex, lastElIndex){
    let array = arr;
    let currentIndex = 0;
    function partition(firstElIndex, lastElIndex) {
        let i = firstElIndex;
        let j = lastElIndex;
        let pivot = array[lastElIndex];
        while(i < j){
            while(i < lastElIndex && array[i] < pivot){
                const iCopy = i;
                const lastCopy = lastElIndex;
                i++;
                const arrCopy = array.slice();
                setTimeout(() => {
                    drawLines(arrCopy, iCopy, -1, lastCopy, -1);
                });
            }

            while(j > firstElIndex && array[j] >= pivot){
                const jCopy = j;
                const firstCopy = firstElIndex;
                j--;
                const arrCopy = array.slice();
                setTimeout(() => {
                    drawLines(arrCopy, -1, jCopy,-1, firstCopy);
                });
            }

            if(i < j){
                array.swap(i, j);
            }
        }
        if(array[i] > pivot){
            array.swap(i, lastElIndex);
        }
        return i;
    }
    if(firstElIndex < lastElIndex){
        currentIndex = partition(firstElIndex, lastElIndex);
        quickSort(array, firstElIndex, currentIndex - 1);
        quickSort(array, currentIndex + 1, lastElIndex);
    }
    setTimeout(() => {drawLines(array, -1, -1);}, 1000);
}