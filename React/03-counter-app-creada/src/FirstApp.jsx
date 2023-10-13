export function App(){
    //no se recomienda usar clases
    //forma mas facil de hacer: document.createElement...
    return (
        //esto de abajo representa un fragmento
        <> 
            <h1>Hola David</h1>
            <p>subtitulo</p>
            <p>{1+5}</p>
        </>
    )
}

//tambien se puede exportar asi
//export default App