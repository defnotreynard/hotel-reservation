<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "hotelMS";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get POST values
$name = $_POST['name'] ?? '';
$email = $_POST['email'] ?? '';
$password = $_POST['password'] ?? '';
$confirm_password = $_POST['confirm_password'] ?? '';

// Check required fields
if (empty($name) || empty($email) || empty($password) || empty($confirm_password)) {
  die("❌ All fields are required.");
}

// Check if passwords match
if ($password !== $confirm_password) {
  die("❌ Passwords do not match.");
}

// Insert into DB
$sql = "INSERT INTO register (name, email, password, role) VALUES (?, ?, ?, 'admin')";

$stmt = $conn->prepare($sql);
$stmt->bind_param("sss", $name, $email, $password);

if ($stmt->execute()) {
  echo "✅ Registration successful! <a href='login.html'>Go to Login</a>";
} else {
  echo "❌ Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
