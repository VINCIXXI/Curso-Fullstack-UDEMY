const nombre="david";
const apellido="rodriguez";

//const nombreCompleto=nombre+' '+apellido;
const nombreCompleto=`
${nombre}
${apellido}
`;

console.log(nombreCompleto)

function getSaludo(){
    return "Hola"
}

console.log(`Este es un texto: ${getSaludo()}`)