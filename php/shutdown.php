#!/usr/bin/php
<?php

system("sudo poweroff");

header('Location: ' . $_SERVER["HTTP_REFERER"] );
exit;

?>
