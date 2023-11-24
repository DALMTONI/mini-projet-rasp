<?php
$color = $_POST['color'];
$color2 = $_POST['color2'];
error_log("Color received: $color", 0);

if ($color == 'off') {
    
    exec('sudo -u www-data /usr/bin/pkill python');
    exec('sudo -u www-data /usr/bin/python3 /var/www/html/led_on_off_RGB.py 0 0 0');
    
    echo "eteindre";
}
else {
   
   
     // Convertir la couleur hexadécimale en valeurs RGB
        list($r, $g, $b) = sscanf($color2, "#%02x%02x%02x");
        

        // Exécuter le script Python avec les valeurs RGB
        exec("sudo -u www-data /usr/bin/python3 /var/www/html/led_on_off_RGB.py $r $g $b");
        
        echo ($r.' '.$g.' '.$b) ;
        echo('test2');
}
?>
