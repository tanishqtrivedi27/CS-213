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


// $sql = "SELECT customers.customerNumber, SUM(orderdetails.quantityOrdered*orderdetails.priceEach)
//         FROM customers, orders, orderdetails
//         WHERE (customers.customerNumber = orders.customerNumber AND orders.orderNumber = orderdetails.orderNumber)
//         GROUP BY customers.customerNumber
//         HAVING SUM(orderdetails.quantityOrdered*orderdetails.priceEach) > 150000
//         ORDER BY SUM(orderdetails.quantityOrdered*orderdetails.priceEach) DESC";

$sql = "SELECT customers.customerNumber, SUM(orderdetails.quantityOrdered*orderdetails.priceEach)
        FROM ((customers
        INNER JOIN orders ON customers.customerNumber = orders.customerNumber)
        INNER JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber)
        GROUP BY customers.customerNumber
        HAVING SUM(orderdetails.quantityOrdered*orderdetails.priceEach) > 150000
        ORDER BY SUM(orderdetails.quantityOrdered*orderdetails.priceEach) DESC";

$result = $conn->query($sql);

echo "<table>";

echo "<th> customerNumber </th>";
echo "<th> orderValue </th>";

if ($result->num_rows > 0) {
  while($row = $result->fetch_assoc()) {
    echo "<tr><td>".$row["customerNumber"]."</td><td>".$row["SUM(orderdetails.quantityOrdered*orderdetails.priceEach)"]."</td></tr>";
  }
} 
else {
  echo "0 results";
}
$conn->close();

echo"</table>";
?>
</body>
</html>