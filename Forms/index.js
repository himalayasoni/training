var fopt="";
var fname,fid,ftype;
function myFunction() {
  fname = document.getElementById("fname").value;
  fid = document.getElementById("fid").value;
  ftype = document.getElementById("ftype").value;
  //var fopt;
  
  if (ftype === "select"){
     document.getElementById("addmore").style.display="inline";
     document.getElementById("textbox").style.display="inline";
     document.getElementById("close").style.display="inline";
  }
  else{
     toParse();
  }
}

function toParse(){
   let notesStorage = localStorage.getItem("storeditems") ? JSON.parse(localStorage.getItem("storeditems")) : [];
  
   notesStorage.push({name:fname,id:fid,type:ftype,opt:fopt});
  
   localStorage.setItem("storeditems",JSON.stringify(notesStorage));
  
   console.log(notesStorage);

   addToTable (fname, fid, ftype, fopt);
}

function additem(){
   var inputval=document.getElementById("textbox").value;
   fopt+=inputval+",";
   document.getElementById("textbox").value='';
}


function closeitem(){
  //console.log("hi")
  document.getElementById("addmore").style.display="none";
  document.getElementById("textbox").style.display="none";
  document.getElementById("close").style.display="none";
  toParse();
  // addToTable(fname,fid,ftype,fopt);
}


function addToTable (fname, fid, ftype, fopt){
  var nrow = "<tr>";
  nrow += "<td>" + fname + "</td>";
  nrow += "<td>" + fid + "</td>";
  nrow += "<td>" + ftype + "</td>";
  nrow += "<td>" + fopt + "</td>";
  nrow+="</tr>"

  document.getElementById ("tab").innerHTML += nrow;
}


function codeGenerator (storeditems){
  var userdata = JSON.parse (localStorage.getItem ('storeditems')) ;
  console.log(userdata)
  var str = "";
  str = "<form>\n"; 
  for (var i=0; i<userdata.length; i++){
    str += "<label for="+"'"+ userdata[i].id + "'>" + userdata[i].name+ "</label>\n";
    
    if (userdata[i].type === "select"){
      var arr = userdata[i].opt.split(',');
      str += "<select name="+ "'" + userdata[i].id + "'" + "id="+"'"+userdata[i].id+"'>\n";
      
      for (var i=0; i<arr.length-1; i++){
        str += "<option value="+"'"+arr[i]+"'>"+arr[i]+"</option>\n";
      }

      str += "</select>\n";
    }
    
    else{
      str += "<input type="+"'"+userdata[i].type+"'"+"id="+"'"+userdata[i].id+"'"+"name="+"'"+userdata[i].id+"'>\n";
    }
  }
  str+="</form>\n"
  document.getElementById ("code").innerText += str;
  localStorage.clear();
}





