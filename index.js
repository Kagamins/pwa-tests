if("serviceWorker" in  navigator){
    navigator.serviceWorker.register("sw.js").then(regsistration=>{
        console.log("SW Regestired");
        console.log(regsistration);
    }).catch(error=>{
        console.log("sw Registration Failed!");
        console.log(error);
    });
}