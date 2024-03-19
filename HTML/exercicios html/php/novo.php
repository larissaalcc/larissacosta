<?php

$host = '127.0.0.1';
$database = 'banco de dados';
$user = 'larissa';
$password ='usuario';

$con = new mysqli ($host, $user, $password,$database);

if($con){
//  echo 'conectado com sucesso';
}else{
    echo 'ERRO AO CONECTAR!';
}


