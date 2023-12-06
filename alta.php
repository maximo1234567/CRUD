<?php

include_once("conn.php");

$objConexion = new Conexion();

class Estudiante {
    public $dni;
    public $sexo;
    public $nombre;
    public $apellido;

    function guardar_datos() {
        global $objConexion;

        $sql = "INSERT INTO estudiantes (dni, sexo, nombres, apellidos) VALUES ('$this->dni', '$this->sexo', '$this->nombre', '$this->apellido')";
        $objConexion->query($sql);
    }
}

$estu = new Estudiante();

$dni = htmlspecialchars($_GET["dni"], ENT_QUOTES);
$sexo = htmlspecialchars($_GET["sexo"], ENT_QUOTES);
$nombre = htmlspecialchars($_GET["nombres"], ENT_QUOTES);
$apellido = htmlspecialchars($_GET["apellidos"], ENT_QUOTES);

if (($dni != "") and ($sexo != "") and ($nombre != "") and ($apellido != "")) {
    $estu->dni = $dni;
    $estu->sexo = $sexo;
    $estu->nombre = $nombre;
    $estu->apellido = $apellido;

    $estu->guardar_datos();
}
?>
