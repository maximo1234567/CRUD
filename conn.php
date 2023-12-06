<?
define ('DB_HOST','db.tecnica4berazategui.edu.ar');
define ('DB_USER','lperconti_g1');
define ('DB_PASS','Syssen23');
define ('DB_NAME','lperconti_g1'); 

class Conexion extends mysqli {
    public $enlace;

    function __construct() {
        parent::__construct(DB_HOST, DB_USER, DB_PASS, DB_NAME);
        if ($this->connect_error) {
            die('Error de conexión (' . $this->connect_errno . ') ' . $this->connect_error);
        }
    }

    function __destruct() {
        $this->close();
    }
}
