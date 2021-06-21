var MAX_VALUE = 1000;

function thread1(value, maxValue){
    console.log(value);
    value++;
  
    //Continue execution
    if(value<=maxValue)
        setTimeout(()=>{ thread1(value, maxValue); }, 0);
}

function thread2(value, maxValue){
    console.log(value);
    value++;
	
    if(value<=maxValue)
        setTimeout(()=>{ thread2(value, maxValue); }, 0);
}

function thread3(value, maxValue){
    console.log(value);
    value++;
	
    if(value<=maxValue)
        setTimeout(()=>{ thread3(value, maxValue); }, 0);
}
function thread4(value, maxValue){
    console.log(value);
    value++;
	
    if(value<=maxValue)
        setTimeout(()=>{ thread4(value, maxValue); }, 0);
}



thread1(0, MAX_VALUE);
thread2(0, MAX_VALUE);
thread3(0, MAX_VALUE);
thread4(0, MAX_VALUE);
