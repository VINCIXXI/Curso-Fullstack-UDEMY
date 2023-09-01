async function crearPost(titulo, contenido) {
    try {
        let respuesta = await fetch('https://jsonplaceholder.typicode.com/posts',{
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                title: titulo,
                body: contenido,
                uderId: 1,
            }),
        })

        if(!respuesta.ok) {
            throw new Error("Error en la solicitud: " + respuesta.statusText);
        }

        let data = await respuesta.json();
        console.log("Registro creado: ", data);

    } catch(error) {
        console.error("Algo salio mal al crear el registro: ", error)
    }
}


crearPost("Mi titulo de ejemplo", "Mi contenido de ejemplo");

/*Ejercicio */
/*Desarrolla la función agregarRegistro, donde utilizando la herramienta fetch realice una solicitud POST al servidor con URL https://api.restful-api.dev/objects para agregar un nuevo registro a la API. Para construir el campo body de la petición, los campos del objeto que la API espera son name y data, a los cuales se le deben asignar los parámetro de la función, nombre y datos, respectivamente.
El resultado de la petición será un objeto JSON con los datos del nuevo registro. Esta respuesta se debe imprimir en consola. */

/*Una manera de solucionar */
/*function agregarRegistro(nombre, datos) {
    fetch('https://api.restful-api.dev/objects',{
        method: "POST",
        headers: {
            "Content-Type":"application/json",
        },
        body: JSON.stringify({
            name: nombre,
            data: datos
        })
    })
    .then(res=>res.json());
}
agregarRegistro(nombre,datos);*/

/*Otra manera */
/*function agregarRegistro(nombre, datos) {
    fetch('https://api.restful-api.dev/objects', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: nombre,
            data: datos
        })
    })
    .then(respuesta => respuesta.json())
    .then(data => console.log(data))
    .catch(error => console.error(error))
}*/