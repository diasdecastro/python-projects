import {bubbleSort} from "./algorithms";
import {quickSort} from "./algorithms";
import {heapsort} from "./algorithms";

export function drawLines(arr, x, y, rightPivot, leftPivot){
    let array = arr.slice();
    let container = document.getElementById("centerContent");
    let line = undefined;
    container.innerHTML = '';
    for(let i = 0; i < array.length; i++){
        let my_length = (array[i]/6.7).toString() + "em";
        line = document.createElement("div");
        line.className = "line";
        if(i === x || i === y){
            line.style.borderLeftWidth = (1/6.5).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "red";
        }
        else if(i === rightPivot){
            line.style.borderLeftWidth = (1/6.5).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "aqua";
        }
        else if(i === leftPivot){
            line.style.borderLeftWidth = (1/6.5).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "orange";
        }
        else{
            line.style.borderLeftWidth = (1/6.5).toString() + "em";
            line.style.borderLeftStyle = "solid";
            line.style.borderLeftColor = "black";
        }        
        line.style.height = my_length;
        container.appendChild(line);
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
var initialArray;

export function createUnsortedArray(){
    let arr = [];
    for(let i = 0; i < 200; i++){
        arr[i] = i + 1;
    }
    arr.sort(() => Math.random() - 0.5);
    initialArray = arr.slice();
    return arr;
}

export function changeChannel(){
    let container = document.getElementById("centerBox");
    let header = document.getElementById("algInfo")
    switch (container.className) {
        case "tvOnCh0":
            container.className = "tvOnCh1";
            header.innerHTML = "Bubble Sort";
            break;
        case "tvOnCh1":
            container.className = "tvOnCh2";
            header.innerHTML = "Quicksort";
            break;
        case "tvOnCh2":
            container.className = "tvOnCh3";
            header.innerHTML = "Heapsort";
            break;
        case "tvOnCh3":
            container.className = "tvOnCh0";
            header.innerHTML = "Select Algorithm";
            break;

    }
}

export function changePower(){
    let container = document.getElementById("centerBox");
    if(container.className === "tvOffCh0"){
        container.className = "tvOnCh0";
    }
    else{
        container.className = "tvOffCh0";
        document.getElementById("centerContent").innerHTML = "";
    }
}

export async function sortArray(arr){
    let container = document.getElementById("centerBox");
    if(container.className === "tvOnCh1"){
        await bubbleSort(arr, 0);
    }
    else if(container.className === "tvOnCh2"){
        await quickSort(arr, 0, arr.length -1, 1);
    }
    else if(container.className === "tvOnCh3"){
        await heapsort(arr);
    }
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*Array.prototype.swap = function(x, y) {
    let b = this[x];
    this[x] = this[y];
    this[y] = b;
    return this;
}

function sleep(callback, arr, x, y, rightPivot, leftPivot, ms) {
    setTimeout(() => {callback(arr, x, y, rightPivot, leftPivot)}, ms)
}

async function bubbleSort(arr, speed){
    for(let i = arr.length; i > 1; i--){
        for(let j = 0; j < arr.length - 1; j++){
            if(arr[j] > arr[j + 1]){
                arr.swap(j, j+1);
                const arrCopy = arr.slice();
                await sleep(drawLines,arrCopy, j, j+1, -1, -1, speed);
            }
        }       
    }
    setTimeout(() => {drawLines(arr, -1, -1);});
}

async function quickSort(arr, firstElIndex, lastElIndex, speed){
    let array = arr;
    let currentIndex = 0;
    async function partition(firstElIndex, lastElIndex) {
        let i = firstElIndex;
        let j = lastElIndex;
        let pivot = array[lastElIndex];
        while(i < j){
            while(i < lastElIndex && array[i] < pivot){
                const iCopy = i;
                const lastCopy = lastElIndex;
                i++;
                const arrCopy = array.slice();
                await new Promise(resolve => setTimeout(resolve, speed));
                drawLines(arrCopy, iCopy, -1, lastCopy, -1);
            }

            while(j > firstElIndex && array[j] >= pivot){
                const jCopy = j;
                const firstCopy = firstElIndex;
                j--;
                const arrCopy = array.slice();
                await new Promise(resolve => setTimeout(resolve, speed));
                drawLines(arrCopy, -1, jCopy,-1, firstCopy);
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
        currentIndex = await partition(firstElIndex, lastElIndex);
        await quickSort(array, firstElIndex, currentIndex - 1, speed);
        await quickSort(array, currentIndex + 1, lastElIndex, speed);
    }
    setTimeout(() => {drawLines(array, -1, -1);});
    return new Promise(resolve => setTimeout(resolve, 0));
}


async function heapsort(arr, speed) {
    let myArray = arr.slice();
    let end = myArray.length - 1;

    await heapify(myArray, myArray.length);
    console.log("my array v0");
    console.log("" + myArray);


    while(end > 0){
        myArray.swap(0, end);
        await siftDown(myArray, 0, end);
        end--;
        //drawing
        let myArrayCopy = myArray.slice()
        await new Promise(resolve => setTimeout(resolve, 10));
        drawLines(myArrayCopy, 0, -1,end, -1);
    }
    await new Promise(resolve => setTimeout(resolve, 10));
    drawLines(myArray, -1, -1,-1, -1);


    async function heapify(array, size){
        let start = Math.floor(size/2);
        while(start >= 0){
            await siftDown(array, start, end);
            start--;
        }
    }

    async function siftDown(array, start, end){
        let root = start;
        let child = root * 2 + 1; //left child
        let potentialParent = root;
        while(root < Math.floor(end /2)){
            if(array[potentialParent] < array[child]){
                potentialParent = child;
            }
            if(child + 1 < end && array[potentialParent] < array[child + 1]){
                potentialParent = child + 1;
            }
            if(potentialParent === root){
                break;
            }
            else{
                array.swap(root, potentialParent);
                const myArrayCopy = array.slice();
                await new Promise(resolve => setTimeout(resolve, 10));
                drawLines(myArrayCopy, root, -1,potentialParent, -1);
                root = potentialParent;
                child = root * 2 + 1;
            }
        }
    }
}*/

// TODO: code in mehrere dataien teilen
// TODO: controls ist macht nichts
// TODO: farbverhältnisse