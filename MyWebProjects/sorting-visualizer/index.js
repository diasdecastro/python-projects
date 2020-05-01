require("@babel/polyfill"); // for async/await

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import {bubbleSort, quickSort, heapsort} from "./modules/algorithms";
import {drawLines} from "./modules/renderLines";

var initialArray;

// adding event listeners
document.getElementById("power").addEventListener("click", changePower);
document.getElementById("channel").addEventListener("click", changeChannel);
document.getElementById("generateArray").addEventListener("click", () => {    
    createUnsortedArray()
    drawLines(initialArray);    
}); //anonymous function
document.getElementById("sortArray").addEventListener("click", async () => {
    sortArray(initialArray);
});


function createUnsortedArray(){
    let arr = [];
    for(let i = 0; i < 200; i++){
        arr[i] = i + 1;
    }
    arr.sort(() => Math.random() - 0.5);
    initialArray = arr.slice();
    return initialArray;
}

function changeChannel(){
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

function changePower(){
    let container = document.getElementById("centerBox");
    if(container.className === "tvOffCh0"){
        container.className = "tvOnCh0";
    }
    else{
        container.className = "tvOffCh0";
        document.getElementById("centerContent").innerHTML = "";
    }
}

async function sortArray(arr){
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

