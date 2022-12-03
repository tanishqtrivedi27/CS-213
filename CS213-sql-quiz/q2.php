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

$sql = "SELECT COUNT(employees.employeeNumber), offices.officeCode, offices.city FROM offices 
        INNER JOIN employees 
        ON offices.officeCode  = employees.officeCode
        GROUP BY employees.officeCode
        HAVING COUNT(employees.employeeNumber) >= 3";

// $sql = "SELECT COUNT(employees.employeeNumber), offices.officeCode, offices.city 
//         FROM offices, employees
//         WHERE offices.officeCode  = employees.officeCode
//         GROUP BY employees.officeCode
//         HAVING COUNT(employees.employeeNumber) >= 3";

// $sql = "SELECT COUNT(employees.employeeNumber), officeCode FROM employees GROUP BY officeCode";

$result = $conn->query($sql);

echo "<table>";

echo "<th> COUNT(employeeNumber) </th>";
echo "<th> officeCode </th>";
echo "<th> city </th>";


if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "<tr>";
    echo "<td>".$row["COUNT(employees.employeeNumber)"]. "</td>";
    echo "<td>".$row["officeCode"]. "</td>";
    echo "<td>".$row["city"]. "</td>";
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