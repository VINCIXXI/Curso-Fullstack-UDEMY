const personajes=["goku","vegeta","trunks"];
//forma vieja
console.log(personajes[0]);
console.log(personajes[1]);

//mejor
const [,p2]=personajes;
console.log(p2);

const retornaArreglo=()=>{
    return ["ABC",123];
}

const [letras,numeros]=retornaArreglo();
console.log(letras,numeros);

//ejercicio
const useState=(valor)=>{
    return[valor, ()=>{console.log("Hola mundo")}];
}

//desestructuracion
const [nombre,setNombre]=useState("goku");

console.log(nombre);
setNombre();

