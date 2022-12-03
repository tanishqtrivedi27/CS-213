<?php
// Start the session
session_start();
?>

<html>
<body>

<?php
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

// define variables and set to empty values
if (isset($_SERVER["HTTP_REFERER"]) and strpos($_SERVER["HTTP_REFERER"], "login.php")) {
	$_SESSION["username"] = test_input($_SERVER["REQUEST_METHOD"] == "POST" ? $_POST["username"] : $_GET["username"]);
	$_SESSION["password"] = test_input($_SERVER["REQUEST_METHOD"] == "POST" ? $_POST["password"] : $_GET["password"]);
	
	if ($_SESSION["username"]!="ssl" or $_SESSION["password"]!="123") {
		session_destroy();
		echo "Incorrect login credentials . <br>
				<form action=\"login.php\">
				<input type=\"submit\" value=\"Back\">
				</form>";
	} else {
		echo "Welcome " . $_SESSION["username"] . "<br>" .
		"<form action=\"logout.php\">
		<select name=\"colors[]\" size=\"10\" multiple>
		  <option value=\"black\">Black</option>
		  <option value=\"blue\">Blue</option>
		  <option value=\"violet\">Violet</option>
		  <option value=\"brown\">Brown</option>
		  <option value=\"gold\">Gold</option>
		  <option value=\"green\">Green</option>
		  <option value=\"orange\">Orange</option>
		  <option value=\"pink\">Pink</option>
		  <option value=\"red\">Red</option>
		  <option value=\"yellow\">Yellow</option>
		</select>
		<br>
		<input type=\"submit\" value=\"Submit\">
		</form>

		<form action=\"login.php\">
		<input type=\"submit\" value=\"Logout\">
		</form>";
	}
} elseif (isset($_SERVER["HTTP_REFERER"]) and strpos($_SERVER["HTTP_REFERER"], "logout.php") and session_status() === PHP_SESSION_ACTIVE) {
	echo "</form>
	<form action=\"login.php\">
	<input type=\"submit\" value=\"Logout\">
	</form>";
} else
	echo "Unauthenticated access.";

?>

</body>
</html>