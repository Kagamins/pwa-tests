if("serviceWorker" in  navigator){
    navigator.serviceWorker.register("sw.js").then(regsistration=>{
        console.log("SW Regestired");
        console.log(regsistration);
    }).catch(error=>{
        console.log("sw Registration Failed!");
        console.log(error);
    });
}

     function addData(){
     document.getElementById("tablebody").SetInnerHtml("<tr>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="seventhperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="sixthperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="fithperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="fourthperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="thirdperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="secondperiod"></div></td>
        <td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="firstperiod"></div></td>
        <td></td>
        <td>١١د١</td>
        <td>dummy</td>
      </tr>");
     }
