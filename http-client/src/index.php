<html>
    <head>
        <title>Kursovaya</title>
    </head>
    <body>
        <h2>Изменить кавычки</h2>
        <h3>Строка с кавычками</h3>
        <?php
            if (isset($_POST['s'])){
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['s'],
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                echo "Ответ на Ваш запрос: ".$response;
            }
        ?>
        <form action="index.php" method="post">
            <label for="str">Введите строку: </label>
            <input placeholder="Писать сюда" type="text" name="s" id="s" required>
            <input type="submit" value="Отправить">
        </form>
    </body>
</html>