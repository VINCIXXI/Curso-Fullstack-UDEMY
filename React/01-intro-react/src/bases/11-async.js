/*
const getImagenPromesa=()=>{
    return new Promise((resolve,reject)=>{
        resolve("https://sfasfasfas.com")
    })
} 
getImagenPromesa().then(console.log)
*/

const getImage=async()=>{
    const apiKey="i30BvwN8bVzZwjHEKUaqSTOJkADahGFa";
    const resp=await fetch(`https://api.giphy.com/v1/gifs/random?api_key=${apiKey}`);
    const data= await resp.json();

    console.log(data);
}

getImage();