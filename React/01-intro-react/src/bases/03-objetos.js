const persona={
    nombre: "Tony",
    apellido: "Stark",
    edad: 45,
};

//console.log(persona);
console.table(persona);

const persona2={...persona};
persona2.nombre="peter"

console.log(persona);
console.log(persona2);