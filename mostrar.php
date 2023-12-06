<?php

include_once("conn.php");
$conn = new Conexion();


$sql = "SELECT * FROM estudiantes";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $data = array();

    while ($row = $result->fetch_assoc()) {
        $data[] = $row;
    }

    // Convertir el array a formato JSON y mostrarlo
    echo json_encode($data);
} else {
    echo "No se encontraron resultados";
}

$conn->close();
?>
