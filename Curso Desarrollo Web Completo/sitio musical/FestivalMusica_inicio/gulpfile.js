const {src, dest, watch}=require("gulp");
const sass=require("gulp-sass")(require('sass'));

function css(done){
    //identificar el archivo sass (src)
    //compilar
    //almacenar en el disco duro (dest)

    src('src/scss/app.scss')
    .pipe(sass() )
    .pipe(dest("build/css"));

    done();//call back que avisa a gulp cuando lleguemos al final
} 

function dev(done){
    watch("src/scss/app.scss", css);
    done();
}

exports.css=css;
exports.dev=dev;

//se pueden llamar para compilar npx gulp (nombre tarea opcional)
// o se puede colocar npm run +(lo que se coloque a la variable en package.json)