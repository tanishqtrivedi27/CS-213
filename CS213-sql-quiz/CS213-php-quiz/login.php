<html>
<body>

<?php
if (session_status() === PHP_SESSION_ACTIVE)
	session_destroy();
?>

<form action="welcome.php" method="post">
Username: <input type="text" name="username" required placeholder="username"><br>
Password: <input type="password" name="password" required placeholder="password"><br>

<input type="submit">
</form>

</body>
</html>