//por naturaleza son asincronas
const promesa=new Promise((resolve,reject)=>{
    setTimeout(()=>{
        

        resolve();
        console.log("2 segundos despues")
    },2000)
});

//then significa que se fue exitoso
promesa.then(()=>{
    console.log("Then de la promesa")
})
.catch(err=>console.warn(err));

