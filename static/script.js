// const = constante Variable 
// let = veränderliche Variable , dynamische Typisierung 

// funktionssyntax: 
// function add(a,b){ return a+b; } 
// wichitge Funktionen : 
// document.getElementById("pv-wert") suche das HTML Element mit dieser ID
// fetch(... )  hole Daten von Flask 
// setIntervall() führe diese Funktion alle .. ms aus 
// Objekte const data ={
    // pv:5240; .... } 
    // data.pv // abfragbar 
// DOM Document Object Model 


// gets fetch(url, )
async function getData(){
const response = await fetch("/api/data");
 // response sind noch nicht die Daten sondern das Antwort Obj. des Browsers
 // zweimal await: fetch()-> HTTP Antwort -> response.json() -> javaScript Object
const data = await response.json(); 
console.log(data); 
return data; 
} 
async function updateDash(){


const data = await getData(); 
const date = new Date();

const pv = document.getElementById("pv_wert") ; 
const haus = document.getElementById("haus_wert"); 
const bat = document.getElementById("bat_wert");
const netz = document.getElementById("netz_wert"); 
const soc = document.getElementById("soc_wert");
const date_t = document.getElementById("date"); 
const time_t = document.getElementById("time"); 
pv.textContent = data.p_pv+ " W";
haus.textContent = data.p_haus+ " W";
bat.textContent = data.p_bat+ " W";
netz.textContent = data.p_netz+ " W";
soc.textContent = data.soc+ " %";
date_t.textContent = date.getUTCDate()+"." +(date.getMonth()+1)+ "."+ date.getFullYear(); 
time_t.textContent = date.getHours() + ":"+ date.getMinutes(); 
}

setInterval(updateDash, 1000); 

 
