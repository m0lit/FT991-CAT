#!/usr/bin/php
<?php

system("sudo reboot");

header('Location: ' . $_SERVER["HTTP_REFERER"] );
exit;

?>
