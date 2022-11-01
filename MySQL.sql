function showDatabases()
        {
           $sql = "SHOW DATABASES";
           $pdo = new pdo('mysql:host=localhost;',
                         'newuser', 'password');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_WARNING);
           $stmt = $pdo->prepare($sql);
           $stmt->execute();
$stmt->setFetchMode(PDO::FETCH_ASSOC);
           while ($row = $stmt->fetch())
           {
                 print("<h3>" . $row['Database'] . "</h3>");
} }