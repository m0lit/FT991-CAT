<?php
$par = $_GET['par'];
system("sudo python /home/pi/dev/python/ft991a.py ".$par);
header('Location: ' . $_SERVER["HTTP_REFERER"] );
exit;
?>
