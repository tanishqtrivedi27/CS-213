<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style>
  table, th, td {
       border: 1px solid black;
        border-collapse: collapse;
    }
  </style>
<body>
<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "classicmodels";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM employees WHERE firstName LIKE '_e%'";
$result = $conn->query($sql);

echo "<table>";
echo "<th> employeeNumber </th>";
echo "<th> lastName </th>";
echo "<th> firstName </th>";
echo "<th> extension </th>";
echo "<th> email </th>";
echo "<th> officeCode </th>";
echo "<th> reportsTo </th>";
echo "<th> jobTitle </th>";
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>".$row["employeeNumber"]. "</td>";
    echo "<td>" .$row["lastName"]. "</td>";
    echo "<td>" . $row["firstName"]."</td>";
    echo "<td>" . $row["extension"]."</td>";
    echo "<td>" . $row["email"]."</td>";
    echo "<td>" . $row["officeCode"]."</td>";
    echo "<td>" . $row["reportsTo"]."</td>";
    echo "<td>" . $row["jobTitle"]."</td>";
    echo "</tr>";
  }
} else {
  echo "0 results";
}
$conn->close();

echo"</table>";
?>
</body>
</html>