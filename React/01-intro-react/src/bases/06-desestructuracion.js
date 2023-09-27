//desestructuracion o Asignacion
const persona={
    nombre: "Tony",
    edad: 45,
    clave: "Ironman"
}
/*
console.log(persona.nombre);
console.log(persona.edad);
console.log(persona.clave);
*/

//otra forma
const {nombre, edad}=persona;

console.log(nombre);
console.log(edad);
