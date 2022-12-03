<?php
// Start the session
session_start();
?>

<html>
<body>

<?php
if (isset($_SERVER["HTTP_REFERER"]) and strpos($_SERVER["HTTP_REFERER"], "welcome.php")) {
	if (count($_GET["colors"]) < 5) {
		echo "Select 5 or more colors.";
	} else {	
		sort($_GET["colors"]);

		foreach ($_GET["colors"] as $x) {
			echo $x . "<br>";
		}
	}

	echo "<form action=\"welcome.php\">
			<input type=\"submit\" value=\"Back\">
			</form>";

	echo "<form action=\"login.php\">
			<input type=\"submit\" value=\"Logout\">
			</form>";
} else
	echo "Unauthenticated access.";
?>

</body>
</html>