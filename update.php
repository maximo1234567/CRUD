<?php
include_once("conn.php");
$conn = new Conexion();

$id = $_GET['id'];
$dni = $_GET['dni'];
$sexo = $_GET['sexo'];
$nombres = $_GET['nombres'];
$apellidos = $_GET['apellidos'];

$sql = "UPDATE estudiantes SET dni='$dni', sexo='$sexo', nombres='$nombres', apellidos='$apellidos' WHERE id=$id";

if ($conn->query($sql) === TRUE) {
    echo "Registro actualizado correctamente";
} else {
    echo "Error al actualizar el registro: " . $conn->error;
}

$conn->close();
?>
