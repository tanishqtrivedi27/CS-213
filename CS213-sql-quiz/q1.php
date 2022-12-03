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

$sql = "SELECT * FROM offices";
$result = $conn->query($sql);

echo "<table>";
echo "<th> officeCode </th>";
echo "<th> city </th>";
echo "<th> phone </th>";
echo "<th> addressLine1 </th>";
echo "<th> addressLine2 </th>";
echo "<th> state </th>";
echo "<th> country </th>";
echo "<th> postalCode </th>";
echo "<th> territory </th>";
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>".$row["officeCode"]. "</td>";
    echo "<td>" .$row["city"]. "</td>";
    echo "<td>" . $row["phone"]."</td>";
    echo "<td>" . $row["addressLine1"]."</td>";
    echo "<td>" . $row["addressLine2"]."</td>";
    echo "<td>" . $row["state"]."</td>";
    echo "<td>" . $row["country"]."</td>";
    echo "<td>" . $row["postalCode"]."</td>";
    echo "<td>" . $row["territory"]."</td>";
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