<?php

include_once("conn.php");
$conn = new Conexion();

$id_a_eliminar = htmlspecialchars($_GET["id"], ENT_QUOTES);

$sql = "DELETE FROM estudiantes WHERE id = $id_a_eliminar";

if ($conn->query($sql) === TRUE) {
    echo "Registro eliminado exitosamente";
} else {
    echo "Error al eliminar el registro: " . $conn->error;
}

$conn->close();
?>
