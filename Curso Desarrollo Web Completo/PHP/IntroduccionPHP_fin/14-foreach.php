<?php include 'includes/header.php';

$productos = [
    [
        'nombre' => 'Tablet', 
        'precio' => 200,
        'disponible' => true
    ],
    [
        'nombre' => 'Television 24"', 
        'precio' => 300,
        'disponible' => true
    ],
    [
        'nombre' => 'Monitor Curvo', 
        'precio' => 400,
        'disponible' => false
    ]
];

foreach( $productos as $producto) { ?>
    <li>
        <p>Producto: <?php echo $producto['nombre']; ?> </p>
        <p>Precio: <?php echo "$" . $producto['precio']; ?> </p>
        <p><?php echo ($producto['disponible']) ? 'Disponible' : 'No Disponible';//esto es lo mismo a lo que esta abajo  ?> </p>
        
        <?php
            //esto es lo mismo a lo que está arriba
            if ($producto['disponible']){
                echo "<p>Disponible</p>";
            } else {
                echo"<p>No Disponible</p>";
            }
        ?>
    </li>
    <?php
}



include 'includes/footer.php';